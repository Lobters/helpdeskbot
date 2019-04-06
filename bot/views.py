import datetime

import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from answer import make_answer

logging.basicConfig(filename='requests.log', level=logging.INFO)


@csrf_exempt
def index(request):
    raw_message = request.body.decode('cp1251')
    message = Message(raw_message)
    logging.info(message)
    return HttpResponse(status=200)


class Message:
    def __init__(self, raw_message):
        deserialized_message = json.loads(raw_message)['message']
        self.message_id = deserialized_message['message_id']
        self.user = User(deserialized_message['from'])
        self.chat = Chat(deserialized_message['chat'])
        self.date = datetime.datetime.fromtimestamp(deserialized_message['date'])
        self.text = '123'

    def __str__(self):
        return '"{}" message from {}'.format(self.text, self.user)


class User:
    def __init__(self, user_object):
        self.id = user_object.get('id')
        self.is_bot = user_object.get('is_bot')
        self.first_name = user_object.get('first_name')
        self.last_name = user_object.get('last_name')
        self.username = user_object.get('username')
        self.language_code = user_object.get('language_code')

    def __str__(self):
        return self.username


class Chat:
    def __init__(self, chat_object):
        self.id = chat_object.get('id')
        self.first_name = chat_object.get('first_name')
        self.last_name = chat_object.get('last_name')
        self.username = chat_object.get('username')
        self.type = chat_object.get('type')

    def __str__(self):
        return self.id
