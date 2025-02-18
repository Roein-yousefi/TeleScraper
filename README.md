# Telegram Photo Scraper

This project is a Python script that uses the `Telethon` library to download photos and related information from a Telegram channel. The script not only downloads photos but also saves the sender's information and admin replies (comments) in an organized manner.

## Features

- Download photos from a Telegram channel.
- Save sender information (ID, username, first name, last name).
- Download the sender's profile photo (if available).
- Save admin replies (comments) in a clean format without extra characters.
- Organize files into separate folders for each photo.

## Prerequisites

- Python 3.6 or higher
- `Telethon` library

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Roein-yousefi/TeleScraper.git

2. **Install Required Libraries:**:
   ```bash
   pip install telethon

   
## API Setup

- Go to my.telegram.org and create a new application.
- Obtain your API_ID and API_HASH.


## Files and Folders:

- photo_{message.id}.jpg:  The downloaded photo.
   
- sender_info.json:  Sender information (ID, username, first name, last name).
   
- profile_photo.jpg:  Senders profile photo (if available).
   
- replies.json:  Admin replies (comments) in a clean format (if available).



1. **Example Output sender_info.json:**
   ```
    {
    "id": 123456789,
    "username": "example_user",
    "first_name": "John",
    "last_name": "Doe"
}

2. **Example Output replies.json:**
   ```
   [
    {
        "id": 67890,
        "text": "This test indicates anemia. Please consult your doctor.",
        "sender_id": 987654321,
        "date": "2023-10-01T12:34:56"
    }
   ]

## Important Notes

- Ensure you have access to the target Telegram channel.
- If the channel is private, you must be a member.
- For replies to be saved, admins must have replied to the photos.

## Developer

- Roein