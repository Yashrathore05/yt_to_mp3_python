import streamlit as st
import yt_dlp
import os

def download_youtube_playlist_as_mp3(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

st.title("YouTube Playlist to MP3 Downloader")
url = st.text_input("Enter YouTube Playlist URL:")
if st.button("Download"):
    if url:
        download_youtube_playlist_as_mp3(url)
        st.success("Download started successfully!")
    else:
        st.error("Please enter a valid URL.")
