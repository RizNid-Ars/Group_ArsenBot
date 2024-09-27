from aiogram import types, Dispatcher


async def echo_handler(message: types.Message):
    await message.answer(text="Неправильная команда!")


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)