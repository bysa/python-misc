

from __future__ import unicode_literals
import youtube_dl

videos = ['https://www.youtube.com/watch?v=liEPFoj4qfw',
          'https://www.youtube.com/watch?v=hdaccSL_Ph0', 'https://www.youtube.com/watch?v=vaG5vKKkGJk']


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for video in videos:
        ydl.download([video])


# requirement package: youtube_dl
# ubuntu: sudo apt-get install ffmpeg
# windows: https://stackoverflow.com/questions/30770155/ffprobe-or-avprobe-not-found-please-install-one#answer-41822439
