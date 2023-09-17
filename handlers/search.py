from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
import main
from keyboards.choose_character import search_results

router = Router()


class SearchQuery(StatesGroup):
    results = State()


@router.message(Command("search"))
async def search_cmd(message: Message, command: CommandObject, state: FSMContext):
    query = command.args
    result = await main.client.character.search(query)

    await state.set_state(SearchQuery.results)
    await state.set_data(result["characters"])
    await message.reply(text=f"Search for '{query}'",
                        reply_markup=search_results(result["characters"]).as_markup())
