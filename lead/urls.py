from django.urls import path
from . import views

urlpatterns =[
    path('add-lead/', views.add_lead, name='add_lead'),
    path('<int:pk>/', views.leads_details, name="leads_detail"),
    path('<int:pk>/delete/', views.lead_delete, name="leads_delete"),
    path('<int:pk>/edit /', views.leads_edit, name="leads_edit"),

    path('', views.leads_list, name='leads_list'),
]