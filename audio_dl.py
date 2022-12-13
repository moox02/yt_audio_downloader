import streamlit as st
from utils import *

def main():
    # Streamlit config
    st.set_page_config(
        page_title="YouTube Audio Downloader",
        layout="centered",
    )

    # Introduction
    st.image("https://cdn-icons-png.flaticon.com/512/1384/1384060.png", width=80)
    st.markdown(
        """
        ## YouTube Audio Downloader
        *by Nasrul Hakim*
        """
    )
    st.markdown(
        """
        This tool allows you to easily convert and download audios from youtube for free and in the best available quality. 
        """
    )

    # Youtube link input https://www.youtube.com/watch?v=0QhkzVIvcLI
    yt_url = st.text_input('Enter the YouTube URL:')

    if yt_url:
        # Check if the input url is a valid YouTube url
        valid_url = validate_url(yt_url)

        if valid_url:
            if get_video_duration_from_youtube_url(yt_url) <= MAX_VIDEO_LENGTH: 
                st.markdown("---")
                st.write(get_video_title_from_youtube_url(yt_url))
                st.video(yt_url)
                audio_path = get_audio_from_youtube_url(yt_url)

                audio_file = open(audio_path, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')

                with open(audio_path,'rb') as file:
                    download_audio = st.download_button(
						label = 'Download Audio',
						data = file,
						file_name = os.path.basename(audio_path)
					)

                    if download_audio:
                        st.success('Audio file downloaded successfully')
            
            else:
                st.warning("Sorry, the video has to be shorter than or equal to eight minutes.")   
        else:
            st.error("Invalid YouTube URL")


if __name__ == "__main__":
    main()