# Create your views here.
from rest_framework import viewsets

from exercises.models import Exercise, ExerciseBook, ExerciseCard
from exercises.serializers import ExerciseBookSerializer, ExerciseCardSerializer, ExerciseSerializer


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


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_fields = ('id', 'exercise_card')
    # permission_classes = [IsAccountAdminOrReadOnly]
