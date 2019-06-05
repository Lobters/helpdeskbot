import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from helpdeskbot.bot.Postman import Postman

logging.basicConfig(filename='errors.log', level=logging.ERROR)


@csrf_exempt
def index(request):
    _, _, message = Postman.process_raw_request(request)
    postman = Postman(message)
    postman.send_response()
    return HttpResponse(status=200)
