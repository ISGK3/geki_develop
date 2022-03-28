from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.top),
    path('music_list/', views.musicListView.as_view(), name='music_list'),
    path('music_list/detail/<str:title>', views.musicDetail.as_view(), name='music_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
