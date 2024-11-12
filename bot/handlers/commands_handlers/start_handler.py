from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.menu import Menu

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    chat = message.chat.id

    keyboard = await Menu.start()
    last_messafe = await bot.send_message(
        chat_id=chat, 
        text="Welcome to BeBeBeAI!",
        reply_markup=keyboard
        )
    
    await state.update_data(last_message_id=last_messafe.message_id)