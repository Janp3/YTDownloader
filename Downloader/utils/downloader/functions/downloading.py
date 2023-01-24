import os

from pytube import YouTube


def download_video(link, user):
    try:
        link = link
        path = f'C:/Users/{user}/Downloads/'
        yt = YouTube(link)
        # Fazer o dowload
        ys = yt.streams.filter(
            subtype='mp4', only_video=False, resolution='720p').first().download(path)
        print("Download Completo")

    except:
        return False


def download_music(link, user):
    try:
        link = link
        path = f'C:/Users/{user}/Downloads/'
        # url do youtube
        yt = YouTube(link)

        # Extraindo o audio do video
        video = yt.streams.filter(only_audio=True).first()

        # Conferir diretorio do usuário
        destination = path or '.'
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " foi baixado com sucesso.")
    except:
        return False
