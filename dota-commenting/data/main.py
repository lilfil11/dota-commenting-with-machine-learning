from data import Video


if __name__ == '__main__':
    video_filename = f'input.mp4'
    video = Video(video_filename)

    lang, segments = video.transcribe_audio()
