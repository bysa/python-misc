

from __future__ import unicode_literals
import youtube_dl

videos = [
'https://www.youtube.com/watch?v=vaG5vKKkGJk', 
'https://www.youtube.com/watch?v=7XXbyvdLgVM'
]


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':'%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for video in videos:
		ydl.download([video])