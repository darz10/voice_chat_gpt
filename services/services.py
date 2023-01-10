from io import BytesIO
from aiogram.types.file import File

from services.chat_gpt import ClientChatGPT
from services.converter import (
    TextConverter,
    convert_voice_to_text
)
from utils import chat_gpt_response_to_text


async def send_text_to_chat_gpt(
    telegram_voice: File,
    downloaded_voice: BytesIO
) -> str:
    text = convert_voice_to_text(telegram_voice, downloaded_voice)
    client_gpt = ClientChatGPT()
    result = await client_gpt.send_data_chat_gpt(text)
    text = chat_gpt_response_to_text(result["choices"])
    return text


async def get_voice_from_chat_gpt(
    telegram_voice: File,
    downloaded_voice: BytesIO
):
    text = await send_text_to_chat_gpt(
        telegram_voice,
        downloaded_voice
    )
    client_gpt = TextConverter()
    chat_gpt_voice = client_gpt.convert(text)
    return chat_gpt_voice
