from django.contrib import admin

# Register your models here.
from wechat.models import WechatUserInfo


class WechatUserInfoAdmin(admin.ModelAdmin):
    """

    """

    list_display = ['openId', 'nickName', 'avatar', 'sex', 'province', 'city', 'is_valid', 'session_key']


admin.site.register(WechatUserInfo, WechatUserInfoAdmin)
