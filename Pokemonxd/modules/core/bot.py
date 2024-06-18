# Aditya Halder

import sys
from pyrogram import Client
from Pokemonxd.utilities import config
from Pokemonxd.console import LOGGER


class Bot(Client):
    def __init__(self):
        LOGGER(__name__).info("🥀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 💞...")
        super().__init__(
            "Pokemonxd",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
        self.username = get_me.username
        self.id = get_me.id
        
        log_message = (
            f"**━━━━━━━━━━━━━━━━━━━**\n"
            f"**✅ 𝐁𝐨𝐭 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n"
            f"**━━━━━━━━━━━━━━━━━━━**\n"
            f"**🥀 𝐍𝐚𝐦𝐞 ›** {self.name}\n"
            f"**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.username}\n"
            f"**🌷 𝐈𝐃✩ : ›** `{self.id}`\n"
            f"**━━━━━━━━━━━━━━━━━━━**\n"
            f"**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐏𝐨𝐤𝐞𝐦𝐨𝐧 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/Tc_pokemon).**\n"
            f"**━━━━━━━━━━━━━━━━━━━**"
        )

        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                log_message,
                disable_web_page_preview=True
            )
        except Exception as e:
            LOGGER(__name__).error(
                f"🥀 𝐏𝐥𝐞𝐚𝐬𝐞, 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐀𝐝𝐝 𝐁𝐨𝐭 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 🌷... Error: {e}"
            )
            await self.stop()
            sys.exit()

        try:
            member = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if member.status != "administrator":
                LOGGER(__name__).error(
                    "🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐁𝐨𝐭 𝐚𝐬 𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 𝐢𝐧 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🌷..."
                )
                await self.stop()
                sys.exit()
        except Exception as e:
            LOGGER(__name__).error(
                f"Error checking bot admin status: {e}"
            )
            await self.stop()
            sys.exit()

        LOGGER(__name__).info(
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"✅ 𝐁𝐨𝐭 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🥀 𝐍𝐚𝐦𝐞 » {self.name}\n"
            f"🌸 𝐋𝐢𝐧𝐤 : » @{self.username}\n"
            f"🌷 𝐈𝐃✩ : » `{self.id}`\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : 𝐏𝐨𝐤𝐞𝐦𝐨𝐧 𝐒𝐞𝐫𝐯𝐞𝐫.\n"
            f"━━━━━━━━━━━━━━━━━━━"
        )
        
