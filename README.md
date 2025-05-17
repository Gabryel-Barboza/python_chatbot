# Projeto Chatbot Python

## Visão Geral

Este projeto consiste em um chatbot interativo com um backend desenvolvido em Python usando FastAPI (seguindo uma arquitetura MVC) e um frontend elegante construído com HTML, CSS e JavaScript puros (fornecido pelo Gemini 2.0 e refinado para integração ao backend). 

O objetivo é fornecer uma interface de usuário amigável para interagir com a lógica do chatbot processada no servidor e retornar respostas como em um aplicativo de conversas.

<img width="400px" height="500px" src="https://github.com/user-attachments/assets/fdbf6620-1999-43b2-8f40-57f92a443507"/>


## Funcionalidades

**Frontend:**
*   Interface de chat limpa e moderna.
*   Distinção visual clara entre mensagens do usuário e do bot.
*   Campo de entrada de texto e botão de envio intuitivos.
*   Rolagem automática para novas mensagens.
*   Indicador de status da conexão com o backend (Online, Offline, Conectando).
*   Indicador de "Bot está digitando...".
*   Design responsivo básico para adaptação em diferentes tamanhos de tela.
*   Envio de mensagens ao pressionar "Enter" ou clicar no botão "Enviar".

Envio do prompt para o ChatBot:

<img width="500px" src="https://github.com/user-attachments/assets/736e6aec-a945-4271-b997-12aa41751582"/>

Retorno da sua resposta:

<img width="500px" src="https://github.com/user-attachments/assets/dc591b36-e30b-4fc8-baf3-fbac5d08fa2a"/>


**Backend (Template FastAPI com MVC):**
*   API RESTful para receber mensagens do usuário e retornar respostas do chatbot.
*   Arquitetura organizada (inspirada em MVC) para separação de responsabilidades:
    *   **Schemas (Esquemas Pydantic):** Definição da estrutura dos dados de requisição e resposta.
    *   **Services (Serviços de endpoints):** Contêm a lógica de negócios do chatbot.
    *   **Controllers (Controladores das rotas):** Gerenciam os endpoints da API, recebem requisições HTTP e delegam para os serviços.
*   Suporte a CORS para permitir a comunicação com o frontend.
*   Validação de dados de entrada usando Pydantic.

## Tecnologias Utilizadas

**Frontend:**
*   HTML5
*   CSS3 (com Google Fonts e Font Awesome para ícones)
*   JavaScript (Vanilla JS, ES6+)

**Backend:**
*   Python 3.10+
*   FastAPI (framework web)
*   Uvicorn (servidor ASGI)
*   Pydantic (para validação de dados)

## Estrutura do Projeto

```
chatbot-project/
├── client/
|    src/
|     ├── assets/
|     |    ├── favicon.ico
|     |    └── style.css
|     |
│     ├── index.html
│     └── main.js
│
├── server/
|
└── README.md # Este arquivo
```

## Colocando o projeto para rodar

O frontend é composto por arquivos estáticos HTML, CSS e JavaScript.

