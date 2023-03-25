import asyncio
import speedtest
from pyrogram import filters
from Pokemonxd.utilities.strings import get_command
from Pokemonxd import bot
from Pokemonxd.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐩𝐞𝐞𝐝𝐓𝐞𝐬𝐭")
        test.download()
        m = m.edit("𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐔𝐩𝐥𝐨𝐚𝐝 𝐒𝐩𝐞𝐞𝐝𝐓𝐞𝐬𝐭")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐒𝐩𝐞𝐞𝐝𝐓𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐬")
    except Exception as e:
        return m.edit(e)
    return result


@bot.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐒𝐩𝐞𝐞𝐝 𝐭𝐞𝐬𝐭")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Speedtest Results**
    
<u>**Client:**</u>
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
  
<u>**Server:**</u>
**__Name:__** {result['server']['name']}
**__Country:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latency:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    msg = await bot.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
