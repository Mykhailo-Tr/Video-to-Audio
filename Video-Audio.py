import logging

logging.basicConfig(level=logging.INFO)


def get_data_from_user() -> dict:
    video_path = input("Path to Video (my_video.mp4): ")
    file_type = video_path[-4:]
    while file_type != '.mp4':
        print("[-] File type must be .mp4")
        video_path = input("Path to Video (my_video.mp4): ")
        file_type = video_path[-4:]

    print(f'[+] Video - {video_path}')
    audiofile_name = input("Audio file name (my_audio): ")
    print(f'[+] Audio - {audiofile_name}\n')

    return {"video": video_path, "audio": audiofile_name}


def make_audio(data: dict) -> None:
    video_path = data.get("video")
    audio_name = data.get("audio")

    video = moviepy.editor.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(f'{audio_name}.mp3')


def main():
    print("------------Video to Audio------------\n")

    try:
        data = get_data_from_user()
        make_audio(data=data)
    except OSError as error:
        print(f'[-] {error}')

    print("\n-----------------Bye-----------------")


if __name__ == '__main__':
    try:
        import moviepy.editor
        main()
    except ModuleNotFoundError as er:
        print(f'[-] {er}')
        print("Try install 'moviepy': pip install moviepy")
