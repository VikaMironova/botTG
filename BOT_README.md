# Телеграм-бот для поиска информации о фильмах

Данный телеграм-бот позволяет находить информацию о фильмах и сериалах, используя API сервиса OMDB.

## Установка

Для запуска бота необходимо установить следующие зависимости:
- Python 3.8+
- Виртуальное окружение (опционально)
- Библиотеки aiohttp, aiogram, aiosqlite

Установите зависимости, используя следующую команду:
```
pip install -r requirements.txt
```

## Использование

Перед запуском бота необходимо создать файл config.py, который будет содержать в себе секретные ключи и токены для доступа к API, например:
```python
TELEGRAM_TOKEN = 'your_telegram_bot_token'
OMDB_API = 'your_omdb_api_key'
```

Чтобы запустить бота, выполните файл bot.py с помощью интерпретатора Python:
```
python bot.py
```

Бот реагирует на команды в чате:
- /start - приветственное сообщение
- /help - справка
- название - поиск информации о фильме или сериале

Пример использования:
```
inception
```

## База данных

Бот использует базу данных SQLite для хранения истории поиска пользователей. Файл базы данных - bot_db.db.

## Лицензия

Этот проект лицензирован в соответствии с условиями лицензии MIT.