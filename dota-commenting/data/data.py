import ffmpeg

from faster_whisper import WhisperModel
from time import time


class Video:
    def __init__(self, filename):
        self.video_filename = filename
        self.audio_filename = f'audio-{filename.replace(".mp4", ".wav")}'

    def extract_audio(self):
        stream = ffmpeg.input(self.video_filename)
        stream = ffmpeg.output(stream, self.audio_filename)
        ffmpeg.run(stream, overwrite_output=True)

    def transcribe_audio(self):
        model = WhisperModel("small")
        ts = time()
        print(f'Transcribing starts...')
        segments, info = model.transcribe(self.audio_filename)
        te = time()
        print(f'Audio transcribed! Transcription language: {info.language}')
        segments = list(segments)
        for segment in segments:
            print("[%.2fs -> %.2fs] %s" %
                  (segment.start, segment.end, segment.text))

        print(f'time for transcribing is {te - ts:.2f} sec')

        return info.language, segments
