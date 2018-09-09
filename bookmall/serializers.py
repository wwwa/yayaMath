# coding: utf-8
"""
@author
@date
@content

"""
from rest_framework import serializers

from bookmall.models import BookMall, Tag


class BookMallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMall
        fields = ('id', 'title', 'content')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'value')
