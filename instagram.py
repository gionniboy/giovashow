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
        raise EnvironmentError(
            "Please set INSTAGRAM_LOGIN and INSTAGRAM_PASSWORD environment variables."
        )
    else:
        return login, password


def download_last_post(username, login, password):
    loader = instaloader.Instaloader()
    loader.login(login, password)

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        posts = profile.get_posts()
        last_post = next(posts, None)
        if last_post:
            video_filename = f"{profile.username}/{last_post.date_utc.strftime('%Y-%m-%d_%H-%M-%S_UTC')}.mp4"
            video_path = os.path.join(os.getcwd(), video_filename)
            if os.path.exists(video_path):
                print(f"Post already downloaded: {os.path.relpath(video_path)}")
                return os.path.relpath(video_path)
            else:
                loader.download_post(last_post, target=profile.username)
                print("Post downloaded successfully!")
                print(f"Video saved as: {os.path.relpath(video_path)}")
                return os.path.relpath(video_path)
        else:
            print(f"No posts found for '{username}'.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")
    except Exception as err:
        print(f"An error occurred: {str(err)}")
