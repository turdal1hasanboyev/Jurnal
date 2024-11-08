# Generated by Django 5.1.3 on 2024-11-06 14:28

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('grade', models.IntegerField(choices=[(1, '1-sinf'), (2, '2-sinf'), (3, '3-sinf'), (4, '4-sinf'), (5, '5-sinf'), (6, '6-sinf'), (7, '7-sinf'), (8, '8-sinf'), (9, '9-sinf'), (10, '10-sinf'), (11, '11-sinf')])),
                ('section', models.CharField(choices=[('A', 'A sinfi'), ('B', 'B sinfi'), ('C', 'C sinfi'), ('D', 'D sinfi')], max_length=1)),
            ],
            options={
                'verbose_name': 'Sinf',
                'verbose_name_plural': 'Sinflar',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=25, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('sinf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_subject', to='juornal.class')),
            ],
            options={
                'verbose_name': 'Fan',
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Ayol', 'Ayol'), ('Erkak', 'Erkak')], max_length=10)),
                ('image', models.ImageField(default='img/default.png', upload_to='teacher_images/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('sinf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='juornal.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='juornal.subject')),
            ],
            options={
                'verbose_name': "O'qituvchi",
                'verbose_name_plural': "O'qituvchilar",
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_teacher', to='juornal.teacher'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default='img/default.png', upload_to='student_images/')),
                ('gender', models.CharField(choices=[('Qiz Bola', 'Qiz Bola'), ("O'g'il Bola", "O'g'il Bola")], max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('sinf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='juornal.class')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to='juornal.teacher')),
            ],
            options={
                'verbose_name': 'Talaba',
                'verbose_name_plural': 'Talabalar',
            },
        ),
    ]
