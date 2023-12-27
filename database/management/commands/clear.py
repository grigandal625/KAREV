from django.core.management.base import BaseCommand, CommandError
from database.models import Account, Administrator, Discipline, Group, Test, Student, TestResult, Teacher






class Command(BaseCommand):
    help = "Clears database"

    def handle(self, *args, **options):
        all = [Account, Administrator, Discipline, Group, Test, Student, TestResult, Teacher]
        all.reverse()
        for m in all:
            m.objects.all().delete()
            print('DELETED', m.__name__)