from django.db import models
from ..common.models import BaseModel
from ckeditor.fields import RichTextField
from datetime import date


class Class(BaseModel):
    GRADE_CHOICES = [
        (1, '1-sinf'),
        (2, '2-sinf'),
        (3, '3-sinf'),
        (4, '4-sinf'),
        (5, '5-sinf'),
        (6, '6-sinf'),
        (7, '7-sinf'),
        (8, '8-sinf'),
        (9, '9-sinf'),
        (10, '10-sinf'),
        (11, '11-sinf'),
    ]
    SECTION_CHOICES = [
        ('A', 'A sinfi'),
        ('B', 'B sinfi'),
        ('C', 'C sinfi'),
        ('D', 'D sinfi'),
    ]
    grade = models.IntegerField(choices=GRADE_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)

    def __str__(self):
        return f"{self.grade} {self.section}"

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"


class Subject(BaseModel):
    name = models.CharField(max_length=25, unique=True)
    description = RichTextField(null=True, blank=True)
    sinf = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_subject')

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Teacher(BaseModel):
    GENDER = (
        ('Ayol', ('Ayol')),
        ('Erkak', ('Erkak')),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sinf = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_teacher', null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subjects")
    gender = models.CharField(max_length=10, choices=GENDER)
    image = models.ImageField(upload_to='teacher_images/', default='img/default.png')
    description = RichTextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def age(self):
        if not isinstance(self.birth_date, date):
            return None
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.get_full_name()} - {self.subject}"
    
    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"


class Student(BaseModel):
    GENDER = (
        ('Qiz Bola', ('Qiz Bola')),
        ("O'g'il Bola", ("O'g'il Bola"))
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='student_teacher', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = RichTextField(null=True, blank=True)
    sinf = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='student_class')
    image = models.ImageField(upload_to='student_images/', default='img/default.png')
    gender = models.CharField(max_length=20, choices=GENDER)
    birth_date = models.DateField(null=True, blank=True)

    def age(self):
        if not isinstance(self.birth_date, date):
            return None
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.get_full_name()}-{self.sinf}"
    
    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"