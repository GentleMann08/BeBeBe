from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.menu import Menu

llm_router = Router()

@llm_router.callback_query(F.data == 'llm')
async def llm_generation(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_message_id = data.get("last_message_id")

    if last_message_id:
        await callback_query.message.chat.delete_message(message_id=last_message_id)

    keyboard = await Menu.models()
    last_messafe = await callback_query.message.answer(
        text="Select your AI-Model",
        reply_markup=keyboard
        )
    
    await state.update_data(last_message_id=last_messafe.message_id)