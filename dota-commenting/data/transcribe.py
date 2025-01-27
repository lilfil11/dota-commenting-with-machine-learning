import time
import math
import ffmpeg

from faster_whisper import WhisperModel


def extract_audio():
    extracted_audio = f"audio-{input_video_name}.wav"
    stream = ffmpeg.input(input_video)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)

    return extracted_audio

def transcribe(audio):
    model = WhisperModel("small")
    segments, info = model.transcribe(audio)
    print("Transcription language", info.language)
    segments = list(segments)
    for segment in segments:
        # print(segment)
        print("[%.2fs -> %.2fs] %s" %
              (segment.start, segment.end, segment.text))

    return info.language, segments

def run():
    extracted_audio = extract_audio()

    language, segments = transcribe(audio=extracted_audio)


if __name__ == '__main__':
    input_video = "input.mp4"
    input_video_name = input_video.replace(".mp4", "")

    run()

