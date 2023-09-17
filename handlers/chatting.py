from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.choose_character import characters_builder
from utils.character import Character


router = Router()


@router.message(Command("character"))
async def choose_character_menu(message: Message):
    await message.reply(text="Choose character:",
                        reply_markup=characters_builder().as_markup())


@router.message(F.text)
async def char_reply(message: Message):
    char = Character(user_id=message.from_user.id)
    if char.character is None:
        await message.reply("Сначала выберите персонажа коммандой /character")
        return

    result = await char.reply_to_bot(message.text)

    await message.reply(text=result)
