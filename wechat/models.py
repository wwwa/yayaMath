from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe


class WechatUserInfo(models.Model):
    """
    微信用户信息
    """
    add_time = models.DateTimeField('添加时间', auto_now=True)
    openId = models.CharField('openId', max_length=128, blank=True)
    nickName = models.CharField('昵称', max_length=128, blank=True)
    avatarUrl = models.CharField('头像', max_length=128, blank=True)
    gender = models.IntegerField('性别', blank=True)
    country = models.CharField('国家', max_length=24, blank=True)
    province = models.CharField('省份', max_length=24, blank=True)
    city = models.CharField('城市', max_length=24, blank=True)
    language = models.CharField('语言', max_length=10, blank=True)
    timestamp = models.IntegerField('时间戳')
    is_valid = models.BooleanField('是否有效', default=True)
    session_key = models.CharField('session_key', max_length=128, blank=True)

    def __str__(self):
        return f'{self.nickName}'

    def avatar(self):
        avatar_html = f"<img src={self.avatarUrl}> </img>"
        return mark_safe(avatar_html)

    def sex(self):
        return '男' if self.gender == 1 else '女'

    @staticmethod
    def create_user(wechat_user):
        """
        当openId不存在时,新建一个用户,和其对应的 UserProfile
        :return:
        """
        from myaccount.models import UserProfile
        from pypinyin import lazy_pinyin
        import datetime

        username = lazy_pinyin(wechat_user.nickName, errors='ignore')
        now = datetime.datetime.now()
        print('-' * 100)
        print(username, now)
        username = ''.join(username) + '_' + str(now)
        username = username.replace(' ', '_')
        print(username)
        user = User(username=username, first_name=wechat_user.nickName)
        user.save()

        user_profile = UserProfile(user=user, wechat=wechat_user)
        user_profile.save()
