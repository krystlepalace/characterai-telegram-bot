from aiogram.utils.keyboard import InlineKeyboardBuilder

# example of characters dict
characters = {
    'Рик Санчез': "2aZlJFMrZvCUdu26Jvn-CUJ-wdcBCCfCPBwDysLyOyk",
    'Дио Брандо': "HZGKpemYKi0xEPaUCTkf_8H99MIoANY-vhvnFKPhwWw",
    'Мармок': "BB69lWJvnUwV4KBkzOmGiRyfSDkIlExCL3ltORDs2s4",
    'Чоппер': "69DhQhcbx2h486NkVWDGKOL8KNCgg3zB04ddOYoGE7M"
}


def characters_builder():
    builder = InlineKeyboardBuilder()
    for name, char_id in characters.items():
        builder.button(
            text=name,
            callback_data=char_id
        )
    builder.adjust(2)

    return builder
