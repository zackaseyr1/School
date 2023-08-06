from django.contrib import admin
from .models import Year, Subject, Class, StudentClass, EducationEvent

admin.site.register(Year)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(StudentClass)
admin.site.register(EducationEvent)