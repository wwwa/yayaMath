# coding: utf-8
"""
@author
@date
@content

"""
import random

from drf_queryfields import QueryFieldsMixin
from rest_framework import serializers


def ret_data(data=(), status='ok', code=0, msg=''):
    """

    :param data:
    :param status:
    :param code:
    :param msg:
    :return:
    """
    return {'status': status, 'code': code, 'data': data, 'msg': msg}


class MyListSerializer(serializers.ListSerializer):
    """

    """

    @property
    def data(self):
        data = super(MyListSerializer, self).data

        return ret_data(data)


class MyRandomListSerializer(serializers.ListSerializer):
    """

    """

    @property
    def data(self):
        data = super(MyRandomListSerializer, self).data
        random.shuffle(data)
        return ret_data(data[:30])


class MyModelSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    """

    """

    @property
    def data(self):
        data = super(MyModelSerializer, self).data

        return ret_data(data)
