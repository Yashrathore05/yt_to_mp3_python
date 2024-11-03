import streamlit as st
import yt_dlp

# Function to download YouTube video as MP3
def download_youtube_playlist_as_mp3(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=True)
            title = info.get('title', 'audio')
            filename = f"{title}.mp3"
            st.success(f"Download successful! Saved as {filename}")
            return filename
    except yt_dlp.utils.DownloadError as e:
        st.error("Download error: Unable to extract audio format from the provided URL.")
        st.error(f"Error details: {e}")

# Streamlit app
st.title("YouTube to MP3 Downloader")

url = st.text_input("Enter the YouTube Playlist/Video URL:")

if st.button("Download as MP3"):
    if url:
        filename = download_youtube_playlist_as_mp3(url)
        if filename:
            with open(filename, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name=filename,
                    mime="audio/mpeg"
                )
    else:
        st.warning("Please enter a valid URL.")
