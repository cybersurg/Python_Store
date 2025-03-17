from pytube import YouTube

#link = "https://youtu.be/k36LmS_3bH0"
link = "https://youtu.be/_nyZhYnCNLA"

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "D:/coding/Python_Store/pytube/", 
filename = "CISSP Exam Cram Full Course (All 8 Domains) - Covers latest exam!")
except:
    print("Some Error!")
print('Awsome Task Completed!')