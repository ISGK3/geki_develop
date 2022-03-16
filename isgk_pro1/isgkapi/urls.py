from django.urls import path
from isgkapi.views import hello


urlpatterns = [
    path('hello/', hello, name='hello'),
]