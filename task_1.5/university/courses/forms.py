from django import forms
from django.forms import ModelForm
from .models import Teacher, Subject


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=250)
    code = forms.IntegerField(min_value=1000)


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['last_name', 'first_name', 'degree']


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
