import os
import whisper

from utils import split_path_and_filename, extract_audio


def extract_transcript(audio_path):
    """
    Extract transcript from the audio using Whisper.
    Returns the transcript text.
    """
    model = whisper.load_model("large")
    transcript = model.transcribe(audio_path, language="it")

    print("Audio transcript:")
    print(transcript)
    print(transcript["text"])
    return transcript["text"]


def extract_audio_transcript(video_path):
    """
    Extract audio transcript from the video.
    Returns the transcript text.
    """
    directory_name, file_name = split_path_and_filename(video_path)
    audio_output_path = os.path.join(directory_name, f"{file_name}.wav")
    extract_audio(video_path, audio_output_path)
    transcript_text = extract_transcript(audio_output_path)

    print("Audio transcript:")
    print(transcript_text)

    return transcript_text
