import keyboards.reply as kb
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from database.my_form_settings import get_my_form
from database.utils import check_my_form


async def my_form(message: types.Message, bot: Bot, state: FSMContext):
    form = check_my_form(message.from_user.id)
    if form == False:
        await message.answer('Вы еще не создали анкету', reply_markup=kb.form_create_options)
    else:
        await message.answer('Ваша анкета:')
        form = get_my_form(message.from_user.id)
        form_info = f'<b>{form[0][1]} {form[0][2]}</b>\n' \
                    f'<i>{form[0][3]}, {form[0][4]}</i>\n' \
                    f'<i>Родной язык - {form[0][5]}</i>\n\n' \
                    f'{form[0][6]}'
        await bot.send_photo(chat_id=message.chat.id, photo=form[0][7], caption=form_info,
                             parse_mode='html', reply_markup=kb.my_form_settings)
    await message.delete()
    await state.clear()

async def hide_my_form(message: types.Message):
    await message.answer('Ваша анкета скрыта', reply_markup=kb.start_keyboard)
    await message.delete()