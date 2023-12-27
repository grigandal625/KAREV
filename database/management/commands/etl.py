from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from database.models import Account, Administrator, Discipline, Group, Test, Student, TestResult, Teacher
from django.db.models import ForeignKey
import random


ALL_MODELS = [Account, Administrator, Discipline, Group, Test, Student, TestResult, Teacher]


fake = Faker()

class Command(BaseCommand):
    help = "Fills database"

    def handle(self, *args, **options):
        for m in ALL_MODELS:
            for i in range(random.randint(50, 100)):
                unique_data = {}
                data = {}
                for field in m._meta.fields:
                    fm_map = {
                        'username': fake.email().split('@')[0],
                        'email': fake.email(),
                        'fio': fake.name(),
                        'password': fake.password(),
                        'Account.is_blocked': random.choice([True, False]),
                        'Administrator.univercity': 'NRNU MEPhI',
                        'Administrator.post': random.choice(['Engineer', 'Assistent', 'Senior Lecturer', 'Docent', 'Professor', 'Head of the Department', 'Dean']),
                        'Administrator.access_level': random.choice([Administrator.AccessLevelChoices.BLOCKING, Administrator.AccessLevelChoices.CHANGING, Administrator.AccessLevelChoices.FULL]),
                        'title': fake.sentence(),
                        'topic': fake.sentence(),
                        'Group.number': random.choice(['Б21-504', 'Б21-514', 'Б21-524', 'Б21-564', 'Б21-534', 'Б21-501']),
                        'Group.specialization': random.choice(['09.01.01', '09.03.04', '09.03.03', '09.02.03']),
                        'mark': random.randint(0, 100),
                        'phone': fake.phone_number()
                    }

                    key = f'{m.__name__}.{field.name}'
                    if key not in fm_map:
                        key = field.name
                    if key in fm_map:
                        if field._unique:
                            unique_data[field.name] = fm_map[key]
                        else:
                            data[field.name] = fm_map[key]
                    
                    if isinstance(field, ForeignKey):
                        data[field.name] = random.choice(field.related_model.objects.all())
                
                if not len(list(unique_data.keys())):
                    unique_data = data
                inst, _ = m.objects.get_or_create(**unique_data, defaults=data)
                print('CREATED' if _ else 'HAVE', m.__name__, inst)

        for admin in Administrator.objects.all():
            admin.manages.add(*random.sample(list(Account.objects.all()), random.randint(3, 10)))
        for student in Student.objects.all():
            student.learns.add(*random.sample(list(Discipline.objects.all()), random.randint(3, 10)))
        for teacher in Teacher.objects.all():
            teacher.teaches.add(*random.sample(list(Discipline.objects.all()), random.randint(3, 10)))