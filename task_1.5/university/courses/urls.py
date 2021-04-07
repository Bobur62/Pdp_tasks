from django.urls import path
from .views import *

urlpatterns = [
    # path('courses/<str:name>/', home)
    path('', home),
    path('speciality/', special, name='special_list'),
    path('speciality/create/', speciality_create, name='special-create'),
    path('teacher/', teacher, name='teacher'),
    path('subject/', subjects, name='subject'),
    path('subjet/<int:pk>/', subject_detail, name='subject-detail'),
    path('teacher/create/', teacher_create, name='teacher-create'),
    path('subject/create/', subject_create, name='subject-create'),
]
