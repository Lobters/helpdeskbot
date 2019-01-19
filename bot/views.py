import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from answer import make_answer


@csrf_exempt
def index(request):
    data = json.loads(str(request.body.decode('UTF-8')))
    answer = make_answer(data)
    requests.get(answer)
    return HttpResponse(status=200)
