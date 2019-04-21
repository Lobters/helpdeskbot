import json
import logging

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bot.models import TelegramUser, TelegramChat, TelegramMessage

logging.basicConfig(filename='messages.log', level=logging.INFO)

base_api_url = 'https://api.telegram.org/bot722520790:AAEM0nUuaAD9BWFp0jv58VkeX3m-85DQOq0/'


@csrf_exempt
def index(request):
    raw_message = request.body.decode('cp1251')
    deserialized_message = json.loads(raw_message)['message']

    user = TelegramUser.objects.get(id=deserialized_message['from']['id'])
    chat = TelegramChat.objects.get(id=deserialized_message['chat']['id'])
    if not user:
        user = TelegramUser.objects.create_user_from_json(deserialized_message['from'])
    if not chat:
        chat = TelegramChat.objects.create_chat_from_json(deserialized_message['chat'])
    message = TelegramMessage.objects.create_message_from_json(deserialized_message, user, chat)

    postman = Postman(message)
    postman.send_response()
    return HttpResponse(status=200)


class Postman:
    def __init__(self, message):
        self.message = message

    def generate_response(self):
        if self.message.text == 'Hi':
            return "Hi, {}!".format(self.message.user)
        else:
            return "Bye {}!".format(self.message.user)

    @staticmethod
    def make_api_url(method, api_method, **kwargs):
        if method == 'GET':
            api_url = base_api_url + method + '?'
            for key, value in kwargs.items():
                api_url += str(key) + '=' + str(value) + '&'
            return api_url
        return base_api_url + api_method

    def send_response(self):
        response = self.generate_response()
        api_url = self.make_api_url('POST', 'sendMessage')
        sent_response = requests.post(api_url, {'chat_id': self.message.chat.id, 'text': response})
        return sent_response
