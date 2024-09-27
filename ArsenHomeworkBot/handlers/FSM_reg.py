from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons

from aiogram.types import ReplyKeyboardRemove


class fsm_registration(StatesGroup):
    fullname = State()
    date = State()
    email = State()
    address = State()
    phone = State()
    gender = State()
    photo = State()
    submit = State()


async def start_reg(message: types.Message):
    await message.answer('Привет!\n'
                         'Введи фио: \n\n'
                         '!Для того чтобы воспользоваться командами, '
                         'нажмите на "Отмена"!',
                         reply_markup=buttons.cancel_button)
    await fsm_registration.fullname.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await message.answer('Введите дату рождения: ')
    await fsm_registration.next()


async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text

    await message.answer('Укажите свою эл.почту: ')

    await fsm_registration.next()


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await message.answer('Введите адрес:')
    await fsm_registration.next()


async def load_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer('Введите номер телефона: ')
    await fsm_registration.next()


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    await message.answer('Укажите пол: ')
    await fsm_registration.next()


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await message.answer('Отправьте фото: ')
    await fsm_registration.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id


    await message.answer('Верные ли данные ?')
    await message.answer_photo(
        photo=data['photo'],
        caption=f'ФИО: {data["fullname"]}\n'
        f'Дата рождения: {data["date"]}\n'
        f'Почта: {data["email"]}\n'
        f'Адрес: {data["address"]}\n'
        f'Номер телефона: {data["phone"]}\n'
        f'Пол: {data["gender"]}',
        reply_markup=buttons.submit_buttons)

    await fsm_registration.next()

async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        await message.answer('Отлично, регистрация пройдена!',
                             reply_markup=kb)
        await state.finish()


    elif message.text == 'Нет':
        await message.answer('Хорошо, регистрация отменена!',
                             reply_markup=kb)
        await state.finish()
    else:
        await message.answer('Выберите "Да" или "Нет"')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!')


def register_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(
        equals='Отмена',
        ignore_case=True),
                                state="*")

    dp.register_message_handler(start_reg, commands=['reg'])

    dp.register_message_handler(load_name,
                                state=fsm_registration.fullname)
    dp.register_message_handler(load_date,
                                state=fsm_registration.date)
    dp.register_message_handler(load_email,
                                state=fsm_registration.email)
    dp.register_message_handler(load_address,
                                state=fsm_registration.address)
    dp.register_message_handler(load_phone,
                                state=fsm_registration.phone)
    dp.register_message_handler(load_gender,
                                state=fsm_registration.gender)
    dp.register_message_handler(load_photo,
                                state=fsm_registration.photo,
                                content_types=['photo'])

    dp.register_message_handler(submit,
                                state=fsm_registration.submit)