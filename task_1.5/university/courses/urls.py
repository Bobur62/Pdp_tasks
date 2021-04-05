from django.urls import path
from .views import *

urlpatterns = [
    # path('courses/<str:name>/', home)
    path('courses/', home),
    path('courses/speciality/', special, name='special_list'),
    path('courses/teacher/', teacher, name='teacher'),
    path('courses/subject/', subjects, name='subject'),
    path('courses/subjet/<int:pk>/', subject_detail, name='subject-detail'),
]
