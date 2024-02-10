import whisper


def extract_transcript(audio_path):
    """
    Extract transcript from the audio using Whisper.
    Returns the transcript text.
    """
    model = whisper.load_model("large")
    print("Transcribing audio...")
    transcript = model.transcribe(audio_path, language="it")

    print("Audio transcript:")
    print(transcript)
    print(transcript["text"])
    return transcript["text"]
