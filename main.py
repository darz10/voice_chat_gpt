from aiogram import Bot, Dispatcher, executor, types
from services.services import get_voice_from_chat_gpt

from settings import settings


bot = Bot(token=settings.API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_start(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    text_message = "Запишите головое сообщение"
    await message.reply(text_message)


@dp.message_handler(
    content_types=types.ContentType.VOICE
)
async def handler_voice(message: types.Message):
    telegram_voice = await message.voice.get_file()
    downloaded_file = await bot.download_file(telegram_voice.file_path)
    chat_gpt_voice = await get_voice_from_chat_gpt(
        telegram_voice,
        downloaded_file
    )
    await bot.send_voice(message.from_user.id, chat_gpt_voice)


@dp.message_handler(
    content_types=types.ContentType.TEXT
)
async def handler_text(message: types.Message):
    text_message = "Запишите головое сообщение"
    await message.reply(text_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
