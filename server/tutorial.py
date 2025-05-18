from IPython.display import HTML, Markdown, display
from google.genai import types
from google import genai

from src.services import get_models

# Instanciando o cliente do modelo
client = genai.Client()


# Visualizando os modelos disponíveis
async def print_models():
    models = await get_models()
    print(models)


model_id = 'gemini-2.0-flash'

# Gerando conteúdo com o modelo
response = client.models.generate_content(
    model=model_id, contents='Me faça uma receita de bolo de chocolate.'
)
display(response.text)
print('=' * 100)

# Criando um chat para manter histórico e criar contexto
chat_config = types.GenerateContentConfig(
    system_instruction='Você é um assistente pessoal e deve responder aos prompts de forma sucinta.'
)
chat = client.chats.create(model=model_id, config=chat_config)

# Enviando prompts ao modelo
response = chat.send_message(
    'Olá, gostaria de aprender a linguagem Python. Se comporte como um profissional senior e me ensine os princípios da linguagem.'
)
display(response.text)
display(response)

print('=' * 100)

# Utilizando outras ferramentas na geração de conteúdo
response = client.models.generate_content(
    model=model_id,
    contents='Qual foi o nome feminino eleito como mais bonito do mundo em 2025?',
    config={'tools': [{'google_search': {}}]},
)
# Utilizar display para renderizar formatos de HTML ou Markdown no frontend
display(f'Response: \n{response.text}')

sites = [
    site.web.title
    for site in response.candidates[0].grounding_metadata.grounding_chunks
]
print(f'Páginas utilizadas na pesquisa: {",".join(sites)}')


# Criando agentes
