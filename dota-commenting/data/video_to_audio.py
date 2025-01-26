import os
import sys
from moviepy import VideoFileClip


def convert_video_to_audio_moviepy(video_file, output_ext="wav"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")


if __name__ == "__main__":
    vf = f'../../data/2350276298_dota2_paragon_ru.mp4'
    convert_video_to_audio_moviepy(vf)
