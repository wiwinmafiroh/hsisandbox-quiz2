from django.urls import path
from . import views

urlpatterns = [
  path('', views.adminhsi, name="adminhsi")
]