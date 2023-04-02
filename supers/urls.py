from django.urls import path 
from . import views


urlpattern = [
    path('supers/', views.supers_list),
]