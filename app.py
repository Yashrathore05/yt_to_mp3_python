import streamlit as st
import yt_dlp
import os

# Streamlit Page Configurations
st.set_page_config(page_title="Xtract Audio", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>Xtract Audio</h1>", unsafe_allow_html=True)

# Download Function
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

# Input and Button
st.write("Enter the YouTube URL to download audio from:")
url = st.text_input("YouTube URL", value="", label_visibility="collapsed")

# Button to trigger download
file_path = ""
if st.button("Download"):
    if not url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        # Ensure directory exists
        if not os.path.exists("Downloaded_Audio"):
            os.makedirs("Downloaded_Audio")

        file_path = download_audio_original_format(url)

        # Provide download button if the file path is valid
        if file_path and os.path.exists(file_path):
            with open(file_path, "rb") as file:
                st.download_button(
                    label="Click here to download your audio file",
                    data=file,
                    file_name=os.path.basename(file_path),
                    mime="audio/webm" if file_path.endswith(".webm") else "audio/mpeg",
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
