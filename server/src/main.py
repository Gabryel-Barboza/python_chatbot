import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

client = genai.Client()


def get_models() -> str:
    print(f'\033[33m{"Display Name":^50} {"Model Name":^50}\033[m')

    for model in client.models.list():
        print(f'{model.display_name:^50} {model.name:^50}')

    option = input('Insira o nome do modelo: [gemini-2.0-flash] ')
    model = 'gemini-2.0-flash' if option == '' else option

    return model


def prompt_model(model: str, prompt: str):
    response = client.models.generate_content(model=model, contents=prompt)

    return response


model = get_models()

# Gerando mensagens sem contexto
response = prompt_model(
    model, 'Olá, estou criando um ChatBot em Python, poderia me dar algumas dicas?'
)
print(response.text)

# Criando contexto com chats
chat = client.chats.create(model=model)
response = chat.send_message('Olá, qual o seu modelo?')
print(response.text)

# Configuração de chat, aplicando instruções de sistema para o modelo
chat_config = types.GenerateContentConfig(
    system_instruction='Você é um assistente pessoal e responde às perguntas de forma objetiva, dando exemplos onde possível.'
)

chat = client.chats.create(model=model, config=chat_config)
response = chat.send_message('Qual a maneira mais rápida de se aprender Python?')
print(response.text)
print(chat.get_history())

prompt = input('Esperando prompt: ')
while prompt != 'fim':
    response = chat.send_message(prompt)
    print(response.text)
    prompt = input('Esperando prompt: ')
