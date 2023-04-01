# Powered By @Pokemonxd

from typing import Union
from pyrogram.types import InlineKeyboardButton

from Pokemonxd import bot
from Pokemonxd.utilities.config import SUPPORT_CHANNEL, SUPPORT_GROUP


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ✨",
                url=f"https://t.me/Telugu_Friends_Chatting",
            )
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬",
                url=f"https://t.me/premavennela_143",
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬",
                url=f"https://t.me/Telugu_Friends_Chatting",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"
            )
        ]
    ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝗢𝘄𝗻𝗲𝗿𝐱𝗗",
                url=f"https://t.me/shreya_ghoshal_143"),
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ✨",
                callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬",
                url=f"https://t.me/Telugu_Friends_Chatting")
        ],
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
                url=f"https://t.me/{bot.username}?startgroup=true"
            )
        ]
    ]
    return buttons

def private_panelx(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰ 𝐀𝐝𝐝 𝐌𝐞 𝐁𝐚𝐛𝐞 ❱",
                url=f"https://t.me/{bot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="🥀❰ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ❱",
                callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="💞 𝗢𝘄𝗻𝗲𝗿𝐱𝐃 💞",
                url=f"https://t.me/shreya_ghoshal_143",   
                
            )
        ]
    ]
    return buttons
