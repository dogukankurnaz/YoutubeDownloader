import pytube
from pytube import YouTube

while True:
    url = input("Video Linki: ")

    print("indiriliyor....")
    print("Authot: " + pytube.YouTube(url).author)

    pytube.YouTube(url).streams.get_highest_resolution().download()

    print("Video indirildi..")