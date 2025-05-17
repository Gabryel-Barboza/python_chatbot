from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers import chat_controller
from .settings import settings

app = FastAPI()

# Incluir routers
app.include_router(chat_controller.router)


origins = settings.allowed_hosts
# Incluir middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
