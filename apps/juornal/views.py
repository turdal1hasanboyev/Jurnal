from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Class, Subject, Teacher, Student


@login_required
def home_view(request):
    return render(request, "home.html")

def class_list_view(request):
    classes = Class.objects.all()
    data = []

    for cls in classes:
        student_count = cls.student_class.count()
        teacher = cls.class_subject.first().subjects.first() if cls.class_subject.exists() else None
        data.append({
            'class': cls,
            'student_count': student_count,
            'teacher': teacher,
        })

    return render(request, 'class_list.html', {'data': data})

def subject_list(request):
    subjects = Subject.objects.all()

    return render(request, 'subject_list.html', {'subjects': subjects})

def teacher_list(request):
    teachers = Teacher.objects.all()

    return render(request, 'teacher_list.html', {'teachers': teachers})

def student_list(request):
    students = Student.objects.all()
    
    return render(request, 'student_list.html', {'students': students})