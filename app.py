import streamlit as st
import yt_dlp
import os

# Set the title of the app
st.title("Xtract Audio")

# Sidebar for URL input
st.sidebar.header("Download Settings")
playlist_url = st.sidebar.text_input("Enter the YouTube Playlist URL")

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
        'ffmpeg_location': 'C:/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe'  # Set path to FFmpeg
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
