from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.menu import Menu

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: Message, bot: Bot):
    chat = message.chat.id
    chat_type = message.chat.type

    # keyboard = await Menu.start()
    await bot.send_message(
        chat_id=chat, 
        text="Добро пожаловать в BeBeBeAI!"
        # reply_markup=keyboard
        )