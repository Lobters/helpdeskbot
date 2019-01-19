from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    data = json.loads(str(request.body.decode('UTF-8')))
    print(data['message']['text'])
    return HttpResponse(status=200)
