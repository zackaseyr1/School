from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import School, TeacherProfile, StudentProfile, ParentProfile, StaffProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from django.utils import timezone


def home(request):
    # Get the current user's school profile
    try:
        school_profile = School.objects.get(administrator=request.user)
    except School.DoesNotExist:
        school_profile = None

    teacher_profiles = []
    student_profiles = []
    staff_profiles = []

    if school_profile:
        # Get the profiles associated with the school
        teacher_profiles = TeacherProfile.objects.filter(school=school_profile)
        student_profiles = StudentProfile.objects.filter(school=school_profile)
        staff_profiles = StaffProfile.objects.filter(school=school_profile)

    context = {
        'school_profile': school_profile,
        'teacher_profiles': teacher_profiles,
        'student_profiles': student_profiles,
        'staff_profiles': staff_profiles,
    }

    return render(request, 'home.html', context)

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the newly registered user
            authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, authenticated_user)
            # Redirect to the home page or any other desired page after successful registration
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register_user.html', {'form': form})


def create_school(request):
    if request.method == 'POST':
        form = SchoolRegistrationForm(request.POST)
        if form.is_valid():
            school = form.save(commit=False)
            # Set the administrator field to the currently logged-in user
            school.administrator = request.user
            school.save()
            return redirect('home')  # Redirect to your home page after successful registration
    else:
        form = SchoolRegistrationForm()
    return render(request, 'registration/create_school.html', {'form': form})


def generate_teacher_username(school_name):
    # Generate a unique username based on the school's name and a number
    base_username = school_name[:3].lower()  # Get the first 3 letters of the school name in lowercase
    count = 1
    while True:
        username = f"{base_username}{count}"
        if not User.objects.filter(username=username).exists():
            return username
        count += 1

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST)
        if form.is_valid():
            teacher_profile = form.save(commit=False)
            # Get the school associated with the administrator
            school = get_object_or_404(School, administrator=request.user)
            teacher_profile.school = school

            # Generate a unique username for the teacher
            teacher_username = generate_teacher_username(school.name)

            # Create a new user instance for the teacher
            teacher_user = User.objects.create(username=teacher_username)
            teacher_user.set_password('Zaka5577')  # Set a default password for the teacher
            teacher_user.save()

            teacher_profile.user = teacher_user  # Set the user for the teacher profile
            teacher_profile.save()

            # Redirect to the home page or any other desired page after successful registration
            return redirect('home')
    else:
        form = TeacherProfileForm()

    return render(request, 'registration/register_teacher.html', {'form': form})
# Similar views for other profile types (Student, Parent, Staff) will follow a similar pattern.


def generate_student_username(school_name):
    # Generate a unique username based on the school's name and the current year
    base_username = f"stud{timezone.now().year}"
    count = 1
    while True:
        username = f"{base_username}{count}"
        if not User.objects.filter(username=username).exists():
            return username
        count += 1

def register_student(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            student_profile = form.save(commit=False)
            # Get the school associated with the administrator
            school = get_object_or_404(School, administrator=request.user)
            student_profile.school = school

            # Generate a unique username for the student
            student_username = generate_student_username(school.name)

            # Create a new user instance for the student
            student_user = User.objects.create(username=student_username)
            student_user.set_password('Zaka5577')  # Set a default password for the student
            student_user.save()

            student_profile.user = student_user  # Set the user for the student profile
            student_profile.save()

            # Redirect to the home page or any other desired page after successful registration
            return redirect('home')
    else:
        form = StudentProfileForm()

    return render(request, 'registration/register_student.html', {'form': form})





def generate_staff_username(school_name):
    # Generate a unique username based on the school's name and the current year
    base_username = f"stuff{timezone.now().year}"
    count = 1
    while True:
        username = f"{base_username}{count}"
        if not User.objects.filter(username=username).exists():
            return username
        count += 1




def register_staff(request):
    if request.method == 'POST':
        form = StaffProfileForm(request.POST)
        if form.is_valid():
            staff_profile = form.save(commit=False)
            # Get the school associated with the administrator
            school = get_object_or_404(School, administrator=request.user)
            staff_profile.school = school

            # Generate a unique username for the staff
            staff_username = generate_staff_username(school.name)

            # Create a new user instance for the staff
            staff_user = User.objects.create(username=staff_username)
            staff_user.set_password('Zaka5577')  # Set a default password for the staff
            staff_user.save()

            staff_profile.user = staff_user  # Set the user for the staff profile
            staff_profile.save()

            # Redirect to the home page or any other desired page after successful registration
            return redirect('home')
    else:
        form = StaffProfileForm()

    return render(request, 'registration/register_staff.html', {'form': form})