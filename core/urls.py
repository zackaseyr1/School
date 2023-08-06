from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_school/', views.create_school, name='create_school'),
    path('register_user/', views.register_user, name='register_user'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('register_student/', views.register_student, name='register_student'),
    path('register_staff/', views.register_staff, name='register_staff'),


    # Add other URL patterns for your views if needed
]
