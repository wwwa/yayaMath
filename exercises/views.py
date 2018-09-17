# Create your views here.
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from base.serializers import ret_data
from exercises.models import Exercise, ExerciseBook, ExerciseCard, ExerciseCardRecord, Record
from exercises.serializers import ExerciseBookSerializer, ExerciseCardRecordSerializer, ExerciseCardSerializer, \
    ExerciseSerializer, RecordSerializer


class ExerciseBookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ExerciseBook.objects.all()
    serializer_class = ExerciseBookSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


class ExerciseCardViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ExerciseCard.objects.all()
    serializer_class = ExerciseCardSerializer
    filter_fields = ('id', 'name', 'exercise_book')
    # permission_classes = [IsAccountAdminOrReadOnly]


class ExerciseCardRecordViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ExerciseCardRecord.objects.all().order_by('-add_time')
    serializer_class = ExerciseCardRecordSerializer
    filter_fields = ('id', 'user', 'add_time', 'total_time', 'right_ratio', 'exercise_card')
    # permission_classes = [IsAccountAdminOrReadOnly]


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_fields = ('id', 'exercise_card')
    # permission_classes = [IsAccountAdminOrReadOnly]


class RecordViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_fields = ('id', 'exercise_card')

    # permission_classes = [IsAccountAdminOrReadOnly]

    @action(methods=['post'], detail=False)
    def bulk_insert(self, request):
        """
        批量插入答题记录
        :return:
        """

        data = request.data

        records = data['records']
        right_ratio = data['right_ratio']

        user = User(id=data['user_id'])
        exercise_card = ExerciseCard(id=data['exercise_card_id'])
        exercise_card_record = ExerciseCardRecord(
            user=user,
            exercise_card=exercise_card,
            total_time=data['total_time'],
            right_ratio=right_ratio,
        )
        exercise_card_record.save()

        for value in records:
            value.pop('id')
            delta_time = value['delta_time']
            record = Record(
                is_right=value['is_right'],
                user_answer=value['user_answer'],
                delta_time=delta_time,
                exercise_card_record=exercise_card_record,
            )
            record.user = user
            record.exercise_card = exercise_card
            record.exercise = Exercise(id=value['exercise'])
            record.save()

        data = ret_data()
        return JsonResponse(data)
