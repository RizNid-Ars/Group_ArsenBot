from aiogram import types, Dispatcher
from config import bot, admin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f"Добро пожаловать, {member.full_name}\n\n"
                             f"Правила группы:\n"
                             f"* Не материться!\n"
                             f"* Не спамить!\n")


words = ['дурак', 'тупой', "козел", "овца", "ублюдок", "черт", "идиот", "Засранец", "простофиля"]


async def filter_words(message: types.Message):
    message_text = message.text.lower()
    for word in words:
        if word in message_text:
            await message.answer(f'Не ругайся! {message.from_user.full_name}')
            await message.delete()
            break


user_warnings = {}

async def user_warning(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admin:
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть овтетом на сообщение!')

        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name
            user_warnings[user_id] = user_warnings.get(user_id, 0) + 1

            for Admin in admin:
                await bot.send_message(chat_id=Admin,
                                       text=f"{user_name} получил предупреждение ({user_warnings[user_id]}/3)")

                if user_warnings[user_id] >= 3:
                    await bot.kick_chat_member(message.chat.id, user_id)
                    await bot.unban_chat_member(message.chat.id, user_id)

                    await bot.send_message(chat_id=message.chat.id,
                                           text=f'{user_name} был удален за превышение количества предупреждний!')

async def reply_webapp(message: types.Message):
    await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.message_id)

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

    geeks_online = KeyboardButton('Geeks Online',
                                  web_app=types.WebAppInfo(url='https://online.geeks.kg/'))

    youtube = KeyboardButton('YouTube',
                             web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    spotify = KeyboardButton('Spotify', web_app=types.WebAppInfo(url='https://open.spotify.com/'))

    jutsu = KeyboardButton('Jut.Su', web_app=types.WebAppInfo(url='https://jut.su/'))

    netflix = KeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/kg/'))

    kinokrad = KeyboardButton('Kinokrad', web_app=types.WebAppInfo(url='https://kinokrad.ac/'))

    os_kg = KeyboardButton('OK KG', web_app=types.WebAppInfo(url='https://oc.kg/'))

    keyboard.add(geeks_online, youtube, spotify, jutsu, netflix, kinokrad, os_kg)

    await message.answer(text='WebApp кнопки: ', reply_markup=keyboard)




def register_admin_group(dp: Dispatcher):
    dp.register_message_handler(welcome_user,
                                content_types=[types.ContentType.NEW_CHAT_MEMBERS])

    dp.register_message_handler(user_warning, commands=['warn'])

    dp.register_message_handler(filter_words)