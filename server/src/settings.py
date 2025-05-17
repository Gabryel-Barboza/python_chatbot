from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    google_api_key: str | None = None
    llm_model: str = 'gemini-2.0-flash'
    llm_instructions: str = 'Você é um assistente pessoal e deve responder as perguntas que receber, de maneira objetiva e sucinta. Se necessário dê exemplos para enriquecer a resposta. Suas repostas são renderizadas em uma página HTML, então estilize para tal.'
    allowed_hosts: list[str] = ['http://127.0.0.1:8080']

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
        env_file_encoding='utf-8',
        env_ignore_empty=True,
    )


settings = Settings()
