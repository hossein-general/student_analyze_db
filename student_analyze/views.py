from django.shortcuts import render, HttpResponse

# for json response
from django.http import JsonResponse

# using models
from .models import Person

# Create your views here.


# region Test
def say_hello(request):
    return HttpResponse("say hello 1")


def say_hello2(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html", {})


def test(request):
    return JsonResponse({"title": 1})


# endregion


# region Queries
def get_all_person(request):
    data = list(Person.objects.all())
    the_dict = {}
    
    return JsonResponse(data, safe=False)
