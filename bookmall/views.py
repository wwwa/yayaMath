# Create your views here.
from rest_framework import viewsets

from bookmall.models import BookMall, Tag
from bookmall.serializers import BookMallSerializer, TagSerializer


class BookMallViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = BookMall.objects.all()
    serializer_class = BookMallSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
