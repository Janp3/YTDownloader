from os import getlogin

from django.contrib import messages
from django.shortcuts import render

from .utils.downloader.functions.downloading import (download_music,
                                                     download_video)

# Create your views here.


def home(request):
    return render(request, 'downloader/pages/home.html')


def videos(request):
    link = ''
    user = getlogin()
    if request.method == 'GET':
        return render(request, 'downloader/pages/videos.html')
    else:
        link = request.POST.get('url-video')
        if link == '':
            messages.warning(request, 'Você deve inserir uma URL.')
            return render(request, 'downloader/pages/videos.html')
        elif download_video(link=link, user=user) is False:
            messages.warning(request, 'Url inválida ou não encontrada')
            return render(request, 'downloader/pages/videos.html')
        else:
            messages.success(
                request, f'O video foi baixado em C:/users/{user}/downloads/')
            download_video(link=link, user=user)

            return render(request, 'downloader/pages/videos.html')


def musics(request):
    link = ''
    user = getlogin()
    if request.method == 'GET':
        return render(request, 'downloader/pages/music.html')
    else:
        link = request.POST.get('url-music')
        if link == '':
            messages.warning(request, 'Você deve inserir uma URL.')
            return render(request, 'downloader/pages/music.html')
        elif download_music(link=link, user=user) is False:
            messages.warning(request, 'Url inválida ou não encontrada')
            return render(request, 'downloader/pages/music.html')
        else:
            messages.success(
                request, f'A música foi baixado em C:/users/{user}/downloads/')
            download_music(link=link, user=user)
            return render(request, 'downloader/pages/music.html')
