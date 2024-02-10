import os
from moviepy.editor import VideoFileClip


def split_path_and_filename(file_path):
    """
    Split the file path into directory name and filename.
    Returns a tuple (directory_name, file_name).
    """
    directory_name, file_name = os.path.split(file_path)
    file_name = os.path.splitext(file_name)[0]  # Remove extension from filename
    return directory_name, file_name


def extract_audio(video_path, output_path):
    """
    Extract audio from the video and save it as a WAV file.
    """
    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile(output_path)
