from django.urls import path
from .views import *

urlpatterns = [
    # path('courses/<str:name>/', home)
    path('', home),
    path('speciality/', special, name='special_list'),
    path('teacher/', teacher, name='teacher'),
    path('subject/', subjects, name='subject'),
    path('subjet/<int:pk>/', subject_detail, name='subject-detail'),
]
