document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const statusIndicator = document.getElementById('status-indicator');

    // URL do seu backend Python (Flask, FastAPI, etc.)
    // Certifique-se de que seu backend tem CORS habilitado para este frontend
    const CHATBOT_API_URL = 'http://localhost:5000/chat'; // Exemplo para Flask/FastAPI

    // Função para adicionar mensagem na UI
    function addMessage(text, sender, isError = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
        if (isError && sender === 'bot') {
            messageDiv.classList.add('error-message');
        }
        
        const p = document.createElement('p');
        p.textContent = text;
        messageDiv.appendChild(p);
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll
    }

    // Função para mostrar indicador de "digitando..."
    let typingIndicatorDiv = null;
    function showTypingIndicator() {
        if (typingIndicatorDiv) return; // Evita múltiplos indicadores
        typingIndicatorDiv = document.createElement('div');
        typingIndicatorDiv.classList.add('message', 'bot-message', 'typing-indicator');
        typingIndicatorDiv.innerHTML = '<p>Bot está digitando...</p>';
        chatMessages.appendChild(typingIndicatorDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function hideTypingIndicator() {
        if (typingIndicatorDiv) {
            chatMessages.removeChild(typingIndicatorDiv);
            typingIndicatorDiv = null;
        }
    }

    // Função para enviar mensagem ao backend
    async function sendMessageToBot(messageText) {
        addMessage(messageText, 'user');
        userInput.value = ''; // Limpa o input
        showTypingIndicator();
        updateStatus('connecting');

        try {
            const response = await fetch(CHATBOT_API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: messageText }), // Seu backend deve esperar um JSON com a chave "message"
            });

            hideTypingIndicator();

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({ detail: 'Erro desconhecido do servidor.' }));
                console.error('Erro na API:', response.status, errorData);
                addMessage(`Erro: ${errorData.detail || response.statusText}`, 'bot', true);
                updateStatus('offline');
                return;
            }

            const data = await response.json();
            // Assumindo que seu backend retorna um JSON com a chave "reply"
            // Ex: { "reply": "Esta é a resposta do bot." }
            addMessage(data.reply, 'bot');
            updateStatus('online');

        } catch (error) {
            hideTypingIndicator();
            console.error('Erro ao enviar mensagem:', error);
            addMessage('Desculpe, não consegui me conectar ao servidor. Verifique sua conexão ou tente mais tarde.', 'bot', true);
            updateStatus('offline');
        }
    }
    
    // Função para atualizar o indicador de status
    function updateStatus(status) { // 'online', 'offline', 'connecting'
        statusIndicator.className = ''; // Limpa classes existentes
        statusIndicator.classList.add(`status-${status}`);
        statusIndicator.title = status.charAt(0).toUpperCase() + status.slice(1);
    }

    // Event Listeners
    sendButton.addEventListener('click', () => {
        const messageText = userInput.value.trim();
        if (messageText) {
            sendMessageToBot(messageText);
        }
    });

    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            const messageText = userInput.value.trim();
            if (messageText) {
                sendMessageToBot(messageText);
            }
        }
    });

    // Verifica a conectividade inicial (opcional, mas bom para UX)
    async function checkInitialConnectivity() {
        updateStatus('connecting');
        try {
            // Pode ser um endpoint específico de health check ou o próprio /chat com uma mensagem vazia/padrão
            const response = await fetch(CHATBOT_API_URL, { 
                method: 'POST', // Ou GET se tiver um health check
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: "ping" }) // Pode não ser necessário se tiver um endpoint GET
            }); 
            if (response.ok) {
                updateStatus('online');
                console.log("Conectado ao backend do chatbot.");
            } else {
                updateStatus('offline');
                console.warn("Não foi possível conectar ao backend do chatbot na inicialização.");
            }
        } catch (error) {
            updateStatus('offline');
            console.warn("Erro de rede ao tentar conectar ao backend na inicialização.");
        }
    }

    checkInitialConnectivity(); // Verifica ao carregar a página
});