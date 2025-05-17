from pydantic import BaseModel


class PromptInput(BaseModel):
    message: str
