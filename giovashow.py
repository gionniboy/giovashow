import os
import instagram
import whisperer

from utils import split_path_and_filename, extract_audio


def is_anagram(str1: str, str2: str) -> bool:
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


def main():
    # Replace 'username' with the Instagram username you want to download the last post from
    username = "giovashow"
    # Replace 'your_login' and 'your_password' with your Instagram login credentials
    login, password = instagram.get_instagram_credentials()
    video_path = instagram.download_last_post(username, login, password)

    directory_name, file_name = split_path_and_filename(video_path)
    audio_output_path = os.path.join(directory_name, f"{file_name}.wav")
    extract_audio(video_path, audio_output_path)

    whisperer.extract_transcript(audio_output_path)


if __name__ == "__main__":
    main()
