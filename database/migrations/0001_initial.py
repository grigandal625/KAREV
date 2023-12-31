# Generated by Django 5.0 on 2023-12-26 20:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='имя пользователя')),
                ('password', models.CharField(max_length=255, verbose_name='пароль')),
                ('is_blocked', models.BooleanField(default=False, verbose_name='заблокирован?')),
            ],
            options={
                'verbose_name': 'личный кабинет',
                'verbose_name_plural': 'личные кабинеты',
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=255, verbose_name='почта')),
                ('univercity', models.CharField(max_length=255, verbose_name='университет')),
                ('post', models.CharField(max_length=255, verbose_name='должность')),
                ('access_level', models.IntegerField(choices=[(1, 'блокирование'), (2, 'изменение'), (3, 'полный доступ')], verbose_name='уровень доступа')),
            ],
            options={
                'verbose_name': 'администратор',
                'verbose_name_plural': 'администраторы',
                'db_table': 'administrator',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'дисциплина',
                'verbose_name_plural': 'дисциплины',
                'db_table': 'discipline',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, unique=True, verbose_name='номер')),
                ('specialization', models.CharField(max_length=255, verbose_name='специальность')),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=255, verbose_name='почта')),
                ('phone', models.CharField(max_length=255, verbose_name='номер телефона')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='students', to='database.account', verbose_name='личный кабинет')),
                ('learns', models.ManyToManyField(related_name='students', to='database.discipline', verbose_name='изучает')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=255, verbose_name='почта')),
                ('phone', models.CharField(max_length=255, verbose_name='номер телефона')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='teachers', to='database.account', verbose_name='личный кабинет')),
                ('teaches', models.ManyToManyField(related_name='teachers', to='database.discipline', verbose_name='преподает')),
            ],
            options={
                'verbose_name': 'преподаватель',
                'verbose_name_plural': 'преподаватели',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('topic', models.CharField(max_length=255, verbose_name='тема')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tests', to='database.discipline', verbose_name='дисциплина')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
                'db_table': 'test',
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='database.student', verbose_name='студент')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='results', to='database.test', verbose_name='тест')),
            ],
            options={
                'verbose_name': 'результат теста',
                'verbose_name_plural': 'результаты тестов',
                'db_table': 'test_result',
            },
        ),
    ]
