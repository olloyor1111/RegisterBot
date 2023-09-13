import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import contents, main as main_handler, register
from aiogram.fsm.storage.memory import MemoryStorage
from extra import BOT_TOKEN

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="html")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(main_handler.router, register.router, contents.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")
