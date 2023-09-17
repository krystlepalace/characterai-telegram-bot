import asyncio
from aiogram import Bot, Dispatcher
from config import CONFIG
from handlers import base, chatting, search
from handlers.callbacks import char_menu_callback
from utils.commands import set_commands
from characterai import PyAsyncCAI


bot = Bot(token=CONFIG.bot_token.get_secret_value())
client = PyAsyncCAI(token=CONFIG.characterai_token.get_secret_value())


async def main():
    dp = Dispatcher()

    dp.include_routers(base.router,
                       search.router,
                       chatting.router,
                       char_menu_callback.router,
                       )

    await client.start()
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
