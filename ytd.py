#!python

import sys
from pytube import YouTube
import subprocess

# a function to download only audio
def downloaderaudio(url):
    yt = YouTube(url)
    title = yt.title.encode("cp850","replace").decode("cp850")

    # remove special characters from title
    specialCharacters = ['\\','/',':','*','?','\"','<','>','|']
    for f in specialCharacters:
        title = title.replace(f,'_')
    #replace spaces with underscores
    title = title.replace(' ','_')
    
    print("Title: ", title)
    audio = yt.streams.filter(only_audio=True)
    audio.first().download("./", filename=title + ".mp3")

def downloader(url):
        yt = YouTube(url)
        #Title of video
        title = yt.title


        title = title.encode("cp850","replace").decode("cp850")
        print(title)


        # remove special characters from title
        specialCharacters = ['\\','/',':','*','?','\"','<','>','|']
        for f in specialCharacters:
            title = title.replace(f,'_')
        #replace spaces with underscores
        title = title.replace(' ','_')
        
        print(title)
        video = yt.streams.filter(only_video=True)
        audio = yt.streams.filter(only_audio=True)
        print("Downloading...")
        # download video and audio and then merge them together
        video.first().download("./",filename="temp.mp4")
        audio.first().download("./",filename="temp.mp3")
        print("Downloaded")
        # merge video and audio
        args = """ffmpeg -i temp.mp4 -i temp.mp3 -c:v copy -c:a aac -strict experimental temp2.mp4"""
        subprocess.call(args, shell=True)
        # delete temp files
        args = """rm temp.mp4 temp.mp3"""
        subprocess.call(args, shell=True)
        print("Deleted")
        # rename file to title of video
        args = """mv temp2.mp4 {}.mp4""".format(title)
        subprocess.call(args, shell=True)
        print("Renamed")
        print("Done")
        return

def downloaderlow(url):
        yt = YouTube(url)
        print(yt.title.encode("cp850","replace").decode("cp850"))
        ys = yt.streams.get_highest_resolution()
        print("Low Quality")
        print("Downloading...")
        # Download video
        ys.download()
        print("Downloaded")


def main():
    url = ''
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("URL: ",sys.argv[1])
            url = sys.argv[1]
            downloader(url)
        elif len(sys.argv) == 3:
            if sys.argv[1] == 'l':
                print("URL: ",sys.argv[2])
                print("Low Quality")
                url = sys.argv[2]
                downloaderlow(url)
            elif sys.argv[1] == 'a':
                print("URL: ",sys.argv[2])
                print("Audio")
                url = sys.argv[2]
                downloaderaudio(url)
            else:
                print("Invalid Arguments")
                print("Usage: python ytd.py [l] [url]")
    else:
        print("Invalid Arguments")
        print("Usage: python ytd.py [l] [url]")
        url = input('Enter url: ')
        quality = input('Enter quality or a for audio only: ')
        if quality == "" or quality == "h":
            downloader(url)
        elif quality == "l" and url != "":
            print("Low Quality")
            downloaderlow(url)
        elif quality == "l" and url == "":
            print("Invalid Arguments")
            print("Usage: python ytd.py [l] [url]")
        elif quality == "a" and url != "":
            print("Audio")
            downloaderaudio(url)
        else:
            print("Invalid Arguments")
            print("Usage: python ytd.py [l] [url]")
        return

main()