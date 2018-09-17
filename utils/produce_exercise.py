# coding: utf-8
"""
@author
@date
@content

生成题库
"""
import os

import django

print(os.environ)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primaryMath.settings')
django.setup()

from exercises.models import Exercise, ExerciseBook, ExerciseCard

exercise_book, create = ExerciseBook.objects.get_or_create(name='乘法运算')

exercise_card, _ = ExerciseCard.objects.get_or_create(name='一位乘以两位', exercise_book=exercise_book)
exercise_card.description = '如: 8×15'
exercise_card.save()

for x in range(1, 10):
    for y in range(10, 20):
        question = f'{x}×{y}'
        answer = x * y
        exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_card, _ = ExerciseCard.objects.get_or_create(name='乘以25', exercise_book=exercise_book)
exercise_card.description = '如: 4×25,12×25'
exercise_card.save()

for x in range(1, 20):
    for i in (1, 2, 5, 10):
        y = 25
        x *= i
        question = f'{x}×{y}'
        answer = x * y
        exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)
exercise_card, _ = ExerciseCard.objects.get_or_create(name='一位乘以25', exercise_book=exercise_book)
exercise_card.description = '如: 4×25'
exercise_card.save()

for x in range(1, 11):
    y = 25
    question = f'{x}×{y}'
    answer = x * y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_card, _ = ExerciseCard.objects.get_or_create(name='两位乘以25', exercise_book=exercise_book)
exercise_card.description = '如: 4×25'
exercise_card.save()

for x in range(10, 21):
    y = 25
    question = f'{x}×{y}'
    answer = x * y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_card, _ = ExerciseCard.objects.get_or_create(name='一位乘以15', exercise_book=exercise_book)
exercise_card.description = '如: 4×15'
exercise_card.save()

for x in range(1, 11):
    y = 15
    question = f'{x}×{y}'
    answer = x * y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_card, _ = ExerciseCard.objects.get_or_create(name='一位乘以125', exercise_book=exercise_book)
exercise_card.description = '如: 4×125'
exercise_card.save()

for x in range(1, 11):
    y = 125
    question = f'{x}×{y}'
    answer = x * y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_book, create = ExerciseBook.objects.get_or_create(name='除法运算')

exercise_card, _ = ExerciseCard.objects.get_or_create(name='三位除以两位', exercise_book=exercise_book)
exercise_card.description = '如: 128÷16'
exercise_card.save()

for x in range(1, 10):
    for y in range(10, 20):
        result = x * y

        question = f'{result}÷{y}'
        answer = x
        print(result, answer)

        if result < 100:
            continue
        exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_book, create = ExerciseBook.objects.get_or_create(name='小数运算')
exercise_card, _ = ExerciseCard.objects.get_or_create(name='除以10', exercise_book=exercise_book)
exercise_card.description = '如: 15÷10'
exercise_card.save()

for x in range(1, 10):
    y = 10
    question = f'{x}÷{y}'
    answer = x / y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

for x in range(1, 100, 3):
    y = 10
    question = f'{x}÷{y}'
    answer = x / y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_card, _ = ExerciseCard.objects.get_or_create(name='除以5', exercise_book=exercise_book)
exercise_card.description = '如: 15÷5'
exercise_card.save()

for x in range(1, 10):
    y = 5
    question = f'{x}÷{y}'
    answer = x / y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

for x in range(1, 100, 3):
    y = 5
    question = f'{x}÷{y}'
    answer = x / y
    exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_card, _ = ExerciseCard.objects.get_or_create(name='小数加法', exercise_book=exercise_book)
exercise_card.description = '如: 1.25+0.7'
exercise_card.save()

for x in range(1, 100, 3):
    a = x / 10
    for y in range(10, 200, 4):
        b = y / 10
        question = f'{a}+{b}'
        answer = (x + y) / 10
        answer = str(answer)

        exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)
        if answer.endswith('.0'):
            print(question, answer, len(answer))
            answer = answer.rstrip('.0')
            exercise.answer = answer
            exercise.save()

exercise_card, _ = ExerciseCard.objects.get_or_create(name='小数除法', exercise_book=exercise_book)
exercise_card.description = '如: 9.6÷0.2'
exercise_card.save()

for x in range(1, 100):
    a = x / 10
    for y in (1, 2, 4, 5, 8):
        question = f'{a}÷{y}'
        answer = round(a / y, 5)
        answer = str(answer)
        if answer.endswith('.0'):
            answer = answer.rstrip('.0')
        exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)

exercise_card, _ = ExerciseCard.objects.get_or_create(name='小数乘法', exercise_book=exercise_book)
exercise_card.description = '如: 1.25x0.7'
exercise_card.save()

for x in range(1, 200, 6):
    x = x / 10
    for y in range(1, 100, 4):
        y = y / 10
        question = f'{x}×{y}'
        answer = str(x * y)

        if len(answer) > 5:
            continue

        exercise, _ = Exercise.objects.get_or_create(question=question, answer=answer, exercise_card=exercise_card)
