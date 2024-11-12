from rest_framework import serializers
from student_analyze.models import (
    Person,
    Gender, 
    EducationState,
    EducationGrade,
    EducationGroup,
    Lesson,
    School,
    ClassRoom,
    Student,
    Teacher,
    ClassGroup,
)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class ESSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationState
        fields = '__all__'

class EGdSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationGrade
        fields = '__all__'

class EGpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationGroup
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class CRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = '__all__'