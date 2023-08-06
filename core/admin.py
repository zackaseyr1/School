
from django.contrib import admin
from .models import School, TeacherProfile, StudentProfile, ParentProfile, StaffProfile

admin.site.register(School)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
admin.site.register(StaffProfile)
