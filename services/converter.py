from io import BytesIO, BufferedRandom
from abc import ABC, abstractmethod

from aiogram.types.file import File
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment


class AbstractConverter(ABC):
    @abstractmethod
    def convert():
        raise NotImplementedError()


class TextConverter(AbstractConverter):
    def convert(self, text: str) -> BytesIO:
        """
        Convert text to audio file
        """
        bytes_file = BytesIO()
        audio = gTTS(text=text, lang="ru")
        audio.write_to_fp(bytes_file)
        bytes_file.seek(0)
        return bytes_file


class VoiceConverter(AbstractConverter):
    def convert(self, voice: str) -> str:
        """
        Convert audio file to text
        """
        recognizer = sr.Recognizer()
        with sr.AudioFile(voice) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language="ru")
            return text


def convert_oga_to_wav(filename: str, file: BytesIO) -> BufferedRandom:
    """
    Change format file from .oga to .wav
    """
    path = filename.split("/")
    name = path[-1].split(".oga")
    converted_path = name[0] + '.wav'
    segment = AudioSegment.from_ogg(file)
    wav_file = segment.export(converted_path, format="wav")
    return wav_file


def convert_voice_to_text(
    telegram_voice: File,
    downloaded_voice: BytesIO
) -> str:
    buffered_file = convert_oga_to_wav(
        telegram_voice.file_path,
        downloaded_voice
    )
    service = VoiceConverter()
    text = service.convert(buffered_file)
    return text
