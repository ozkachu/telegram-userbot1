import os
from telethon import TelegramClient, events

# --- Ortam Değişkenlerini Oku ---
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
phone_number = os.environ["PHONE_NUMBER"]
target_username = os.environ["TARGET_USERNAME"]

# --- Telegram Client Başlat ---
client = TelegramClient('userbot_session', api_id, api_hash)

@client.on(events.NewMessage)
async def catch_target_user(event):
    sender = await event.get_sender()
    if sender and sender.username == target_username:
        message = f"[{sender.first_name}] {event.text}"
        await client.send_message("me", message)  # "me" Saved Messages

client.start(phone_number)
print("Userbot çalışıyor... Hedef kullanıcıdan mesaj bekleniyor.")
client.run_until_disconnected()
