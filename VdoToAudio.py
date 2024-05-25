import subprocess
import streamlit
from lyzr import VoiceBot


def convert_vdo_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '192k',
        '-ar', '44100',
        '-y',
        output_file

    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        streamlit.info('Successfully Conveted !!!')
    except subprocess.CalledProcessError as e:
        streamlit.error('Converstion Failed !!!')



def audio_transcript(audio_file, API_KEY):
    vb = VoiceBot(api_key=API_KEY)
    transcript = vb.transcribe(audio_file)
    return transcript

