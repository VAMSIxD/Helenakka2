import random

from Pokemonxd import app
from Pokemonxd.modules.core.adb import mongodb

db = mongodb.assistants

assistantdict = {}


async def get_client(assistant: int):
    if int(assistant) == 1:
        return app.one
    elif int(assistant) == 2:
        return app.two
    elif int(assistant) == 3:
        return app.three
    elif int(assistant) == 4:
        return app.four
    elif int(assistant) == 5:
        return app.five


async def set_assistant(chat_id):
    from Pokemonxd.modules.core.app import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    app = await get_client(ran_assistant)
    return app


async def get_assistant(chat_id: int) -> str:
    from Pokemonxd.modules.core.app import assistants

    assistant = assistantdict.get(chat_id)
    if not assistant:
        dbassistant = await db.find_one({"chat_id": chat_id})
        if not dbassistant:
            app = await set_assistant(chat_id)
            return app
        else:
            got_assis = dbassistant["assistant"]
            if got_assis in assistants:
                assistantdict[chat_id] = got_assis
                app = await get_client(got_assis)
                return app
            else:
                app = await set_assistant(chat_id)
                return app
    else:
        if assistant in assistants:
            app = await get_client(assistant)
            return app
        else:
            app = await set_assistant(chat_id)
            return app


async def set_calls_assistant(chat_id):
    from Pokemonxd.modules.core.app import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    return ran_assistant


async def group_assistant(self, chat_id: int) -> int:
    from Pokemonxd.modules.core.app import assistants

    assistant = assistantdict.get(chat_id)
    if not assistant:
        dbassistant = await db.find_one({"chat_id": chat_id})
        if not dbassistant:
            assis = await set_calls_assistant(chat_id)
        else:
            assis = dbassistant["assistant"]
            if assis in assistants:
                assistantdict[chat_id] = assis
                assis = assis
            else:
                assis = await set_calls_assistant(chat_id)
    else:
        if assistant in assistants:
            assis = assistant
        else:
            assis = await set_calls_assistant(chat_id)
    if int(assis) == 1:
        return self.one
    elif int(assis) == 2:
        return self.two
    elif int(assis) == 3:
        return self.three
    elif int(assis) == 4:
        return self.four
    elif int(assis) == 5:
        return self.five
