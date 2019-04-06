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
    raw = request.body.decode('utf-8')
    logging.info(raw)
    return HttpResponse(status=200)
