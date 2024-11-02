from django.contrib import admin
from .models import (
    Gender,
    Person,
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


admin.site.register(Gender)
admin.site.register(Person)
admin.site.register(EducationState)
admin.site.register(EducationGrade)
admin.site.register(EducationGroup)
admin.site.register(Lesson)
admin.site.register(School)
admin.site.register(ClassRoom)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ClassGroup)
