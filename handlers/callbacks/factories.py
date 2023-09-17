from aiogram.filters.callback_data import CallbackData


class CharacterCallback(CallbackData, prefix='char'):
    id: str


class PaginationCallback(CallbackData, prefix='page'):
    page: int
    type: str
