import config
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
import aiohttp
import aiosqlite

bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def get_movie_info(title):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://www.omdbapi.com/?t={title}&apikey={config.OMDB_API}') as resp:
            data = await resp.json()
            return data

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    response_message = "Напиши название фильма или сериала:"
    await message.reply(response_message)

@dp.message_handler(commands=['help'])
async def send_help(message: Message):
    response_message = (
        "Привет! Я бот для поиска информации о фильмах и сериалах.\n\n"
        "Я поддерживаю следующие команды:\n"
        "/start - Начать использование бота\n"
        "/help - Получить справку о доступных командах\n"
        "/stats - Статистика поиска\n"
        "Просто напиши мне название фильма или сериала, и я постараюсь найти для тебя информацию о нем."
    )
    await message.reply(response_message)

@dp.message_handler()
async def search_film(message: Message):
    film_title = message.text
    movie_info = await get_movie_info(film_title)

    if movie_info['Response'] == 'True':
        response = (f"Название: {movie_info['Title']}\nГод: {movie_info['Year']}\nРейтинг: {movie_info['imdbRating']}"
                    f"\nПостер: {movie_info['Poster']}")

        async with aiosqlite.connect('bot_db.db') as db:
            await db.execute("INSERT INTO search_history (user_id, film_name) VALUES (?, ?)",
                             (message.from_user.id, film_title))
            await db.commit()

    else:
        response = "К сожалению, информация о фильме не найдена."
    await message.answer(response)


async def on_startup(_):
    async with aiosqlite.connect('bot_db.db') as db:
        await db.execute("CREATE TABLE IF NOT EXISTS search_history (user_id INTEGER, film_name TEXT)")
        await db.commit()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)