from .bleu_callbacks import bleu_router
from .to_start import to_start_router
from .llm_callbacks import llm_router

callbacks_routers = [
    bleu_router,
    to_start_router,
    llm_router
]