from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

builder = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text="Информация об исполнителе", callback_data="info")],
    [InlineKeyboardButton(text="Соц.сети исполнителя", callback_data="social")],
    [InlineKeyboardButton(text="Помощь", callback_data="help")]
    ])

builderBack = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text="Назад", callback_data="back")]
    ])

builderBackTwo = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text="На старт!", callback_data="back")]
    ])

builderSocial = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text="Яндекс Музыка", url ="https://music.yandex.ru/artist/16864620")],
    [InlineKeyboardButton(text="ВК Музыка", url ="https://vk.com/artist/vijazo")],
    [InlineKeyboardButton(text="Телеграм канал", url="https://t.me/Vijazik")],
    [InlineKeyboardButton(text="Группа Вконтакте", url="https://vk.com/vijazoofficial")],
    [InlineKeyboardButton(text="Назад", callback_data="back")]
    ])