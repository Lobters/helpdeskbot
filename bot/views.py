from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    with open('requests.txt', 'a') as f:
        f.write(str(request.body))
    return HttpResponse(True)
