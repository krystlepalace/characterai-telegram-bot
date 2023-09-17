from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    default_commands = [
            BotCommand(
                command="start",
                description="Start message"
                ),
            BotCommand(
                command="help",
                description="Command for help and command list of the bot"
                ),
            BotCommand(
                command="character",
                description="Menu with characters"
            ),
            BotCommand(
                command="search",
                description="<query> - search characters"
            ),
            ]

    await bot.set_my_commands(default_commands, BotCommandScopeDefault())