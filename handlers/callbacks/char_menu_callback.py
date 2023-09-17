from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.callbacks.factories import CharacterCallback, PaginationCallback
from utils import character
from keyboards.choose_character import characters_builder
import main

router = Router()


@router.callback_query(CharacterCallback.filter(F.id != None))
async def process_choose_character(callback: CallbackQuery,
                                   callback_data: CharacterCallback):
    char = character.Character(user_id=callback.from_user.id)
    await char.change_char(callback_data.id)

    info = await main.client.character.info(callback_data.id)
    await callback.message.edit_text(f"You have choosed character {info['character']['name']}")
    await callback.message.answer(info['character']['greeting'])
    await callback.answer()


@router.callback_query(PaginationCallback.filter(F.page >= -1))
async def process_change_page(callback: CallbackQuery,
                              callback_data: PaginationCallback):
    if callback_data.page < 0:
        await callback.answer()
        return

    await callback.message.edit_reply_markup(reply_markup=characters_builder(
        page=callback_data.page
            ).as_markup()
        )
    await callback.answer()
