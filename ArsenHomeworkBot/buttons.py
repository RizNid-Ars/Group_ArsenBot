from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
meme_button = KeyboardButton('/mem')
meme_all_button = KeyboardButton('/mem_all')
music_button = KeyboardButton('/music')
quiz_button = KeyboardButton('/quiz')

start.add(start_button, info_button, meme_button,
          meme_all_button, music_button, quiz_button)


cancel_button = ReplyKeyboardMarkup(
    resize_keyboard=True
).add(KeyboardButton('Отмена'))


submit_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, row_width=2).add(
    KeyboardButton('Да'),
    KeyboardButton('Нет'))