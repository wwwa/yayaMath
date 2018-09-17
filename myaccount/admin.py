from django.contrib import admin

# Register your models here.
from myaccount.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """

    """

    list_display = ['user', 'org', 'telephone', 'mod_date', 'account_verified', 'wechat']


admin.site.register(UserProfile, UserProfileAdmin)
