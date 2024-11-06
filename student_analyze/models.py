from django.db import models

# Person Base


# region Gender
class Gender(models.Model):
    name = models.CharField(max_length=50, unique=True)
    prefix = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


# endregion


# region Person
class Person(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    birth_date = models.DateField()
    national_code = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return f"{self.gender.prefix} {self.first_name} {self.last_name}"


# endregion


# Global Attrs


# region ES
class EducationState(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


# endregion


# region EGd
class EducationGrade(models.Model):
    name = models.CharField(max_length=50, unique=True)
    educationstate = models.ForeignKey(EducationState, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


# endregion


# region EGp
class EducationGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    educationstate = models.ForeignKey(EducationState, on_delete=models.CASCADE)
    direct_use = models.BooleanField(default=True)
    generic_dependancies = models.ManyToManyField("self")

    def __str__(self) -> str:
        return self.name


# endregion


# region Lesson
class Lesson(models.Model):
    name = models.CharField(max_length=50, unique=True)
    educationgroup = models.ForeignKey(EducationGroup, on_delete=models.CASCADE)
    educationgrade = models.ForeignKey(EducationGrade, on_delete=models.CASCADE)
    grade_base_prerequisite = models.ManyToManyField("self")

    def __str__(self) -> str:
        return self.name


# endregion


# School-Base


# region School
class School(models.Model):
    name = models.CharField(max_length=50, unique=True)
    education_states = models.ManyToManyField(EducationState)
    education_groups = models.ManyToManyField(EducationGroup)

    def __str__(self) -> str:
        return self.name


# endregion


# region C-Room
class ClassRoom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


# endregion


# region Student
class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    education_grade = models.ForeignKey(EducationGrade, on_delete=models.CASCADE)
    education_group = models.ForeignKey(EducationGroup, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.gender.prefix} {self.first_name} {self.last_name}"


# endregion


# region Teacher
class Teacher(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.person.gender.prefix} {self.person.first_name} {self.person.last_name}"


# endregion


# region C-Group
class ClassGroup(models.Model):
    name = models.CharField(max_length=35, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    educationgrade = models.ForeignKey(EducationGrade, on_delete=models.CASCADE)
    educationgroup = models.ForeignKey(EducationGroup, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    students = models.ManyToManyField

    def __str__(self) -> str:
        return self.name(Student)


# endregion
