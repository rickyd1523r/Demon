# Written By [MaskedVirus | swatv3nub] for William and Ryūga
# Kang With Proper Credits

from pyrogram import filters

from Shikimori import app
from Shikimori.utils.permissions import adminsOnly
from Shikimori.utils.errors import capture_err
from Shikimori.ex_plugins.dbfunctions import (
    antiservice_off,
    antiservice_on,
    is_antiservice_on,
)

__mod_name__ = "AntiService"
__help__ = """
Plugin to delete service messages in a chat!

/antiservice [enable|disable]
"""


@app.on_message(
    filters.command("antiservice")
)
@capture_err
@adminsOnly("can_change_info")
async def anti_service(_, message):
    if len(message.command) != 2:
        return await message.reply_text(
            "Usage: /antiservice [enable | disable]"
        )
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "enable":
        await antiservice_on(chat_id)
        await message.reply_text(
            "Enabled AntiService System. I will Delete Service Messages from Now on."
        )
    elif status == "disable":
        await antiservice_off(chat_id)
        await message.reply_text(
            "Disabled AntiService System. I won't Be Deleting Service Message from Now on."
        )
    else:
        await message.reply_text(
            "Unknown Suffix, Use /antiservice [enable|disable]"
        )


@app.on_message(filters.service, group=11)
async def delete_service(_, message):
    chat_id = message.chat.id
    try:
        if await is_antiservice_on(chat_id):
            return await message.delete()
    except Exception:
        pass