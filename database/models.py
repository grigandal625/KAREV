from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Account(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name='имя пользователя')
    password = models.CharField(max_length=255, verbose_name='пароль')
    is_blocked = models.BooleanField(default=False, verbose_name='заблокирован?')
    
    class Meta:
        db_table = 'account'
        verbose_name = 'личный кабинет'
        verbose_name_plural = 'личные кабинеты'

    def __str__(self) -> str:
        return self.username


class Administrator(models.Model):
    class AccessLevelChoices(models.IntegerChoices):
        BLOCKING = 1, 'блокирование'
        CHANGING = 2, 'изменение'
        FULL = 3, 'полный доступ'

    fio = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(max_length=255, verbose_name='почта')
    univercity = models.CharField(max_length=255, verbose_name='университет')
    post = models.CharField(max_length=255, verbose_name='должность')
    access_level = models.IntegerField(choices=AccessLevelChoices.choices, verbose_name='уровень доступа')
    manages = models.ManyToManyField(Account, verbose_name='управляет', related_name='managed_by')

    class Meta:
        db_table = 'administrator'
        verbose_name = 'администратор'
        verbose_name_plural = 'администраторы'

    def __str__(self) -> str:
        return f'{self.post} {self.fio}'


class Discipline(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')

    class Meta:
        db_table = 'discipline'
        verbose_name = 'дисциплина'
        verbose_name_plural = 'дисциплины'

    def __str__(self) -> str:
        return self.title


class Group(models.Model):
    number = models.CharField(max_length=255, unique=True, verbose_name='номер')
    specialization = models.CharField(max_length=255, verbose_name='специальность')

    class Meta:
        db_table = 'group'
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self) -> str:
        return self.number


class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    topic = models.CharField(max_length=255, verbose_name='тема')
    discipline = models.ForeignKey(Discipline, on_delete=models.RESTRICT, verbose_name='дисциплина', related_name='tests')

    class Meta:
        db_table = 'test'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self) -> str:
        return self.title


class Student(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(max_length=255, verbose_name='почта')
    phone = models.CharField(max_length=255, verbose_name='номер телефона')
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, verbose_name="личный кабинет", related_name="students")    
    learns = models.ManyToManyField(Discipline, verbose_name='изучает', related_name="students")

    class Meta:
        db_table = 'student'
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self) -> str:
        return self.fio
    

class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='студент', related_name='results')
    test = models.ForeignKey(Test, on_delete=models.RESTRICT, verbose_name='тест', related_name='results')
    mark = models.IntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        db_table = 'test_result'
        verbose_name = 'результат теста'
        verbose_name_plural = 'результаты тестов'

    def __str__(self) -> str:
        return f'{self.student} - {self.test}: {self.mark}'


class Teacher(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(max_length=255, verbose_name='почта')
    phone = models.CharField(max_length=255, verbose_name='номер телефона')
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, verbose_name="личный кабинет", related_name="teachers")    
    teaches = models.ManyToManyField(Discipline, verbose_name='преподает', related_name="teachers")

    class Meta:
        db_table = 'teacher'
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'

    def __str__(self) -> str:
        return self.fio
        