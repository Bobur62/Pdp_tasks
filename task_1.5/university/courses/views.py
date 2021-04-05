from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Speciality, Teacher, Subject


# task1.7_2
# def home(request, name):
# return HttpResponse(f'Hello {name}')


def home(request):
    name = request.GET.get('name', 'Django')
    return HttpResponse(f'Hello {name}')


# task1.7-5
def special(request):
    special_list = Speciality.objects.all()
    return render(request, 'courses/special_list.html', {'special_list': special_list})


# task1.7-6
def teacher(request):
    name = request.GET.get('search')
    if not name:
        teachers_list = Teacher.objects.all()
    else:
        teachers_list = Teacher.objects.filter(first_name__icontains=name)

    return render(request, 'courses/teacher.html', {'teachers': teachers_list})


def subjects(request):
    subject = Subject.objects.all()
    return render(request, 'courses/subjects.html', {'subjects': subject})


def subject_detail(request, pk):
    subject = Subject.objects.get(pk=pk)
    special = subject.speciality.all()
    teacher = subject.teacher.all()
    return render(request, 'courses/subject_detail.html', {'subject': subject, 'special': special, 'teacher': teacher})
