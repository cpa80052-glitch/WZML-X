
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import FORCE_SUB_CHANNELS

async def check_force_sub(client, message):
    user_id = message.from_user.id

    for channel in FORCE_SUB_CHANNELS:
        try:
            member = await client.get_chat_member(channel, user_id)
            if member.status in ["left", "kicked"]:
                raise Exception
        except:
            try:
                chat = await client.get_chat(channel)
                username = chat.username
                url = f"https://t.me/{username}" if username else ""
            except:
                url = ""

            buttons = [[
                InlineKeyboardButton("Join Channel", url=url)
            ]]

            await message.reply(
                "❌ You must join all required channels to use this bot!",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return False

    return True
