from aiogram import Dispatcher, F, Bot
import asyncio
from aiogram.filters import Command
from handlers.look_forms.subhandlers import search_friends, LikeCollector, answer
from handlers.look_likes.subhandlers import callback_likes, answer_like, AnswerLikeCollector
from handlers.my_form_settings.change_my_description import change_my_description, description_push, DescriptionUpdater
from handlers.my_form_settings.change_my_photo import change_my_photo, photo_push, PhotoUpdater
from handlers.my_form_settings.create_my_form import get_name, get_surename, FormMaker, get_country, get_city, \
    get_language, get_description, get_photo, form_result
from handlers.my_form_settings.simple_handlers import my_form, hide_my_form
from handlers.simple_handlers import hello_message

token = '6179591494:AAFl9ShxK_jqbDv7Sw-gOMKga_T44zsmXHk'

bot = Bot(token=token)

dp = Dispatcher()

dp.message.register(hello_message, Command(commands="start"))
dp.message.register(search_friends, F.text == 'Начинаем поиск')
dp.message.register(answer, LikeCollector.GET_ANSWER)
dp.message.register(callback_likes, F.text == 'Показать мои лайки')
dp.message.register(answer_like, AnswerLikeCollector.GET_LIKE_ANSWER)
dp.message.register(my_form, F.text == 'Моя анкета')
dp.message.register(change_my_photo, F.text == 'Изменить фото')
dp.message.register(photo_push, PhotoUpdater.GET_PHOTO)
dp.message.register(change_my_description, F.text == 'Изменить описание')
dp.message.register(description_push, DescriptionUpdater.GET_DESCRIPTION)
dp.message.register(hide_my_form, F.text == 'Скрыть мою анкету')
dp.message.register(hello_message, F.text == 'Главное меню')
dp.message.register(get_name, F.text == 'Создать анкету')
dp.message.register(get_name, F.text == 'Изменить анкету')
dp.message.register(get_surename, FormMaker.GET_NAME)
dp.message.register(get_country, FormMaker.GET_SURENAME)
dp.message.register(get_city, FormMaker.GET_COUNTRY)
dp.message.register(get_language, FormMaker.GET_CITY)
dp.message.register(get_description, FormMaker.GET_LANGUAGE)
dp.message.register(get_photo, FormMaker.GET_DESCRIPTION)
dp.message.register(form_result, FormMaker.GET_PHOTO)




async def on_startup():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(on_startup())