import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip


def extract_audio_transcript(video_path):
    recognizer = sr.Recognizer()

    # Extract directory name and filename from video_path
    directory_name, file_name = os.path.split(video_path)
    file_name = os.path.splitext(file_name)[0]  # Remove extension from filename

    # Construct output audio file path
    audio_output_path = os.path.join(directory_name, f"{file_name}.wav")

    # Extract audio from video and save as WAV file
    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile(audio_output_path)

    # Recognize speech from the extracted audio
    with sr.AudioFile(audio_output_path) as source:
        audio = recognizer.record(source)

        try:
            transcript = recognizer.recognize_google(audio, language="it-IT")
            print("Audio transcript:")
            print(transcript)
            return transcript
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

    # os.remove(audio_output_path)
