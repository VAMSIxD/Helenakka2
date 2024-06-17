# Aditya Halder

import sys
from pyrogram import Client
from Pokemonxd.utilities import config
from Pokemonxd.console import LOGGER

assistants = []
assistantids = []

class App(Client):
    def __init__(self):
        # Initialize each Client with the session name as the first argument
        self.one = Client(
            str(config.STRING1),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.two = Client(
            str(config.STRING2),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.three = Client(
            str(config.STRING3),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.four = Client(
            str(config.STRING4),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.five = Client(
            str(config.STRING5),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )

    async def start_all(self):
        LOGGER(__name__).info(f"🥀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐂𝐥𝐢𝐞𝐧𝐭𝐬 🌷...")
        await self._start_client(self.one, config.STRING1, 1)
        await self._start_client(self.two, config.STRING2, 2)
        await self._start_client(self.three, config.STRING3, 3)
        await self._start_client(self.four, config.STRING4, 4)
        await self._start_client(self.five, config.STRING5, 5)

    async def _start_client(self, client, string, index):
        if string:
            await client.start()
            get_me = await client.get_me()
            client.username = get_me.username
            client.id = get_me.id
            assistantids.append(get_me.id)
            client.name = get_me.first_name + (" " + get_me.last_name if get_me.last_name else "")
            try:
                await client.join_chat("tgshadow_fighters")
                await client.join_chat("Tc_pokemon")
            except:
                pass
            assistants.append(index)
            try:
                await client.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n"
                    f"**✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 {index} 𝐇𝐚𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n"
                    f"**━━━━━━━━━━━━━━━━━━━**\n"
                    f"**🥀 𝐍𝐚𝐦𝐞 ›** {client.name}\n"
                    f"**🌸 𝐋𝐢𝐧𝐤 : ›** @{client.username}\n"
                    f"**🌷 𝐈𝐃✩ : ›** `{client.id}`\n"
                    f"**━━━━━━━━━━━━━━━━━━━**\n"
                    f"**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐏𝐨𝐤𝐞𝐦𝐨𝐧 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/Tc_pokemon).**\n"
                    f"**━━━━━━━━━━━━━━━━━━━**",
                    disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🥀𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 {index} 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬\n𝐋𝐨𝐠'𝐬 𝐆𝐫𝐨𝐮𝐩 ✨ ...\n\n"
                    f"🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐚𝐧𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬\n𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🥀 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 {index} 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🌿 𝐀𝐬 {client.name} ✨..."
            )

# Initialize and start the App
app = App()
app.run(app.start_all())
