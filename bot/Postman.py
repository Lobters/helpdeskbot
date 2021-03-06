import json
import logging

import requests
from django.core.exceptions import ObjectDoesNotExist

from .models import TelegramChat, TelegramUser, TelegramMessage

base_api_url = 'https://api.telegram.org/bot722520790:AAEM0nUuaAD9BWFp0jv58VkeX3m-85DQOq0/'


class Postman:
    def __init__(self, message):
        self.message = message

    def generate_response(self):
        if self.message.text == 'Hi':
            return "Hi, {}!".format(self.message.user)
        # elif self.message.text[:4] == 'task':

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

    @staticmethod
    def process_raw_request(request):
        raw_message = request.body.decode('cp1251')
        try:
            deserialized_message = json.loads(raw_message)['message']
        except KeyError:
            logging.critical("process_raw_request: no key 'message' in request.")
            raise KeyError

        try:
            chat = TelegramChat.objects.get(id=deserialized_message['chat']['id'])
        except ObjectDoesNotExist:
            chat = TelegramChat.objects.create_chat_from_json(deserialized_message['chat'])

        try:
            user = TelegramUser.objects.get(id=deserialized_message['from']['id'])
        except ObjectDoesNotExist:
            user = TelegramUser.objects.create_user_from_json(deserialized_message['from'])
        try:
            message = TelegramMessage.objects.get(message_id=deserialized_message['message_id'])
        except ObjectDoesNotExist:
            message = TelegramMessage.objects.create_message_from_json(deserialized_message, user, chat)

        return user, chat, message
