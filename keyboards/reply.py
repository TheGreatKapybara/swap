from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Начинаем поиск'),
     KeyboardButton(text='Моя анкета')],
    [KeyboardButton(text='Скрыть мою анкету'),
     KeyboardButton(text='Показать мои лайки')],
])

search_forms_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Нравится'),
     KeyboardButton(text='Не нравится')],
     [KeyboardButton(text='Главное меню')],
])

my_form_settings = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Изменить анкету'),
     KeyboardButton(text='Изменить фото')],
    [KeyboardButton(text='Изменить описание'),
     KeyboardButton(text='Главное меню')],
])

form_create_options = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Создать анкету'),
     KeyboardButton(text='Главное меню')],
])