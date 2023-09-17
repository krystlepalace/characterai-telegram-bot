from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hello there! This bot porvides access to character.ai\n"
                         "You can talk with avaible character from /character menu"
                         "If you need some help send /help")


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Help message.\n\n"
                         "/start - greeting message\n"
                         "/help - this message\n"
                         "/character - choose character for dialog\n\n"
                         "Author - @krystlepalace")
