from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Programmers. Ready Fight.")

def land(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "../index.html")