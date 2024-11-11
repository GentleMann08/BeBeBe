from aiogram import Bot                         
from aiogram import Dispatcher
from aiogram.filters import Command             
from aiogram.filters import CommandStart        
from aiogram import F                                              
import aiogram.exceptions                                   
from aiogram.types import CallbackQuery        
from aiogram.types import Message               
from aiogram.types import FSInputFile           
# from handlers.commands_handlers import command_routers

import asyncio                                  
import logging                                  
from settings import Settings                   
import logging                                  
# from handlers import routers_list
# from handlers.commands_handlers import start_handler

async def main():
    logging.basicConfig(level=logging.INFO)                    

    telegram_token = Settings.telegram_token

    bot = Bot(token=telegram_token)
    dp = Dispatcher()

    # dp.include_routers(*routers_list)

    print("Starting server")
    await dp.start_polling(bot)

def start_app():
    print("Starting app")
    asyncio.run(main())


if __name__ == "__main__":
    start_app()