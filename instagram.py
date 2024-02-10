import os

import instaloader


def get_instagram_credentials():
    """
    Retrieves Instagram login and password from environment variables.
    Returns a tuple (login, password).
    """
    login = os.environ.get("INSTAGRAM_LOGIN")
    password = os.environ.get("INSTAGRAM_PASSWORD")
    if login is None or password is None:
        print(
            "Please set INSTAGRAM_LOGIN and INSTAGRAM_PASSWORD environment variables."
        )
        return None, None
    else:
        return login, password


def download_last_post(username, login, password):
    loader = instaloader.Instaloader()
    loader.login(login, password)

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        # Get the last post
        posts = profile.get_posts()
        post = None
        for p in posts:
            post = p
            break

        if post:
            # Download the post
            loader.download_post(post, target=profile.username)
            print("Post downloaded successfully!")
        else:
            print(f"No posts found for '{username}'.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
