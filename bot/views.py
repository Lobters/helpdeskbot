from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    with open('requests.txt', 'a') as f:
        f.write(str(request.body) + '')
    return HttpResponse(status=200)
