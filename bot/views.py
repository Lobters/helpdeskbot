import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from answer import make_answer


@csrf_exempt
def index(request):
    try:
        with open('error_log.txt', 'a') as f:
            f.write(str(request.body.decode('UTF-8')))
        data = json.loads(str(request.body.decode('UTF-8')))
        answer = str(make_answer(data))
        requests.get(answer)
    except Exception as e:
        with open('error_log.txt', 'a') as f:
            f.write(str(e))
    return HttpResponse(status=200)
