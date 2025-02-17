from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto


class TeleScraper:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('session', api_id, api_hash)

    async def startscrap(self):
        # connected to telegram
        await self.client.start(phone = '+989050967501')
        print('Connected to Telegram')

        # get me name
        me = await self.client.get_me()
        print(f'Username: {me.first_name}')

        async for message in self.client.iter_messages('@Roeinnnn', limit=10):
            if message.media and isinstance(message.media, MessageMediaPhoto):
                path = await message.download_media()
                print(f"Photo saved to {path}")

    def run(self):
        with self.client:
            self.client.loop.run_until_complete(self.startscrap())


if __name__ == "__main__":
    teleScraper = TeleScraper('26624174', '315f3ba819aae882e912f5f34a3a6bac')
    teleScraper.run()