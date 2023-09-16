import asyncio
from aiogram import Bot, Dispatcher
from config import CONFIG
from handlers import base, chatting
from utils.commands import set_commands
import nest_asyncio
from characterai import PyCAI


nest_asyncio.apply()
bot = Bot(token=CONFIG.bot_token.get_secret_value())
client = PyCAI(CONFIG.characterai_token.get_secret_value())
client.start()


async def main():
    dp = Dispatcher()

    dp.include_routers(base.router,
                       chatting.router,
                       )

    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
