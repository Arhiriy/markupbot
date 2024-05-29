from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2, get_keyboard_3, get_keyboard_4

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой бот показатель блюд', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Открыть список супов')
async def button_1_slick(message: types.Message):
    await message.answer('Тут ты можешь попросить бота показать тебе список супов', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отвравь фото открошки')
async def button_2_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://edalove.ru/wp-content/uploads/2022/10/photo.jpg', caption='Вот тебе вкусная окрошка')

@dp.message_handler(lambda message: message.text == 'Отвравь фото куринова супа')
async def button_2_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://recept-borscha.ru/wp-content/uploads/4/4/6/446b6d7c8eccb8014b515076ebfe1416.jpeg', caption='Вот тебе вкусный куриный суп')

@dp.message_handler(lambda message: message.text == 'Отвравь фото борща')
async def button_2_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663686606_11-mykaleidoscope-ru-p-borshch-so-smetanoi-oboi-15.jpg', caption='Вот тебе вкусный борщ')

@dp.message_handler(lambda message: message.text == 'Перейти на следуйщие блюда')
async def button_2_slick(message: types.Message):
    await message.answer('Тут ты можешь попросить бота показать тебе вторые блюда', reply_markup= get_keyboard_3())


@dp.message_handler(lambda message: message.text == 'Открыть список гарниров')
async def button_3_slick(message: types.Message):
    await message.answer('Тут ты можешь попросить бота показать тебе вторые блюда', reply_markup= get_keyboard_4())

@dp.message_handler(lambda message: message.text == 'Отвравь фото Жареной картошки')
async def button_4_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://cdn.fishki.net/upload/post/2018/11/11/2763706/zharenaya-kartoshka-s-lukom-i-chesnokom.jpg', caption='Вот тебе вкусная картошка')

@dp.message_handler(lambda message: message.text == 'Отвравь фото карбонара')
async def button_4_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Espaguetis_carbonara.jpg/1280px-Espaguetis_carbonara.jpg', caption='Вот тебе вкусная карбонара')

@dp.message_handler(lambda message: message.text == 'Отвравь фото стейка')
async def button_4_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663788543_38-mykaleidoscope-ru-p-steik-tibon-yeda-krasivo-42.jpg', caption='Вот тебе вкусный стейк')

@dp.message_handler(lambda message: message.text == 'Вернутся на раздел супов')
async def button_4_slick(message: types.Message):
    await message.answer('Тут ты можешь вернутся на раздел супов', reply_markup= get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)