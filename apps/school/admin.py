from django.contrib import admin

from apps.school.models import Student, Teacher, Grade, School


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'date_of_birth', 'grade', 'address', 'gender', 'photo')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'subject')
    list_display_links = ('phone_number',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
