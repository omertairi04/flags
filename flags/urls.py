from django.urls import path
from . import views

urlpatterns = [
    path('', views.selectingGame , name='selecting'),
    path('play/<str:pk>/', views.index , name='play'),
]