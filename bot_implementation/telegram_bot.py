import aiohttp
import asyncio

class TelegramBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.token}/"

    async def send_message(self, message):
        url = f"{self.api_url}sendMessage"
        payload = {
            'chat_id': self.chat_id,
            'text': message
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload) as response:
                    response.raise_for_status()
                    result = await response.json()
                    if not result.get('ok'):
                        print(f"Failed to send message: {result}")
            except aiohttp.ClientError as e:
                print(f"Failed to send message: {e}")

