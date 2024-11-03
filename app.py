import streamlit as st
import yt_dlp
import os

# Streamlit Page Configurations
st.set_page_config(page_title="Xtract Audio", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>Xtract Audio</h1>", unsafe_allow_html=True)

# Download Functions
def download_audio_direct_mp3(url):
    ydl_opts = {
        'format': 'bestaudio[ext=mp3]/bestaudio',
        'outtmpl': 'Downloaded_MP3/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': None,
    }

    file_path = ""
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = f"Downloaded_MP3/{info['title']}.mp3"
        st.success("Download completed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return file_path

def download_audio_original_format(url):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'Downloaded_Audio/%(title)s.%(ext)s',
    }

    file_path = ""
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = f"Downloaded_Audio/{info['title']}.{info['ext']}"
        st.success("Download completed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return file_path

# Input and Selection
st.write("Enter the YouTube URL to download audio from:")
url = st.text_input("YouTube URL", value="", label_visibility="collapsed")

download_choice = st.radio(
    "Choose Download Format:",
    ("Direct MP3 Download (No Conversion)", "Original Format (webm/m4a)")
)

# Button to trigger download
file_path = ""
if st.button("Download"):
    if not url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        # Ensure directories exist
        if not os.path.exists("Downloaded_MP3"):
            os.makedirs("Downloaded_MP3")
        if not os.path.exists("Downloaded_Audio"):
            os.makedirs("Downloaded_Audio")

        if download_choice == "Direct MP3 Download (No Conversion)":
            file_path = download_audio_direct_mp3(url)
        else:
            file_path = download_audio_original_format(url)

        # Provide download button if the file path is valid
        if file_path and os.path.exists(file_path):
            with open(file_path, "rb") as file:
                st.download_button(
                    label="Click here to download your audio file",
                    data=file,
                    file_name=os.path.basename(file_path),
                    mime="audio/mpeg" if file_path.endswith(".mp3") else "audio/webm",
                )

# Footer
st.markdown(
    """
    <hr style="margin-top: 2rem;">
    <footer style="text-align: center;">
        <p>&copy; 2024 IMMERSIVE X | Made by Yash Rathore</p>
    </footer>
    """, 
    unsafe_allow_html=True
)
