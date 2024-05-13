import os
from pytube import YouTube
from bidi.algorithm import get_display
import arabic_reshaper
from pytube import Playlist
import time

# Function to download YouTube video
def download_video(url, download_path):
    try:
        # Create a YouTube object
        video = YouTube(url)
        # Check if the download path exists, if not, create it
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        # Get the highest resolution video stream
        stream = video.streams.get_highest_resolution()

        # Download the video to the desktop
        stream.download(download_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

# Helps to display Arabic text correctly
def arabic_title(title):
    reshaped_text = arabic_reshaper.reshape(title)
    bidi_text = get_display(reshaped_text)
    return bidi_text


def download_playlist_auto(playlist_url, download_path, sleep_interval=2):
    downloaded_videos = set()

    while True:
        try:
            # Create a Playlist object
            playlist = Playlist(playlist_url)

            # Check if the download path exists, if not, create it
            if not os.path.exists(download_path):
                os.makedirs(download_path)

            # Iterate through all videos in the playlist
            for video in playlist.videos:
                # If the video has already been downloaded, skip it
                if video.video_id in downloaded_videos:
                    continue

                # Get the highest quality audio stream
                stream = video.streams.get_audio_only()
                print("downloading new video....")
                # Download the video to the desktop
                stream.download(download_path)

                # Add the video to the set of downloaded videos
                downloaded_videos.add(video.video_id)
                title = arabic_title(video.title)
                # Print the title and number of the video
                print(f"Downloaded video: {title}")

            print("Waiting for new videos...")
        except Exception as e:
            print("Error:", str(e))

        # Sleep for the specified interval
        time.sleep(sleep_interval)


def download_playlist(playlist_url, download_path):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Check if the download path exists, if not, create it
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Iterate through all videos in the playlist
        for i, video in enumerate(playlist.videos, start=1):
            # Get the highest quality audio stream
            stream = video.streams.get_audio_only()

            # Download the video to the desktop
            stream.download(download_path)
            
            title = arabic_title(video.title)
            # Print the title and number of the video
            print(f"Downloaded video {i}: {title} ")

        print("Playlist downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

while True:
    print("1. Download a single video")
    print("2. Download a playlist")
    print("3. Download a playlist automatically")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        url = input("Enter the YouTube video URL: ")
        download_path = input("Enter the download path: ")
        download_video(url, download_path)
    elif choice == "2":
        playlist_url = input("Enter the YouTube playlist URL: ")
        download_path = input("Enter the download path: ")
        download_playlist(playlist_url, download_path)
    elif choice == "3":
        playlist_url = input("Enter the YouTube playlist URL: ")
        download_path = input("Enter the download path: ")
        download_playlist_auto(playlist_url, download_path)
    elif choice == "4":
        break
    else:
        print("Invalid choice! Please try again.")

