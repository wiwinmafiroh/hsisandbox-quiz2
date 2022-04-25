from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.pesertahsi, name="pesertahsi"),
] 