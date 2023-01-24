from django.shortcuts import render

from Downloader.utils.downloader.functions.downloading import download_video

# Create your views here.


def home(request):
    return render(request, 'downloader/pages/home.html')


def videos(request):
    if request.method == 'GET':
        return render(request, 'downloader')

    context = {
        'video': download_video()
    }
    return render(request, 'downloader/pages/videos.html',
                  context=context)
