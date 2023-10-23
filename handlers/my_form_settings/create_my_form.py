import keyboards.reply as kb
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.my_form_settings import form_import, form_update
from database.utils import check_my_form


class FormMaker(StatesGroup):
    GET_NAME = State()
    GET_SURENAME = State()
    GET_COUNTRY = State()
    GET_CITY = State()
    GET_LANGUAGE = State()
    GET_DESCRIPTION = State()
    GET_PHOTO = State()

async def get_name(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer('Введите ваше имя')
    await state.set_state(FormMaker.GET_NAME)

async def get_surename(message: types.Message, state: FSMContext):
    await message.answer('Введите вашу фамилию')
    await state.update_data(name=message.text)
    await state.set_state(FormMaker.GET_SURENAME)

async def get_country(message: types.Message, state: FSMContext):
    await message.answer('Из какой вы страны')
    await state.update_data(surename=message.text)
    await state.set_state(FormMaker.GET_COUNTRY)

async def get_city(message: types.Message, state: FSMContext):
    await message.answer('В каком городе вы живёте')
    await state.update_data(country=message.text)
    await state.set_state(FormMaker.GET_CITY)

async def get_language(message: types.Message, state: FSMContext):
    await message.answer('Ваш родной язык')
    await state.update_data(city=message.text)
    await state.set_state(FormMaker.GET_LANGUAGE)

async def get_description(message: types.Message, state: FSMContext):
    await message.answer('Расскажите о себе')
    await state.update_data(language=message.text)
    await state.set_state(FormMaker.GET_DESCRIPTION)

async def get_photo(message: types.Message, state: FSMContext):
    await message.answer('Отправьте ваше фото')
    await state.update_data(description=message.text)
    await state.set_state(FormMaker.GET_PHOTO)

async def form_result(message: types.Message, state: FSMContext, bot: Bot):
    context_data = await state.get_data()
    str(context_data)
    user_id = message.from_user.id
    name = context_data.get("name")
    surename = context_data.get("surename")
    country = context_data.get("country")
    city = context_data.get("city")
    language = context_data.get("language")
    description = context_data.get("description")
    photo = message.photo[0].file_id
    await message.answer('Ваша анкета:', reply_markup=kb.my_form_settings)
    form_info = f'<b>{name} {surename}</b>\n' \
                f'<i>{country}, {city}</i>\n' \
                f'<i>Родной язык - {language}</i>\n\n' \
                f'{description}'
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=form_info, parse_mode='html')
    is_exists = check_my_form(user_id)
    if is_exists == False:
        form_import(user_id, name, surename, country, city, language, description, photo)
    else:
        form_update(user_id, name, surename, country, city, language, description, photo)
    await state.clear()