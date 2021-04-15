from django.contrib import admin
from .models import Speciality, Teacher, Subject


# admin.site.register(Speciality)
# admin.site.register(Teacher)
# admin.site.register(Subject)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active',)
    search_fields = ('name', 'code',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'degree',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('degree',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    autocomplete_fields = ['speciality', 'teacher']
    search_fields = ('name',)
