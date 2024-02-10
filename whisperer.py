import os
import whisper
from moviepy.editor import VideoFileClip


def extract_audio_transcript(video_path):
    # Extract directory name and filename from video_path
    directory_name, file_name = os.path.split(video_path)
    file_name = os.path.splitext(file_name)[0]  # Remove extension from filename

    # Construct output audio file path
    audio_output_path = os.path.join(directory_name, f"{file_name}.wav")

    # Extract audio from video and save as WAV file
    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile(audio_output_path)

    model = whisper.load_model("tiny")
    # audio = whisper.load_audio(audio_output_path)

    transcript = model.transcribe(audio_output_path)

    # Recognize speech from the extracted audio using Whisper
    # transcript = whisper.transcribe(video_path, language="it-IT")

    print("Audio transcript:")
    print(transcript)
    return transcript["text"]
