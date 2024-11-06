# region Importing
from django.core.management.base import BaseCommand
from student_analyze.models import Person
from student_analyze import models

# for person faker
from datetime import datetime
import random

# endregion


# if i need to reset users, i have to creat super user again
# from django.contrib.auth import get_user_model
# User = get_user_model()
# User.objects.create_superuser(username = 'admin', password = '123')


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        # region clear
        models.Person.objects.all().delete()
        models.Gender.objects.all().delete()
        models.EducationState.objects.all().delete()
        models.EducationGrade.objects.all().delete()
        models.EducationGrade.objects.all().delete()
        models.Lesson.objects.all().delete()
        models.School.objects.all().delete()
        models.ClassRoom.objects.all().delete()
        models.Student.objects.all().delete()
        models.Teacher.objects.all().delete()
        models.ClassGroup.objects.all().delete()

        # endregion

        # region ES
        # EducationStates
        es_dict = {}
        es_dict["ps"] = models.EducationState.objects.create(name="Primary School")
        es_dict["hs1"] = models.EducationState.objects.create(name="High School 1st")
        es_dict["hs2"] = models.EducationState.objects.create(name="High School 2nd")
        es_dict["u"] = models.EducationState.objects.create(name="University")

        # data.es.item["ps"] = EducationState("Primary School")
        # data.es.item["hs1"] = EducationState("High School 1st")
        # data.es.item["hs2"] = EducationState("High School 2nd")
        # data.es.item["u"] = EducationState("University")

        # endregion

        # region EGd
        # EducationGrades
        egd_dict = {}
        egd_dict["1st"] = models.EducationGrade.objects.create(
            educationstate=es_dict["ps"], name="1st grade"
        )
        egd_dict["2nd"] = models.EducationGrade.objects.create(
            educationstate=es_dict["ps"], name="2nd grade"
        )
        egd_dict["3rd"] = models.EducationGrade.objects.create(
            educationstate=es_dict["ps"], name="3rd grade"
        )
        egd_dict["4th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["ps"], name="4th grade"
        )
        egd_dict["5th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["ps"], name="5th grade"
        )
        egd_dict["6th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["ps"], name="6th grade"
        )
        egd_dict["7th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["hs1"], name="7th grade"
        )
        egd_dict["8th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["hs1"], name="8th grade"
        )
        egd_dict["9th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["hs1"], name="9th grade"
        )
        egd_dict["10th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["hs2"], name="10th grade"
        )
        egd_dict["11th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["hs2"], name="11th grade"
        )
        egd_dict["12th"] = models.EducationGrade.objects.create(
            educationstate=es_dict["hs2"], name="12th grade"
        )
        egd_dict["bachelor"] = models.EducationGrade.objects.create(
            educationstate=es_dict["u"], name="Bachelor"
        )
        egd_dict["master"] = models.EducationGrade.objects.create(
            educationstate=es_dict["u"], name="Master"
        )
        egd_dict["phd"] = models.EducationGrade.objects.create(
            educationstate=es_dict["u"], name="Ph.D"
        )

        # endregion

        # region EGp
        # EducationGroups
        egp_dict = {}
        egp_dict["ps-general"] = models.EducationGroup.objects.create(
            educationstate=es_dict["ps"], name="Primary School - General"
        )

        egp_dict["hs1-general"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs1"], name="High School 1st - General"
        )

        egp_dict["hs2-general"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs2"],
            name="High School 2nd - General",
            direct_use=False,
        )
        egp_dict["hs2-riazi"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs2"], name="High School 2nd - Riazi Fizik"
        )
        egp_dict["hs2-tajrobi"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs2"], name="High School 2nd - Oloom Tajrobi"
        )
        egp_dict["hs2-ensani"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs2"], name="High School 2nd - Oloom Ensani"
        )
        egp_dict["hs2-zaban"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs2"], name="High School 2nd - Zaban haye Khareje"
        )
        egp_dict["hs2-honar"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs2"], name="High School 2nd - Honar"
        )
        egp_dict["hs2-fani"] = models.EducationGroup.objects.create(
            educationstate=es_dict["hs2"], name="High School 2nd - Fani Herfei"
        )

        egp_dict["u-general"] = models.EducationGroup.objects.create(
            educationstate=es_dict["u"], name="University - General"
        )
        egp_dict["u-mohandesi-computer"] = models.EducationGroup.objects.create(
            educationstate=es_dict["u"], name="University - Mohandesi Computer"
        )
        egp_dict["u-oloom-computer"] = models.EducationGroup.objects.create(
            educationstate=es_dict["u"], name="University - Oloom Computer"
        )
        egp_dict["u-mohandesi-bargh"] = models.EducationGroup.objects.create(
            educationstate=es_dict["u"], name="University - Mohandesi Bargh"
        )

        # endregion

        # region Lessons
        # Lessons
        lesson_dict = {}
        lesson_dict["ps-farsi-aval"] = models.Lesson.objects.create(
            name="Farsi Aval",
            educationgroup=egp_dict["ps-general"],
            educationgrade=egd_dict["1st"],
        )
        lesson_dict["ps-riazi-dovom"] = models.Lesson.objects.create(
            name="Riazi Dovom",
            educationgroup=egp_dict["ps-general"],
            educationgrade=egd_dict["2nd"],
        )
        lesson_dict["hs1-hendese-1"] = models.Lesson.objects.create(
            name="Hendese 1",
            educationgroup=egp_dict["hs1-general"],
            educationgrade=egd_dict["7th"],
        )
        lesson_dict["hs1-riazi-2"] = models.Lesson.objects.create(
            name="Riazi 2",
            educationgroup=egp_dict["hs1-general"],
            educationgrade=egd_dict["8th"],
        )

        # endregion

        # region Gender
        # Genders
        gender_dict = {}
        gender_dict["male"] = models.Gender.objects.create(name="male", prefix="Mr.")
        gender_dict["female"] = models.Gender.objects.create(
            name="female", prefix="Mrs."
        )

        # endregion

        # region School
        # School
        school_dict = {}
        school_dict["hesaraki"] = models.School(name="Dabestan Shahid Abas Hesaraki")
        school_dict["alameh"] = models.School(name="Dabirestan Alameh Tabatabai")
        school_dict["payamenoor"] = models.School(name="Daneshgah Payame Noor")

        # saving the schools so we could add the relations to them
        for item in school_dict:
            school_dict[item].save()

        school_dict["hesaraki"].education_states.add(es_dict["ps"])
        school_dict["hesaraki"].education_groups.add(egp_dict["ps-general"])
        school_dict["alameh"].education_states.add(es_dict["hs1"], es_dict["hs2"])
        school_dict["alameh"].education_groups.add(
            egp_dict["hs1-general"],
            egp_dict["hs2-general"],
            egp_dict["hs2-riazi"],
            egp_dict["hs2-tajrobi"],
        )
        school_dict["payamenoor"].education_states.add(es_dict["u"])
        school_dict["payamenoor"].education_groups.add(
            egp_dict["u-general"],
            egp_dict["u-mohandesi-bargh"],
            egp_dict["u-mohandesi-computer"],
            egp_dict["u-oloom-computer"],
        )

        # endregion

        # region C-Room
        # Classroom
        croom_dict = {}
        croom_dict["1-1"] = models.ClassRoom.objects.create(
            name="Aval 1-1", school=school_dict["hesaraki"]
        )
        croom_dict["1-2"] = models.ClassRoom.objects.create(
            name="Aval 1-2", school=school_dict["hesaraki"]
        )
        croom_dict["1-3"] = models.ClassRoom.objects.create(
            name="Aval 1-3", school=school_dict["hesaraki"]
        )
        croom_dict["2-1"] = models.ClassRoom.objects.create(
            name="Dovom 2-1", school=school_dict["hesaraki"]
        )
        croom_dict["2-2"] = models.ClassRoom.objects.create(
            name="Dovom 2-2", school=school_dict["hesaraki"]
        )
        croom_dict["2-3"] = models.ClassRoom.objects.create(
            name="Dovom 2-3", school=school_dict["hesaraki"]
        )
        croom_dict["3-1"] = models.ClassRoom.objects.create(
            name="Sevom 3-1", school=school_dict["hesaraki"]
        )
        croom_dict["3-2"] = models.ClassRoom.objects.create(
            name="Sevom 3-2", school=school_dict["hesaraki"]
        )
        croom_dict["3-3"] = models.ClassRoom.objects.create(
            name="Sevom 3-3", school=school_dict["hesaraki"]
        )
        croom_dict["4-1"] = models.ClassRoom.objects.create(
            name="chaharom 4-1", school=school_dict["hesaraki"]
        )
        croom_dict["4-2"] = models.ClassRoom.objects.create(
            name="Chaharom 4-2", school=school_dict["hesaraki"]
        )
        croom_dict["4-3"] = models.ClassRoom.objects.create(
            name="Chaharom 4-3", school=school_dict["hesaraki"]
        )
        croom_dict["5-1"] = models.ClassRoom.objects.create(
            name="Panjom 5-1", school=school_dict["hesaraki"]
        )
        croom_dict["5-2"] = models.ClassRoom.objects.create(
            name="Panjom 5-2", school=school_dict["hesaraki"]
        )
        croom_dict["5-3"] = models.ClassRoom.objects.create(
            name="Panjom 5-3", school=school_dict["hesaraki"]
        )
        croom_dict["6-1"] = models.ClassRoom.objects.create(
            name="Shishom 6-1", school=school_dict["hesaraki"]
        )
        croom_dict["6-2"] = models.ClassRoom.objects.create(
            name="Shishom 6-2", school=school_dict["hesaraki"]
        )
        croom_dict["6-3"] = models.ClassRoom.objects.create(
            name="Shishom 6-3", school=school_dict["hesaraki"]
        )
        croom_dict["kharazmi 1"] = models.ClassRoom.objects.create(
            name="Haftom kharazmi 1", school=school_dict["alameh"]
        )
        croom_dict["kharazmi 2"] = models.ClassRoom.objects.create(
            name="Haftom kharazmi 2", school=school_dict["alameh"]
        )
        croom_dict["kharazmi 3"] = models.ClassRoom.objects.create(
            name="Haftom kharazmi 3", school=school_dict["alameh"]
        )

        for i in range(200, 210):
            croom_dict[str(i)] = models.ClassRoom.objects.create(
                name=str(i), school=school_dict["payamenoor"]
            )

        # endregion

        # Adding Persons
        # Person
        person_dict = {}
        person_gen = fake_person(gender_dict, 25)

        for new_person in person_gen:
            person_dict[new_person.national_code] = new_person

        # endregion

        # region Student
        # Students
        # student_dict = {}
        # student_dict['ps-1'] = models.Student.objects.create(
        #     person=person_dict[''],
        #     school=school_dict[''],
        #     education_grade=egd_dict[''],
        #     education_group=egp_dict[''],
        # )

        # data.student.item["ps-1"] = data.school.item["hesaraki"].add_student(
        #     data.person.item[1], data.egd.item["1st"], data.egp.item["ps-general"]
        # )

        # data.student.item["ps-2"] = data.school.item["hesaraki"].add_student(
        #     data.person.item[2], data.egd.item["5th"], data.egp.item["ps-general"]
        # )

        # data.student.item["hs1-1"] = data.school.item["alameh"].add_student(
        #     data.person.item[3], data.egd.item["7th"], data.egp.item["hs1-general"]
        # )

        # data.student.item["hs1-2"] = data.school.item["alameh"].add_student(
        #     data.person.item[4], data.egd.item["9th"], data.egp.item["hs1-general"]
        # )

        # data.student.item["hs2-1"] = data.school.item["alameh"].add_student(
        #     data.person.item[5], data.egd.item["11th"], data.egp.item["hs2-riazi"]
        # )

        # data.student.item["hs2-2"] = data.school.item["alameh"].add_student(
        #     data.person.item[6], data.egd.item["12th"], data.egp.item["hs2-tajrobi"]
        # )

        # data.student.item["u-1"] = data.school.item["payamenoor"].add_student(
        #     data.person.item[7],
        #     data.egd.item["bachelor"],
        #     data.egp.item["u-mohandesi-computer"],
        # )

        # data.student.item["u-2"] = data.school.item["payamenoor"].add_student(
        #     data.person.item[8],
        #     data.egd.item["phd"],
        #     data.egp.item["u-oloom-computer"],
        # )

        # # endregion

        # # region Teacher
        # # Teachers
        # data.teacher.item["hesaraki-1"] = data.school.item["hesaraki"].add_teacher(
        #     data.person.item[11],
        #     data.lesson.item["ps-farsi-aval"],
        #     data.lesson.item["ps-riazi-dovom"],
        # )

        # data.teacher.item["alameh-1"] = data.school.item["alameh"].add_teacher(
        #     data.person.item[12],
        #     data.lesson.item["hs1-riazi-2"],
        # )

        # # endregion

        # # region C-Group
        # data.cg.item["hesaraki-1"] = data.school.item["hesaraki"].add_classgroup(
        #     data.egd.item["1st"],
        #     data.egp.item["ps-general"],
        #     data.teacher.item["hesaraki-1"],
        #     data.lesson.item["ps-farsi-aval"],
        #     [data.student.item["ps-1"]],
        # )

        # data.cg.item["hesaraki-2"] = data.school.item["hesaraki"].add_classgroup(
        #     data.egd.item["2nd"],
        #     data.egp.item["ps-general"],
        #     data.teacher.item["hesaraki-1"],
        #     data.lesson.item["ps-riazi-dovom"],
        # )

        # data.cg.item["alameh-1"] = data.school.item["alameh"].add_classgroup(
        #     data.egd.item["8th"],
        #     data.egp.item["hs1-general"],
        #     data.teacher.item["alameh-1"],
        #     data.lesson.item["hs1-riazi-2"],
        # )

        # # endregion
        self.stdout.write(self.style.SUCCESS("Successfully closed poll"))


