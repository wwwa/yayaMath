from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework import viewsets

from myaccount.serializers import UserProfileSerializer
from .forms import ProfileForm
from .models import UserProfile


@login_required
def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {'user': user})


@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.save()

            return HttpResponseRedirect(reverse('myaccount:profile'))
    else:
        default_data = {
            'first_name': user.first_name, 'last_name': user.last_name,
            'org': user_profile.org, 'telephone': user_profile.telephone,
        }
        form = ProfileForm(default_data)

    return render(request, 'account/profile_update.html', {'form': form, 'user': user})


class UserProfileExerciseViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_fields = ('id', 'user')
    # permission_classes = [IsAccountAdminOrReadOnly]
