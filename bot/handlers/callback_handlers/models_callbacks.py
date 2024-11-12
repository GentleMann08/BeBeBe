from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.menu import Menu

models_router = Router()

@models_router.callback_query(str(F.data).endswith('_model'))
async def model_state(callback_query: CallbackQuery, state: FSMContext):
    model = str(F.data).replace('_model', '')
    callback_query.answer(model)