from rest_framework import serializers
from models import (
    Person,
    Gender, 
    EducationGrade,
    EducationGroup,
    EducationState,
    Lesson,
    School,
    ClassRoom,
    Student,
    Teacher,
    ClassGroup,
)

class Serializer(serializers.ModelSerializer):
    pass