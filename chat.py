from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

from chatgpt import ChatGPT
# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

auth_token = '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'
chat_gpt = ChatGPT(auth_token)
# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

# Функция для непосредственной обработки диалога.
def handle_request(request, response):
    # получение текста сообщения от пользователя
    user_input = request.command
    
    # использование ChatGPT API для получения ответа на вопрос пользователя
    bot_response = chat_gpt.generate_response(user_input)
    
    # отправка ответа в Яндекс.Диалоги 
    response.set_text(bot_response)
    return response

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_request(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )



# обработка запросов от пользователя через SDK Яндекс.Диалогов 