import os
from pytube import YouTube
from bidi.algorithm import get_display
import arabic_reshaper
from pytube import Playlist

# Function to download YouTube video
def download_video(url):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the highest resolution video stream
        stream = video.streams.get_highest_resolution()

        # Set the download path to the desktop
        download_path = os.path.join(os.path.expanduser("~"), "Desktop")

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

playlist_url = input("Enter the YouTube playlist URL: ")
download_playlist(playlist_url, os.path.join(os.path.expanduser("~"), "Desktop"))

