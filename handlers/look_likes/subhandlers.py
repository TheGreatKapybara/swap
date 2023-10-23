import keyboards.reply as kb
from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.look_likes import liked_form_id
from handlers.look_forms.subhandlers import search_friends
from handlers.simple_handlers import hello_message


class AnswerLikeCollector(StatesGroup):
    GET_LIKE_ANSWER = State()

async def callback_likes(message: types.Message, bot: Bot, state: FSMContext):
    form = liked_form_id(message.chat.id)
    if form == False:
        await state.clear()
        await message.answer('Вот и кончились ваши лайки')
        await search_friends(message, bot, state)
    else:
        form_info = f'<b>{form[1]} {form[2]}</b>\n' \
                    f'<i>{form[3]}, {form[4]}</i>\n' \
                    f'<i>Родной язык - {form[5]}</i>\n\n' \
                    f'{form[6]}'
        await bot.send_photo(chat_id=message.chat.id, photo=form[7], caption=form_info,
                             parse_mode='html', reply_markup=kb.search_forms_keyboard)
        await state.update_data(form_id=form[0])
        await state.update_data(name=form[1])
        await state.set_state(AnswerLikeCollector.GET_LIKE_ANSWER)

async def answer_like(message: types.Message, bot: Bot, state: FSMContext):
     if message.text == 'Нравится':
         data = await state.get_data()
         str(data)
         user_id = data.get('form_id')
         name = data.get("name")
         await bot.send_message(chat_id=message.from_user.id,
                               text=f'<a href="tg://user?id={user_id}">{name}</a>', parse_mode='html')
         await bot.send_message(chat_id=user_id,
                                text=f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>',
                                parse_mode='html')
     if message.text == 'Главние меню':
         await state.clear()
         await hello_message(message, bot)
     await callback_likes(message, bot, state)

