
import random
from Pokemonxd.utilities import config
from Pokemonxd.utilities.config import SUPPORT_GROUP, SUPPORT_CHANNEL
from pyrogram.types import InlineKeyboardButton



def time_to_sec_new(time: str):
    x = time.split(":")

    if len(x) == 2:
        min = int(x[0])
        sec = int(x[1])

        total_sec = (min*60) + sec
    elif len(x) == 3:
        hour = int(x[0])
        min = int(x[1])
        sec = int(x[2])

        total_sec = (hour*60*60) + (min*60) + sec

    return total_sec

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_sec_new(played)
    total_sec = time_to_sec_new(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "═"
    circle = "☉"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐎𝐰𝐧𝐞𝐫シ︎𝐱𝐃 ❱ ✨", url=f"https://t.me/shreya_ghoshal_143"), 
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐂𝐥𝐨𝐬𝐞 ✯", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_sec_new(played)
    total_sec = time_to_sec_new(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "═"
    circle = "☉"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐎𝐰𝐧𝐞𝐫シ︎𝐱𝐃 ❱ ✨", url=f"https://t.me/shreya_ghoshal_143"), 
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐂𝐥𝐨𝐬𝐞 ✯", callback_data="close"
            )
        ],
    ]
    return buttons

## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐎𝐰𝐧𝐞𝐫シ︎𝐱𝐃 ❱ ✨", url=f"https://t.me/shreya_ghoshal_143"), 
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐂𝐥𝐨𝐬𝐞 ✯", callback_data="close"
            )
        ],
    ]
    return buttons
            


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐎𝐰𝐧𝐞𝐫シ︎𝐱𝐃 ❱ ✨", url=f"https://t.me/shreya_ghoshal_143"), 
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐂𝐥𝐨𝐬𝐞 ✯", callback_data="close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="𝐏𝐥𝐚𝐲 𝐕𝐢𝐝𝐞𝐨 📺",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"AdityaPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="𝐏𝐥𝐚𝐲 𝐕𝐢𝐝𝐞𝐨 📺",
                callback_data=f"AdityaPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🖥️ 𝐒𝐭𝐚𝐫𝐭 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 🖥️",
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="𝐏𝐥𝐚𝐲 𝐕𝐢𝐝𝐞𝐨 📺",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏸ 𝐏𝐚𝐮𝐬𝐞", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▶️ 𝐑𝐞𝐬𝐮𝐦𝐞",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏯ 𝐒𝐤𝐢𝐩", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⏹ 𝐒𝐭𝐨𝐩", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀️",
                callback_data=f"Pages Back|0|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 𝐁𝐚𝐜𝐤 🔙",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔇 𝐌𝐮𝐭𝐞", callback_data=f"ADMIN Mute|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🔊 𝐔𝐧𝐦𝐮𝐭𝐞",
                callback_data=f"ADMIN Unmute|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔀 𝐒𝐡𝐮𝐟𝐟𝐥𝐞",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔁 𝐋𝐨𝐨𝐩", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀️",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 𝐁𝐚𝐜𝐤 🔙",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏮ 𝟏𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 𝟏𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ 𝟑𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 𝟑𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀️",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 𝐁𝐚𝐜𝐤 🔙",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons
