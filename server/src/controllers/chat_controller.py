from fastapi import APIRouter, status
from src.services import prompt_model
from src.schemas import PromptInput

router = APIRouter(prefix='/chat')


# Criar rota para enviar mensagens ao prompt
@router.post('/', status_code=status.HTTP_202_ACCEPTED)
async def send_prompt_model(prompt: PromptInput):
    reply = await prompt_model(prompt)

    return reply
