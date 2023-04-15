from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Pokemonxd import bot
from Pokemonxd.utilities.config import SUPPORT_GROUP

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [   
                InlineKeyboardButton(
                    text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭࿐",
                    url=f"https://t.me/Telugu_Friends_Chatting",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐏𝐫𝐞𝐦𝐚 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥࿐",
                    url=f"https://t.me/vennela_official143",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{bot.username}?start=help",
            ),
        ],
    ]
    return buttons
