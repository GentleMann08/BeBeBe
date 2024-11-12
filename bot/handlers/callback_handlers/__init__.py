from .bleu_callbacks import bleu_router
from .system_callbacks import system_router
from .llm_callbacks import llm_callback_router

callbacks_routers = [
    bleu_router,
    system_router,
    llm_callback_router
]