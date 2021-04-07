from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views import View
from django.views.generic import CreateView

from .models import Speciality, Teacher, Subject
from .forms import SpecialityForm, TeacherForm, SubjectForm


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


def speciality_create(request):
    if request.method == 'GET':
        form = SpecialityForm
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            spec = Speciality.objects.create(
                name=data['name'],
                code=data['code'],
            )
            special_list = Speciality.objects.all()
            return render(request, 'courses/special_list.html', {'special_list': special_list})
    return render(request, 'courses/special_create.html', {'form': form})


def teacher_create(request):
    if request.method == 'GET':
        form = TeacherForm
    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            teach = Teacher.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                degree=data['degree']
            )
    return render(request, 'courses/teacher_create.html', {'form': form})


def subject_create(request):
    if request.method == 'GET':
        form = SubjectForm
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('special_list')
        else:
            form = SubjectForm()
    return render(request, 'courses/subject_create.html', {'form': form})
