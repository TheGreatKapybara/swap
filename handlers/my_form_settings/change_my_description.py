import keyboards.reply as kb
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.my_form_settings import update_description, get_my_form


class DescriptionUpdater(StatesGroup):
    GET_DESCRIPTION = State()


async def change_my_description(message: types.Message, bot: Bot, state: FSMContext):
    await message.delete()
    await message.answer('Отправьте новый текст')
    await state.set_state(DescriptionUpdater.GET_DESCRIPTION)


async def description_push(message: types.Message, bot: Bot, state: FSMContext):
    update_description(message.from_user.id, message.text)
    await message.answer('Ваша анкета:')
    form = get_my_form(message.from_user.id)
    form_info = f'<b>{form[0][1]} {form[0][2]}</b>\n' \
                f'<i>{form[0][3]}, {form[0][4]}</i>\n' \
                f'<i>Родной язык - {form[0][5]}</i>\n\n' \
                f'{form[0][6]}'
    await bot.send_photo(chat_id=message.chat.id, photo=form[0][7], caption=form_info,
                         parse_mode='html', reply_markup=kb.my_form_settings)
    await state.clear()