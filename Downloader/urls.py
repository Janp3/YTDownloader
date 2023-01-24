from django.urls import path

from . import views

app_name = 'app_downloader'

urlpatterns = [
    path('', views.home, name='home'),
    path('download-videos/', views.videos, name='videos'),
    path('download-musics/', views.musics, name='musics'),
]
