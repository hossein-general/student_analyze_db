from django.shortcuts import render, HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse('say hello 1')

def say_hello2(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html', {})
