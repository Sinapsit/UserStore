"""Promo app urlconf."""
from django.urls import path

from account import views

app_name = 'users'

urlpatterns = [
    path('', views.UserView.as_view(), name='user_list'),
    path('<int:pk>/', views.PersonView.as_view(), name='personal'),
]