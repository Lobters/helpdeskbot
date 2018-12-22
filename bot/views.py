from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    jsonData = json.loads(str(request.body.decode('UTF-8')))
    with open('test_requests.txt', 'a') as f:
        print(type(jsonData))
    return HttpResponse(status=200)
