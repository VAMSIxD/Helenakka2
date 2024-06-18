from Pokemonxd import bot
from Pokemonxd.modules.database import is_on_off
from Pokemonxd.utilities.config import LOG, LOG_GROUP_ID


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        chatusername = f"@{message.chat.username}" if message.chat.username else "Private Chat"
        user_name = f"@{message.from_user.username}" if message.from_user.username else f"{message.from_user.mention}"
        
        logger_text = f"""
**━━━━━━━━━━━━━━━━━━━**
**🤖 𝐏𝐨𝐤𝐞𝐦𝐨𝐧 𝐒𝐞𝐫𝐯𝐞𝐫 : 𝐒𝐦𝐚𝐫𝐭 𝐋𝐨𝐠𝐬.**
**━━━━━━━━━━━━━━━━━━━**
**👾 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 :**
**🥀 𝐍𝐚𝐦𝐞 ›** {message.from_user.first_name}
**🌸 𝐋𝐢𝐧𝐤 : ›** {user_name}
**🌷 𝐈𝐃✩ : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━━━━━**
**💬 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐭 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 :**
**☘️ 𝐍𝐚𝐦𝐞 ›** {message.chat.title}
**🌿 𝐋𝐢𝐧𝐤 : ›** {chatusername}
**🌱 𝐈𝐃✩ : ›** `{message.chat.id}`
**━━━━━━━━━━━━━━━━━━━**
**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐏𝐨𝐤𝐞𝐦𝐨𝐧 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/Tc_pokemon).**
**━━━━━━━━━━━━━━━━━━━**"""

        if message.chat.id != LOG_GROUP_ID:
            try:
                await bot.send_message(
                    LOG_GROUP_ID,
                    logger_text,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                # Handle logging error if needed
                print(f"Error sending log message: {e}")
        return
        
