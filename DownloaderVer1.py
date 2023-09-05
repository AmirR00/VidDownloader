from pytube import YouTube
from pytube.exceptions import RegexMatchError
try:
    link = input("Enter you link: ")
    yt = YouTube(link)
    data = yt.streams.get_lowest_resolution()
    data.download(output_path=input("Name the file: "))
except RegexMatchError:
    print("Try using different URL.")