from aiogram import Router, F
from aiogram.types import Message
from utils.character import Character

router = Router()


@router.message(F.text)
async def char_reply(message: Message):
    char = Character(message.from_user.id)
    result = char.reply_to_bot(message.text)

    await message.reply(text=result)
