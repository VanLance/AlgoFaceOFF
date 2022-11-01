from django.http import HttpResponse
from django.template import loader

from .models import Problem

def index(request):
    template = loader.get_template('battles/index.html')
    context={"index": "Landing Page"}
    return HttpResponse(template.render(context, request))

def algo(request):
    # response = requets.get(apiURL)
    question = Problem.objects.first()
    template = loader.get_template('battles/algo.html')
    context = {'question':question}
    return HttpResponse(template.render(context,request))

