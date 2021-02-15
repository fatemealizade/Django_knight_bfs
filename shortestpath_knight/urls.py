from django.urls import path, include
from . import views
urlpatterns = [
    path('shortestpath/', views.knight_game)
]