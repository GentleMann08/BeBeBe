from .bleu_callbacks import bleu_router
from .to_start_callbacks import to_start_router
from .llm_callbacks import llm_router
# from .models_callbacks import models_router

callbacks_routers = [
    bleu_router,
    to_start_router,
    llm_router,
    # models_router
]