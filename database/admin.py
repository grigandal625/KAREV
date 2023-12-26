from django.contrib import admin
from database import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = 'number', 'specialization'
    search_fields = 'number', 'specialization'


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = 'username', 'is_blocked'
    list_filter = 'is_blocked',
    search_fields = 'username',


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'fio', 'email', 'phone', 'account', 
    search_fields = 'fio', 'email', 'phone'


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = 'fio', 'email', 'phone', 'account', 
    search_fields = 'fio', 'email', 'phone'


@admin.register(models.Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = 'fio', 'email', 'univercity', 'post', 'access_level' 
    search_fields = 'fio', 'email', 'univercity', 'post',
    list_filter = 'access_level',


@admin.register(models.Discipline)
class DispciplineAdmin(admin.ModelAdmin):
    list_display = 'title',
    search_fields = 'title',


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = 'title', 'topic', 'discipline', 
    search_fields = 'title', 'topic',


@admin.register(models.TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = 'student', 'test', 'mark'
    search_fields = 'student__fio', 'test__title', 'mark'
