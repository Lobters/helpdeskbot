import json
import logging

logging.basicConfig(filename='answer.log', level=logging.INFO)


def make_answer(raw_data):
    json_data = json.loads(raw_data)
    # update_id = json_data['update_id']
    try:
        message = json_data['message']
        chat_id = message['chat']['id']
    # message_user = message['first_name']
    # message_text = message['text']
    except KeyError:
        logging.critical("make_answer: bad format of message.")
        raise KeyError

    base_url = 'https://api.telegram.org/'
    token = '795602800:AAElqQv6FqbcvoidTryBEvFL7-G4aI2KLts'
    method = 'sendMessage'
    get_request = base_url + token + '/' + method + '?' + 'chat_id=' + str(chat_id) + '&text=' + 'Hello'
    return get_request
