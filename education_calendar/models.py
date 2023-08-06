from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import School, TeacherProfile, StudentProfile, StaffProfile, ParentProfile

class Year(models.Model):
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
   # Add other fields as needed

    def __str__(self):
        return f"{self.start_year}-{self.end_year}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(TeacherProfile, related_name='taught_subjects')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
   # Add other fields as needed

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return self.name

class StudentClass(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='enrolled_classes')
    class_info = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students_enrolled')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return f"{self.student.full_name} - {self.class_info.name}"

class EducationEvent(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
