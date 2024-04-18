import pytube
from pytube import YouTube
import tkinter as tk

# intitalize

root = tk.Tk()

url_entry = tk.Entry(root)
url_entry.pack()

def DownloadMP4():
    video_object = YouTube(str(url_entry.get()))
    video_object.streams.get_highest_resolution().download()

def DownloadMP3():
    video_object = YouTube(str(url_entry.get()))
    video_object.streams.get_audio_only().download()

button_mp4 = tk.Button(root, text="Download MP4", command=DownloadMP4)
button_mp4.pack()

button_mp3 = tk.Button(root, text="Download MP3", command=DownloadMP3)
button_mp3.pack()

# video information
'''
print(video_object.title)
print(f'{video_object.length / 60} minutes')
print(video_object.views)
print(video_object.author)
print(video_object.description)
'''

# video streams

#download

#closing

root.mainloop()