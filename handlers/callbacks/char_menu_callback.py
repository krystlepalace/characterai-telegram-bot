from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from handlers.callbacks.factories import CharacterCallback, PaginationCallback
from handlers.search import SearchQuery
from utils import character
from keyboards.choose_character import characters_builder, search_results
import main

router = Router()


@router.callback_query(CharacterCallback.filter(F.id != None))
async def process_choose_character(callback: CallbackQuery,
                                   callback_data: CharacterCallback):
    char = character.Character(user_id=callback.from_user.id)
    await char.change_char(callback_data.id)

    info = await main.client.character.info(callback_data.id)
    await callback.message.edit_text(
        f"You have choosed character {info['character']['name']}")
    await callback.message.answer(info['character']['greeting'])
    await callback.answer()


@router.callback_query(PaginationCallback.filter(F.type == "characters"))
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


@router.callback_query(PaginationCallback.filter(F.type == "search"))
async def process_change_page(callback: CallbackQuery,
                              callback_data: PaginationCallback,
                              state: FSMContext):
    if callback_data.page < 0:
        await callback.answer()
        return

    await state.set_state(SearchQuery.results)
    result_state = await state.get_data()
    await callback.message.edit_reply_markup(reply_markup=search_results(
        page=callback_data.page,
        results=result_state
        ).as_markup()
    )
    await callback.answer()
