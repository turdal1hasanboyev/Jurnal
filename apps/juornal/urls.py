from django.urls import path
from .views import home_view, class_list_view, subject_list, teacher_list, student_list


urlpatterns = [
    path('', home_view, name='home'),
    path('classes/', class_list_view, name='class_list'),
    path('subjects/', subject_list, name='subject_list'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('students/', student_list, name='student_list'),
]