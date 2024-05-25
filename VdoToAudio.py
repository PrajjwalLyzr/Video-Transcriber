import subprocess
import streamlit
import imageio_ffmpeg as ffmpeg
from lyzr import VoiceBot


def convert_vdo_to_mp3(input_file, output_file):
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()
    ffmpeg_cmd = [
        ffmpeg_path,
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
        streamlit.info('Successfully Converted !!!')
    except subprocess.CalledProcessError as e:
        streamlit.error('Conversion Failed !!!')



def audio_transcript(audio_file, API_KEY):
    vb = VoiceBot(api_key=API_KEY)
    transcript = vb.transcribe(audio_file)
    return transcript

