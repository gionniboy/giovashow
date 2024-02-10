import speech_recognition as sr


def extract_audio_transcript(video_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(video_path) as source:
        audio = recognizer.record(source)

        # Use Google Web Speech API to recognize speech
        try:
            transcript = recognizer.recognize_google(audio)
            print("Audio transcript:")
            print(transcript)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
