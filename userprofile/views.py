from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import UserProfile
from teams.models import Team
# In your views.py
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

# Create your views here.
def signup(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)

            team =Team.objects.create(name='The Team Name', created_by=request.user)
            team.members.add(request.user)
            team.save()

            return redirect ('/log-in/')
    else:
        form = UserCreationForm()
 
    context={'form': form}

    return render(request, 'registration/signup.html', context)

@login_required 
def account(request):
    team=Team.objects.filter(created_by=request.user)[0]

    return render(request, 'registration/account.html', {
        'team': team
    })



