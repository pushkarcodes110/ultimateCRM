from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from core.views import index, about
from userprofile.views import signup, account
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/accounts/', account, name='account'),
    path('dashboard/teams/', include('teams.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/',about, name='about' ),
    path('sign-up/', signup, name='signup'), 
    path('log-in/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include("django.contrib.auth.urls")),
]
