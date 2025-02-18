from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto
import json

class TeleScraper:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('session', api_id, api_hash)

    async def startscrap(self , output_folder = 'downloaded_photos'):
        # connected to telegram
        await self.client.start(phone = '+989050967501')
        print('Connected to Telegram')

        # get me name
        me = await self.client.get_me()
        print(f'Username: {me.first_name}')
        #get photo
        self.total_photos = 0
        async for message in self.client.iter_messages('@Roeinnnn'):
            if message.media and isinstance(message.media, MessageMediaPhoto ):
                #sender masseges
                sender = message.sender
                sender_info = {
                    'id': sender.id if sender else None,
                    'username': sender.username if sender else None,
                    'first_name': sender.first_name if sender else None,
                    'last_name': sender.last_name if sender else None,
                }

                file_name = f"{output_folder}/photo_{message.id}.jpg"
                path = await message.download_media(file=file_name)
                print(f"Photo saved to {path}")

                #save sender id in json file
                info_file_name = f"{output_folder}/photo_{message.id}_info.json"
                with open(info_file_name, 'w', encoding='utf-8') as f:
                    json.dump(sender_info, f, ensure_ascii=False, indent=4)
                print(f"Sender info saved to {info_file_name}")

                #if sender profile is true
                if sender and sender.photo:
                    profile_photo_path = f"{output_folder}/profile_photo_{sender.id}.jpg"
                    await self.client.download_profile_photo(sender, file=profile_photo_path)
                    print(f"Profile photo saved to {profile_photo_path}")
                self.total_photos += 1

    def run(self):
        with self.client:
            self.client.loop.run_until_complete(self.startscrap())


if __name__ == "__main__":
    teleScraper = TeleScraper('26624174', '315f3ba819aae882e912f5f34a3a6bac')
    teleScraper.run()