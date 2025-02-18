from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto
import os
import json


class TeleScraper:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('session', api_id, api_hash)

    async def startscrap(self, output_folder='downloaded_photos'):
        # connected to telegram
        await self.client.start(phone='+989050967501')
        print('Connected to Telegram')

        # get user info
        me = await self.client.get_me()
        print(f'Username: {me.first_name}')

        # create folder
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # get all image
        self.total_photos = 0
        async for message in self.client.iter_messages('https://t.me/javabeazmayesh'):
            if message.media and isinstance(message.media, MessageMediaPhoto):
                # info sender
                sender = message.sender
                sender_info = {
                    'id': sender.id if sender else None,
                    'username': sender.username if sender else None,
                    'first_name': sender.first_name if sender else None,
                    'last_name': sender.last_name if sender else None,
                }

                # create folder for image
                photo_folder = os.path.join(output_folder, f"photo_{message.id}")
                if not os.path.exists(photo_folder):
                    os.makedirs(photo_folder)

                try:
                    # download image
                    photo_path = os.path.join(photo_folder, f"photo_{message.id}.jpg")
                    await message.download_media(file=photo_path)
                    print(f"photo saved to {photo_path}")

                    # save sender info in json
                    info_file_path = os.path.join(photo_folder, "sender_info.json")
                    with open(info_file_path, 'w', encoding='utf-8') as f:
                        json.dump(sender_info, f, ensure_ascii=False, indent=4)
                    print(f"sender info saved to {info_file_path}")

                    # download profile
                    if sender and sender.photo:
                        profile_photo_path = os.path.join(photo_folder, "profile_photo.jpg")
                        await self.client.download_profile_photo(sender, file=profile_photo_path)
                        print(f"profile photo saved to {profile_photo_path}")

                    # get reply
                    replies = []
                    async for reply in self.client.iter_messages('https://t.me/javabeazmayesh', reply_to=message.id):
                        if reply.text:  
                            cleaned_text = reply.text.strip().replace('\n', ' ').replace('\t', ' ')
                            replies.append({
                                'id': reply.id,
                                'text': cleaned_text,
                                'sender_id': reply.sender_id if reply.sender else None,
                                'date': reply.date.isoformat() if reply.date else None,
                            })

                    # save reply in json file
                    if replies:
                        replies_file_path = os.path.join(photo_folder, "replies.json")
                        with open(replies_file_path, 'w', encoding='utf-8') as f:
                            json.dump(replies, f, ensure_ascii=False, indent=4)
                        print(f"replies saved to {replies_file_path}")
                    else:
                        print(f"no replies found for message {message.id}")

                    self.total_photos += 1

                except Exception as e:
                    print(f"failed to process message {message.id}: {e}")

        print(f"download completed total photos downloaded: {self.total_photos}")

    def run(self):
        with self.client:
            self.client.loop.run_until_complete(self.startscrap())


if __name__ == "__main__":
    teleScraper = TeleScraper('26624174', '315f3ba819aae882e912f5f34a3a6bac')
    teleScraper.run()