import streamlit as st
import os
from utils import utils
from PIL import Image
from VdoToAudio import convert_vdo_to_mp3, audio_transcript


# page config
st.set_page_config(
        page_title="Lyzr - Video Transciber",
        layout="centered",   
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

# style the app
st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)


# Streamlit app interface
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)
st.title('Video Transcriber')
st.markdown('An app leveraging Lyzr.ai to automatically transcribe any video, providing accurate and fast text transcriptions for enhanced accessibility and content analysis.')

# Setting up the sidebar for input
st.sidebar.title("Video Transcriber")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type='password')
submit_api_key = st.sidebar.button("Submit API Key")


videoDir = 'VideoDir'
audioDir = 'AudioDir'

os.makedirs(videoDir, exist_ok=True)
os.makedirs(audioDir, exist_ok=True)

video_formats = [
    ".mp4",  # MPEG-4 Part 14
    ".avi",  # Audio Video Interleave
    ".mov",  # QuickTime Movie
    ".mkv",  # Matroska
    ".flv",  # Flash Video
    ".wmv",  # Windows Media Video
    ".webm", # WebM
    ".mpg",  # MPEG-1 or MPEG-2
    ".mpeg", # MPEG-1 or MPEG-2
    ".m4v",  # MPEG-4 Part 14 (iTunes variant)
    ".3gp",  # 3GPP Multimedia
    ".3g2",  # 3GPP2 Multimedia
    ".f4v",  # Flash MP4 Video
    ".rm",   # RealMedia
    ".vob",  # DVD Video Object
    ".ogv",  # Ogg Video
    ".mts",  # MPEG Transport Stream
    ".m2ts", # MPEG-2 Transport Stream
    ".divx", # DivX Video
    ".mxf",  # Material Exchange Format
    ".m2v",  # MPEG-2 Video
    ".qt",   # QuickTime Movie
    ".asf"   # Advanced Systems Format
]


if api_key != "":
    if submit_api_key:
        utils.save_api_key(api_key)
        st.sidebar.success("API Key saved!")


        with open('api_key.txt', 'r') as file:
            api_key = file.read()
            api_key = api_key.replace(" ","")



    video_file = st.file_uploader(label='Upload any video file', type=video_formats)

    if video_file is not None:
        utils.save_uploaded_file(video_file, directory_name=videoDir)
        file_name = utils.get_files_in_directory(directory=videoDir)
        video_file_name = file_name[0]
        audio_file_name = './AudioDir/audio.mp3'
        convert_vdo_to_mp3(input_file=video_file_name, output_file=audio_file_name)
        if st.button('Get Transcript'):
            audio_file_path = utils.get_files_in_directory(directory=audioDir)
            transcript = audio_transcript(audio_file_path[0], API_KEY=api_key)
            st.markdown('---')
            st.text_area(label='Transcription', value=transcript, height=500)

    else:
        utils.remove_existing_files(videoDir)
        utils.remove_existing_files(audioDir)

else:
    st.warning('Please Provide your OpenAI API Key')



