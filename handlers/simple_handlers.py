from aiogram import types
import keyboards.reply as kb

async def hello_message(message: types.Message):
    await message.answer(f'Приветственное свообщение ', reply_markup=kb.start_keyboard)
    await message.delete()