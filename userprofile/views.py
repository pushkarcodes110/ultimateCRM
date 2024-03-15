from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import UserProfile
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

            return redirect ('/log-in/')
    else:
        form = UserCreationForm()
 
    context={'form': form}

    return render(request, 'registration/signup.html', context)



