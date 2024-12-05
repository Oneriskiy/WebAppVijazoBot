import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers import router
from callbacks import callbackrouter

#Выше находятся нужные импорты

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(TOKEN)


async def main_func():
    dp.include_router(router)
    dp.include_router(callbackrouter)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # Запуск основной асинхронной функции
        asyncio.run(main_func())  # Запускаем все подготовительные шаги и бота
    except KeyboardInterrupt:
        print("Exit")