# coding: utf-8
"""
@author
@date
@content

"""

from base.serializers import MyListSerializer, MyModelSerializer
from myaccount.models import UserProfile


class UserProfileSerializer(MyModelSerializer):
    class Meta:
        list_serializer_class = MyListSerializer
        model = UserProfile
        fields = ('id', 'user', 'org', 'telephone', 'wechat')
