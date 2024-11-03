import streamlit as st
import yt_dlp
import os

# Set the title of the app
st.title("Xtract Audio")

# Centered input for URL
st.markdown("<h3>Enter the YouTube Playlist URL:</h3>", unsafe_allow_html=True)
playlist_url = st.text_input("")

# Function to download the playlist as MP3
def download_youtube_playlist_as_mp3(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'Downloaded_MP3/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe'  # <-- Update this path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Button to trigger download
if st.button("Download MP3"):
    if playlist_url:
        try:
            download_youtube_playlist_as_mp3(playlist_url)
            st.success("Download completed successfully!")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid playlist URL.")

# Footer
st.markdown("---")
st.markdown(
    """
    <style>
        footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            text-align: center;
            padding: 10px;
            background-color: #f1f1f1;
            color: #555;
        }
    </style>
    <footer>
        &copy; 2024 IMMERSIVE X | Made by Yash Rathore
    </footer>
    """,
    unsafe_allow_html=True
)
