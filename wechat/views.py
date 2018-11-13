import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from wechat.models import WechatUserInfo
from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt

# APP_ID = 'wxd7c16b2190e782cd'
APP_ID = 'wx99d68cd2072a86a0'
# APP_SECRET = 'fcce07e362a6a6bba72a088f95881d09'
APP_SECRET = '611965561426261e9114734c37a8b188'


@csrf_exempt
def wechat_auth(request):
    """

    :param request:
    :return:
    """
    data = json.loads(request.body)
    code = data.get('code')

    api = WXAPPAPI(appid=APP_ID,
                   app_secret=APP_SECRET)
    session_key = ''
    if code:
        session_info = api.exchange_code_for_session_key(code=code)
        # 获取session_info 后
        session_key = session_info.get('session_key')

    resp_data = {
        'data': {
            'session_key': session_key,
        },
        'msg': 'hello world',
        'code': 0,
    }
    return JsonResponse(resp_data)


@csrf_exempt
def get_wechat_user_info(request):
    """

    :param request:
    :return:
    """
    data = json.loads(request.body)
    session_key = data.get('session_key')
    encrypted_data = data.get('encryptedData')
    iv = data.get('iv')

    crypt = WXBizDataCrypt(APP_ID, session_key)

    # encrypted_data 包括敏感数据在内的完整用户信息的加密数据
    # iv 加密算法的初始向量
    # 这两个参数需要js获取

    user_info = crypt.decrypt(encrypted_data, iv)
    watermark = user_info.pop('watermark')

    error_data = {'code': -1, 'data': {}, 'msg': 'not valid user info'}
    if not watermark:
        return JsonResponse(error_data)

    appid = watermark.get('appid')

    if appid != APP_ID:
        return JsonResponse(error_data)

    timestamp = watermark.get('timestamp', 0)
    user_info['timestamp'] = timestamp
    user_info['session_key'] = session_key

    openId = user_info.get('openId')

    if openId:
        wechat_users = WechatUserInfo.objects.filter(openId=openId, is_valid=True)
        if wechat_users.count():
            # 已经存在
            wechat_user = wechat_users.first()
        else:
            # 首次用微信登录
            wechat_user = WechatUserInfo(**user_info)
            wechat_user.save()
            WechatUserInfo.create_user(wechat_user)
        user_profile = wechat_user.userprofile_set.get()
        user_profile_dict = user_profile.__dict__
        user_profile_dict['id'] = user_profile_dict['user_id']
        user_profile_dict.pop('_state')

        user_info.update(user_profile_dict)

    # 能够获取到openID,unionID,能够唯一识别是某一个微信用户了
    # 也就能够和本地系统的用户关联了
    resp_data = {
        'data': user_info,
        'code': 0,
    }

    return JsonResponse(resp_data)
