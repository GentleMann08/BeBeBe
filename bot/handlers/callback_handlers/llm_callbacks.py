from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.menu import Menu
from ..states import LLM_Generation
from ai.scripts import LLM_bot

llm_callback_router = Router()

@llm_callback_router.callback_query(F.data == 'llm')
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

@llm_callback_router.callback_query(F.data.endswith('_model'))
async def models_state(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_message_id = data.get("last_message_id")

    model = callback_query.data.replace('_model', '')
    
    if last_message_id:
        await callback_query.message.chat.delete_message(message_id=last_message_id)

    new_message = await callback_query.message.answer(
        text=f'Send your text to "{model}" model or type /exit to quit'
    )

    await state.set_state(LLM_Generation.text_to_model)
    await state.update_data(model=model)
    
    await callback_query.answer(model)

    await state.update_data(model=model)
    await state.update_data(LLM_model = LLM_bot(model_name = model))
    await state.update_data(last_message_id=new_message.message_id)