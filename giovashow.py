import sys

import instagram


def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


def main():
    # Replace 'username' with the Instagram username you want to download the last post from
    username = "giovashow"
    # Replace 'your_login' and 'your_password' with your Instagram login credentials
    login, password = instagram.get_instagram_credentials()
    instagram.download_last_post(username, login, password)


if __name__ == "__main__":
    main()
