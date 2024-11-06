from django.contrib import admin
from .models import Class, Subject, Teacher, Student


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = (
        'id',
        'grade',
        'section',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'grade',
        'section',
    )
    list_filter = (
        'is_active',
        'grade',
        'section',
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'sinf',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_active',
        'name',
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'sinf',
        'subject',
        'gender',
        'image',
        'birth_date',
        'age',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'age',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = (
        'is_active',
        'first_name',
        'last_name',
        'sinf',
        'subject',
        'gender',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'teacher',
        'sinf',
        'gender',
        'image',
        'birth_date',
        'age',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'age',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = (
        'is_active',
        'first_name',
        'last_name',
        'teacher',
        'sinf',
        'gender',
    )