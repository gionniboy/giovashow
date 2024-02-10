import os
from moviepy.editor import VideoFileClip
from typing import Tuple
from typing import Optional


def split_path_and_filename(file_path: str) -> Tuple[str, str]:
    """
    Split the file path into directory name and filename.
    Returns a tuple (directory_name, file_name).
    """
    directory_name, file_name = os.path.split(file_path)
    file_name = os.path.splitext(file_name)[0]
    return directory_name, file_name


def extract_audio(video_path: str, output_path: str) -> bool:
    """
    Extract audio from the video and save it as a WAV file if it doesn't already exist.
    """
    if not os.path.exists(output_path):
        with VideoFileClip(video_path) as video:
            audio = video.audio
            audio.write_audiofile(output_path)
            print(f"Audio extracted and saved as '{output_path}'.")
            return True
    else:
        print(f"Audio file '{output_path}' already exists.")
        return False
