from django.shortcuts import render, HttpResponse

# for json response
from django.http import JsonResponse

# using models
from .models import (
    Person,
    Gender,
    EducationGrade,
    EducationGroup,
    EducationState,
    Lesson,
    School,
    Student,
    Teacher,
)

# # importin json to work with it
# import json
# json.loads()      # convert to python
# json.dumps()      # convert to json


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
# def get_all_person(request):
#     data = list(Person.objects.all())
#     the_dict = {"a": 1, "b": 2, "c": 3}

#     return JsonResponse(the_dict)


def testing(request):
    resault = {"a": [1, 2, 3, 4], "b": [1, 3, 5], "c": [2, 4, 6], "d": [11], "e": 6}
    # resault = json.dumps(resault)

    return JsonResponse(resault)


def contactinside(request, id, test):
    return HttpResponse(id + test + " hello welcome to this page")


# ----------------------------


def show(request, the_model, conditions):
    # getting the conditions as something like: "name_contains_h,id=1"
    # and then making it like: ["name_contains_h", "id=1"]
    str_filters = conditions.split(",")
    params = {}

    for condition in str_filters:
        # and lastly after some changes on each item and setting: {"name__contains": "h", "id":"1"}
        # TODO validating the count of each seperator to be one
        if condition == "all":
            pass
        elif (sep := "=") in condition:
            params.__setitem__(*condition.split(sep))

        elif (sep := "_c_") in condition:
            temp = condition.split(sep)
            temp[0] += "__contains"
            params[temp[0]] = temp[1]

    match the_model:
        case "person":
            test = {"name__icontains": "h"}
            resault = list(Person.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "gender":
            test = {"name__icontains": "h"}
            resault = list(Gender.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "es":
            test = {"name__icontains": "h"}
            resault = list(EducationState.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "egd":
            test = {"name__icontains": "h"}
            resault = list(EducationGrade.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "egp":
            test = {"name__icontains": "h"}
            resault = list(EducationGroup.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "lesson":
            test = {"name__icontains": "h"}
            resault = list(Lesson.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "school":
            test = {"name__icontains": "h"}
            resault = list(School.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "student":
            test = {"name__icontains": "h"}
            resault = list(Student.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "teacher":
            test = {"name__icontains": "h"}
            resault = list(Teacher.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)
