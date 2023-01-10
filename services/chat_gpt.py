import aiohttp

from settings import settings


class ClientChatGPT:

    async def send_data_chat_gpt(self, data: str):
        async with aiohttp.ClientSession() as session:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {settings.API_KEY_CHAT_GPT}"
            }
            data = {
                "model": "text-davinci-003",
                "prompt": data,
                "temperature": 0.9,
                "max_tokens": 150,
                "top_p": 1,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.6,
            }
            async with session.post(
                settings.URL_CHAT_GPT,
                headers=headers,
                json=data
            ) as resp:
                return await resp.json()
