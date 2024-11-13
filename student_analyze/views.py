# Added for restframework and api's
from rest_framework.response import Response
from rest_framework.decorators import api_view
# importing serializers
from .api.serializers import (
    PersonSerializer,
    GenderSerializer,
    ESSerializer,
    EGdSerializer,
    EGpSerializer,
    LessonSerializer,
    SchoolSerializer,
    CRoomSerializer,
    StudentSerializer,
    TeacherSerializer,
    CGroupSerializer,
)

# after adding the GET and POST api functions (those dont need these)
from rest_framework import status


# -------------------------------------------

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
    ClassRoom,
    ClassGroup,
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

        case "croom":
            test = {"name__icontains": "h"}
            resault = list(ClassGroup.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

        case "cgroup":
            test = {"name__icontains": "h"}
            resault = list(ClassGroup.objects.all().filter(**params).values())
            return JsonResponse(resault, safe=False)

# -----------------------------------------------------
# region GET
@api_view(['GET'])
def get_model(request, the_model):
    model = model_resolver(the_model)

    item_list = model['obj'].objects.all()
    serializer = model['serializer'](item_list, many=True)
    return Response(serializer.data)

# endregion
    

# region POST
@api_view(['POST'])
def add_model(request, the_model):
    model = model_resolver(the_model)
    
    serializer = model['serializer'](data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# endregion 


# region DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def modify_model(request, the_model, pk):
    model = model_resolver(the_model)

    # first trying to find that specific person
    try:
        the_item = model['obj'].objects.get(pk=pk)
    except EducationState.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = model['serializer'](the_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # NOTE if we dont pass 'the_item', the .save() will create a new instance. we pass it so it would update the existing one
        serializer = model['serializer'](the_item, data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        the_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


# region model resolver
def model_resolver(model_name:str):
    the_model = {}
    match model_name:
        case "person":
            the_model['obj'] = Person
            the_model['serializer'] = PersonSerializer
            return the_model

        case "gender":
            the_model['obj'] = Gender
            the_model['serializer'] = GenderSerializer
            return the_model

        case "es":
            the_model['obj'] = EducationState
            the_model['serializer'] = ESSerializer
            return the_model

        case "egd":
            the_model['obj'] = EducationGrade
            the_model['serializer'] = EGdSerializer
            return the_model

        case "egp":
            the_model['obj'] = EducationGroup
            the_model['serializer'] = EGpSerializer
            return the_model

        case "lesson":
            the_model['obj'] = Lesson
            the_model['serializer'] = LessonSerializer 
            return the_model

        case "school":
            the_model['obj'] = School
            the_model['serializer'] = SchoolSerializer 
            return the_model

        case "student":
            the_model['obj'] = Student
            the_model['serializer'] = StudentSerializer
            return the_model

        case "teacher":
            the_model['obj'] = Teacher
            the_model['serializer'] = TeacherSerializer
            return the_model
        
        case "croom":
            the_model['obj'] = ClassRoom
            the_model['serializer'] = CRoomSerializer
            return the_model
        
        case "cgroup":
            the_model['obj'] = ClassGroup
            the_model['serializer'] = CGroupSerializer
            return the_model
