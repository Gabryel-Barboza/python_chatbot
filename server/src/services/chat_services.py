from google import genai
from google.genai import types

from src.settings import settings
from src.schemas import PromptInput

# Instanciar configurações de .env e variáveis necessárias
MODEL = settings.llm_model

sys_instructions = settings.llm_instructions
chat_config = types.GenerateContentConfig(system_instruction=sys_instructions)

client = genai.Client()
chat = client.chats.create(model=MODEL, config=chat_config)


async def get_models() -> str:
    text = f'\033[33m{"Display Name":^50} {"Model Name":^50}\033[m\n'
    models = '\n'.join(
        [f'{model.display_name:^50} {model.name:^50}' for model in client.models.list()]
    )
    text += models

    return {'reply': text}


async def prompt_model(prompt: PromptInput) -> dict:
    msg = prompt.message

    if msg == 'ping':
        return {}

    reply = chat.send_message(msg)

    return {'reply': reply.text}
