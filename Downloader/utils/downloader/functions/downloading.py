import os
from tkinter import filedialog

from pytube import YouTube


def download_video(link, user):
    try:
        link = 'https://www.youtube.com/watch?v=gtlUVlnpwq8&list=RDgtlUVlnpwq8&start_radio=1'
        path = f'C:/Users/{user}/Downloads/'
        yt = YouTube(link)
        # Fazer o dowload
        ys = yt.streams.filter(
            subtype='mp4', only_video=False, resolution='720p').first().download(path)
        print("Download Completo")
    except:
        print("Algo deu errado!")
        print("Algo deu errado!")


# def download_music():
#     try:
#         link = 'https://www.youtube.com/watch?v=yKNxeF4KMsY'
#         path = 'C:/Users/jeanc/Downloads/'
#         # url do youtube
#         yt = YouTube(link)

#         # Extraindo o audio do video
#         video = yt.streams.filter(only_audio=True).first()

#         # Conferir diretorio do usuário
#         destination = path or '.'
#         out_file = video.download(output_path=destination)

#         # save the file
#         base, ext = os.path.splitext(out_file)
#         new_file = base + '.mp3'
#         os.rename(out_file, new_file)

#         # result of success
#         print(yt.title + " foi baixado com sucesso.")
#     except:
#         print('Algo deu errado')
#         print('Algo deu errado')
