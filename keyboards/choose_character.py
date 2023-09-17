from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.callbacks.factories import CharacterCallback, PaginationCallback

# example of characters dict
characters = {
    'Рик Санчез': "2aZlJFMrZvCUdu26Jvn-CUJ-wdcBCCfCPBwDysLyOyk",
    'Дио Брандо': "HZGKpemYKi0xEPaUCTkf_8H99MIoANY-vhvnFKPhwWw",
    'Мармок': "BB69lWJvnUwV4KBkzOmGiRyfSDkIlExCL3ltORDs2s4",
    'Чоппер': "69DhQhcbx2h486NkVWDGKOL8KNCgg3zB04ddOYoGE7M",
    'Шако': "IQHlxKIJQN7aSX6-R8V1xFOWs03RAuYfQJAzYqVIFxM",
    'Иван Золо': "uYw10Z_PyKv_fLruAQig0TIqescVmFu21ypSwX1e87Q",
    'Уолтер Вайт': "IJ6eOickbcEbXeAn1Yl8buPo6MCy46BzFEoCIsTIKLU",
    'Астольфо': "VIqELxEyIJttOJVzR_sYEDCOBq9OHuYBTmaEX97lFLw",
    'Масюня': "mJcAJWqqJ7AUgeO79tND_mr6jAMQXrolRaSpqdCFa9I"
}
characters = list(characters.items())
characters = [characters[i:i+5] for i in range(0, len(characters), 5)]


def characters_builder(page=0):
    builder = InlineKeyboardBuilder()
    for name, char_id in characters[page]:
        builder.button(
            text=name,
            callback_data=CharacterCallback(id=char_id).pack()
        )

    builder.button(
        text="<",
        callback_data=PaginationCallback(page=page-1, type="characters").pack()
    )
    builder.button(
        text=">",
        callback_data=PaginationCallback(page=page+1, type="characters").pack()
    )
    builder.adjust(*[1 for i in range(len(characters[page]))], 2)

    return builder


def search_results(results, page=0):
    builder = InlineKeyboardBuilder()
    paginated_results = [results[i:i + 5] for i in range(0, len(results), 5)]
    for char in paginated_results[page]:
        builder.button(
            text=char['participant__name'],
            callback_data=CharacterCallback(id=char["external_id"]).pack()
        )

    builder.button(
        text="<",
        callback_data=PaginationCallback(page=page-1, type="search").pack()
    )
    builder.button(
        text=">",
        callback_data=PaginationCallback(page=page+1, type="search").pack()
    )
    builder.adjust(*[1 for i in range(len(paginated_results[page]))], 2)

    return builder
