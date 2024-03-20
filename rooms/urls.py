from django.contrib import admin
from django.urls import path, include
from .views import home, room1, room2, room3

urlpatterns = [
    path("",  home, name='home'),
    path("1",  room1, name='one'),
    path("2",  room2, name='two'),
    path("3",  room3, name='three'),
]