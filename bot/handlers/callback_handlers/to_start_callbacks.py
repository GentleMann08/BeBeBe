from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.menu import Menu

to_start_router = Router()

@to_start_router.callback_query(F.data == 'to_start')
async def handle_bleu_check(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_message_id = data.get("last_message_id")

    if last_message_id:
        await callback_query.message.chat.delete_message(message_id=last_message_id)

    keyboard = await Menu.start()
    new_message = await callback_query.message.answer(
        text="Welcome to BeBeBeAI!",
        reply_markup=keyboard
    )

    await state.update_data(last_message_id=new_message.message_id)
