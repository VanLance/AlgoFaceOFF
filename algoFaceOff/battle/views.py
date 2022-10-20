from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Planet, Time to battle')