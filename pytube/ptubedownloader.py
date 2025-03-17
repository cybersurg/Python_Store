from os import link
from pytube import YouTube

SAVE_PATH = "P:/coding/Python_Store/pytube/"

link="https://youtu.be/fNzpcB7ODxQ"

try:
    yt = YouTube(link)
except:
    print("Connection Error")

mp4files = yt.filter('mp4')

yt.set_filename('Ethical Hacking in 12 Hours - Full Course - Learn to Hack!')

d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
    d_video.download(SAVE_PATH)
except:
    print("some error!")
print('Task Completed!')