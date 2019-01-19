import json


def make_answer(raw_data):
    json_data = json.loads(raw_data)
    update_id = json_data['update_id']
    message = json_data['message']
    message_id = message['id']
    message_user = message['first_name']
    message_text = message['text']
    return json_data
