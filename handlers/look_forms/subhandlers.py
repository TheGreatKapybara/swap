import keyboards.reply as kb
from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.look_forms import random_forms, safe_like, like_counter
from handlers.simple_handlers import hello_message



class LikeCollector(StatesGroup):
    GET_ANSWER = State()

async def search_friends(message: types.Message, bot: Bot, state: FSMContext):
    form = random_forms()
    form_info = f'<b>{form[1]} {form[2]}</b>\n' \
                f'<i>{form[3]}, {form[4]}</i>\n' \
                f'<i>Родной язык - {form[5]}</i>\n\n' \
                f'{form[6]}'
    await bot.send_photo(chat_id=message.chat.id, photo=form[7], caption=form_info,
                         parse_mode='html', reply_markup=kb.search_forms_keyboard)
    await state.update_data(form_id=form[0])
    await state.set_state(LikeCollector.GET_ANSWER)
    await message.delete()

async def answer(message: types.Message, bot: Bot, state: FSMContext):
    if message.text == 'Нравится':
        data = await state.get_data()
        str(data)
        liked_id = data.get('form_id')
        safe_like(message.from_user.id, liked_id)
        await bot.send_message(chat_id=liked_id, text=f'Вас лайкнули {like_counter(liked_id)} человек',
                               reply_markup=kb.start_keyboard)
        await search_friends(message, bot, state)
    if message.text == 'Не нравится':
        await search_friends(message, bot, state)
    if message.text == 'Главное меню':
        await state.clear()
        await hello_message(message)