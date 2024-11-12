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
    match the_model:
        case "person":
            item_list = Person.objects.all()
            serializer = PersonSerializer(item_list, many=True)
            return Response(serializer.data)

        case "gender":
            item_list = Gender.objects.all()
            serializer = GenderSerializer(item_list, many=True)
            return Response(serializer.data)

        case "es":
            item_list = EducationState.objects.all()
            serializer = ESSerializer(item_list, many=True)
            return Response(serializer.data)

        case "egd":
            item_list = EducationGrade.objects.all()
            serializer = EGdSerializer(item_list, many=True)
            return Response(serializer.data)

        case "egp":
            item_list = EducationGroup.objects.all()
            serializer = EGpSerializer(item_list, many=True)
            return Response(serializer.data)

        case "lesson":
            item_list = Lesson.objects.all()
            serializer = LessonSerializer(item_list, many=True)
            return Response(serializer.data)

        case "school":
            item_list = School.objects.all()
            serializer = SchoolSerializer(item_list, many=True)
            return Response(serializer.data)

        case "student":
            item_list = Student.objects.all()
            serializer = StudentSerializer(item_list, many=True)
            return Response(serializer.data)

        case "teacher":
            item_list = Teacher.objects.all()
            serializer = TeacherSerializer(item_list, many=True)
            return Response(serializer.data)
        
        case "croom":
            item_list = ClassRoom.objects.all()
            serializer = CRoomSerializer(item_list, many=True)
            return Response(serializer.data)
        
        case "cgroup":
            item_list = ClassGroup.objects.all()
            serializer = CGroupSerializer(item_list, many=True)
            return Response(serializer.data)

# endregion
    

# region POST
@api_view(['POST'])
def add_model(request, the_model):
    match the_model:
        case "person":
            serializer = PersonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "gender":
            serializer = GenderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "es":
            serializer = ESSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "egd":
            serializer = EGdSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "egp":
            serializer = EGpSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "lesson":
            serializer = LessonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "school":
            serializer = SchoolSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "student":
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case "teacher":
            serializer = TeacherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        case "croom":
            serializer = CRoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        case "cgroup":
            serializer = CGroupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# endregion 


# region DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def modify_model(request, pk):
    # first trying to find that specific person
    try:
        the_es = EducationState.objects.get(pk=pk)
    except EducationState.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ESSerializer(the_es)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ESSerializer(the_es, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
        
    elif request.method == 'DELETE':
        the_es.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    



