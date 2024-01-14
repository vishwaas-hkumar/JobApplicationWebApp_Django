from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') #calling path function for home page
]