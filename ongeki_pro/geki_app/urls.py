from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.top),
    path('music_list/', views.musicListView.as_view(), name='music_list'),
]
