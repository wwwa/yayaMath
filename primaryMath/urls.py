"""primaryMath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view

# Serializers define the API representation.
from bookmall.views import BookMallViewSet, TagViewSet
from exercises.views import ExerciseBookViewSet, ExerciseCardViewSet, ExerciseViewSet, RecordViewSet, \
    ExerciseCardRecordViewSet
from myaccount.views import UserProfileExerciseViewSet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user_profile', UserProfileExerciseViewSet)
router.register(r'records', RecordViewSet)
router.register(r'exercise_card_records', ExerciseCardRecordViewSet)
router.register(r'exercise_books', ExerciseBookViewSet)
router.register(r'exercise_cards', ExerciseCardViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'bookmalls', BookMallViewSet)
router.register(r'tags', TagViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    path('accounts/', include('myaccount.urls')),
    path('wechat/', include('wechat.urls')),
    path('admin/', admin.site.urls),
    url(r'docs/', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
