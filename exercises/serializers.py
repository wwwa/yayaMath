# coding: utf-8
"""
@author
@date
@content

"""
from rest_framework import serializers

from exercises.models import Exercise, ExerciseBook, ExerciseCard


class ExerciseBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseBook
        fields = ('id', 'name', 'description')


class ExerciseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCard
        fields = ('id', 'name', 'count', 'description')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'question', 'answer', 'description')
