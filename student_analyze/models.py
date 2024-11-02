from django.db import models

# Person Base


class Gender(models.Model):
    name = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)


class Person(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    birth_date = models.DateField()
    national_code = models.IntegerField(unique=True)


# Global Attrs
class EducationState(models.Model):
    name = models.CharField(max_length=50)


class EducationGrade(models.Model):
    name = models.CharField(max_length=50)
    educationstate = models.ForeignKey(EducationState, on_delete=models.CASCADE)


class EducationGroup(models.Model):
    name = models.CharField(max_length=50)
    educationstate = models.ForeignKey(EducationState, on_delete=models.CASCADE)
    direct_use = models.BooleanField()
    generic_dependancies = models.ManyToManyField("self")


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    educationgroup = models.ForeignKey(EducationGroup, on_delete=models.CASCADE)
    educationgrade = models.ForeignKey(EducationGrade, on_delete=models.CASCADE)
    grade_base_prerequisite = models.ManyToManyField("self")


# School-Base
class School(models.Model):
    name = models.CharField(max_length=50)
    education_states = models.ForeignKey(EducationState, on_delete=models.CASCADE)
    education_groups = models.ForeignKey(EducationGroup, on_delete=models.CASCADE)


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    education_grade = models.ForeignKey(EducationGrade, on_delete=models.CASCADE)
    education_group = models.ForeignKey(EducationGroup, on_delete=models.CASCADE)


class Teacher(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class ClassGroup(models.Model):
    name = models.CharField(max_length=35)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    educationgrade = models.ForeignKey(EducationGrade, on_delete=models.CASCADE)
    educationgroup = models.ForeignKey(EducationGroup, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
