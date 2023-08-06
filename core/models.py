from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class School(models.Model):
    name = models.CharField(max_length=100)
    administrator_name = models.CharField(max_length=100)
    administrator_phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    administrator_email = models.EmailField()
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)  # Add the created_at field

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']  # Order by the latest created_at date

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-school__created_at']  # Order by the latest school's created_at date

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-school__created_at']  # Order by the latest school's created_at date

class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-school__created_at']  # Order by the latest school's created_at date

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-school__created_at']  # Order by the latest school's created_at date

