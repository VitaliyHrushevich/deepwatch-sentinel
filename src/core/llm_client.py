import requests
import json

def ask_ollama(user_query, context_data, model="llama3:latest"):
    url = "http://localhost:11434/api/chat" # Используем /api/chat

    system_prompt = (
        "Ты — DeepWatch Sentinel, ИИ-аналитик."
        "Отвечай на русском языке. Твоя задача — интерпретировать данные мониторинга инфраструктуры. "
        "Дай четкий бизнес-вывод."
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Данные из базы:\n{context_data}\n\nВопрос: {user_query}"}
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()

        # Ollama в режиме chat возвращает ответ в поле ['message']['content']
        result = response.json()
        return result['message']['content']

    except Exception as e:
        return f"❌ Ошибка связи с Ollama: {str(e)}"
