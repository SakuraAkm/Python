from pytube import YouTube, contrib, Playlist
import time
import os

while True:
    video_or_playlist = input(
        "What are you wanting to download? insert 1 or 2:\n1) A single video\n2) A playlist\n"
    )
    mp34 = input("\ndo you wanna download in mp3 or mp4 format?\n")

    if video_or_playlist == "1" or video_or_playlist == "2":
        if mp34 == "mp3" or mp34 == "mp4":
            break

    print("something typed wrong, please retype correctly\n\n\n\n")

destination = input(
    "\nplease add the destination, should be something like C:\\Users\\Your User\\Downloads\n"
)
link = input("\nEnter the Link: ")
print("\nDownload in progress...")

try:
    if video_or_playlist == "1":
        if mp34 == "mp4":
            yt = YouTube(link)
            video = yt.streams.get_highest_resolution()
            video.download(f"{destination}\\Youtube Downloader")

        elif mp34 == "mp3":
            yt = YouTube(link)
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(f"{destination}\\Youtube Downloader")
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + ".mp3"
            os.rename(downloaded_file, new_file)

    elif video_or_playlist == "2":
        yt = contrib.playlist.Playlist(link)
        yt_arr = yt.video_urls

        if mp34 == "mp4":
            for link in yt_arr:
                video = YouTube(link)
                video = video.streams.get_highest_resolution()
                video.download(f"{destination}\\Youtube Downloader\\{yt.title} mp4")

        elif mp34 == "mp3":
            for link in yt_arr:
                video = YouTube(link)
                video = video.streams.get_audio_only()
                downloaded_file = video.download(
                    f"{destination}\\Youtube Downloader\\{yt.title} mp3"
                )
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + ".mp3"
                os.rename(downloaded_file, new_file)

    print("\ndownload completed")
    time.sleep(60)

except:
    print("not a valid link or wrong destination")
    time.sleep(4)
