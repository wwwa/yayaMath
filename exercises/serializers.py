# coding: utf-8
"""
@author
@date
@content

"""

from base.serializers import MyListSerializer, MyModelSerializer, MyRandomListSerializer
from exercises.models import Exercise, ExerciseBook, ExerciseCard, ExerciseCardRecord, Record


class ExerciseBookSerializer(MyModelSerializer):
    class Meta:
        list_serializer_class = MyListSerializer
        model = ExerciseBook
        fields = ('id', 'name', 'description')


class ExerciseCardSerializer(MyModelSerializer):
    class Meta:
        list_serializer_class = MyListSerializer
        model = ExerciseCard
        fields = ('id', 'name', 'count', 'description', 'exercise_book')


class ExerciseSerializer(MyModelSerializer):
    class Meta:
        list_serializer_class = MyRandomListSerializer
        model = Exercise
        fields = ('id', 'question', 'answer', 'description', 'exercise_card')


class RecordSerializer(MyModelSerializer):
    class Meta:
        list_serializer_class = MyListSerializer
        model = Record
        fields = ('id', 'user', 'user_answer', 'exercise', 'exercise_card')


class ExerciseCardRecordSerializer(MyModelSerializer):
    class Meta:
        list_serializer_class = MyListSerializer
        model = ExerciseCardRecord
        fields = ('id', 'user', 'add_time', 'total_time', 'right_ratio', 'exercise_card', 'add_day', 'total_seconds')