# region Person Faker
def fake_person(gender_dict, count):
    national_code_counter = 1000
    for count in range(count):
        # TODO i should refactor this and create Names class and assign the gender attribute to it (i dont have enough time)
        fname_gender_list = (
            ("hossein", gender_dict["male"]),
            ("mohammad mahdi", gender_dict["male"]),
            ("reza", gender_dict["male"]),
            ("maryam", gender_dict["female"]),
            ("samira", gender_dict["female"]),
            ("fereshteh", gender_dict["female"]),
            ("eisa", gender_dict["female"]),
            ("peyman", gender_dict["male"]),
            ("mansore", gender_dict["female"]),
            ("elham", gender_dict["female"]),
            ("hasan", gender_dict["male"]),
            ("ali", gender_dict["male"]),
            ("Saeed", gender_dict["male"]),
            ("arash", gender_dict["male"]),
            ("hoorieh", gender_dict["female"]),
        )
        lname_list = (
            "mohammadi",
            "ramezani",
            "mamani",
            "bonab",
            "chakaneh",
            "rajabalian",
            "eisapoor",
            "nobakht",
            "zareiian_zadeh",
            "seyedrazi",
            "dalvand",
            "mohammadian",
            "mohammadian far",
            "mohammad zadeh",
            "pirhadi",
            "enayati",
            "nikravesh",
        )

        # Capitalizing the name parts
        fname_gender_list = tuple(
            (name[0].capitalize(), name[1]) for name in fname_gender_list
        )
        lname_list = tuple(name.capitalize() for name in lname_list)

        temp_fname_gender = random.choice(fname_gender_list)
        temp_first_name = temp_fname_gender[0]
        temp_last_name = random.choice(lname_list)
        temp_gender = temp_fname_gender[1]
        temp_birth_date = datetime(2001, 9, 11)
        national_code_counter += 1

        yield models.Person.objects.create(
            gender=temp_gender,
            first_name=temp_first_name,
            last_name=temp_last_name,
            birth_date=temp_birth_date,
            national_code=national_code_counter,
        )
        # yield Person(
        #     temp_first_name,
        #     temp_last_name,
        #     temp_gender,
        #     temp_birth_date,
        # )


# endregion
