from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import School, TeacherProfile, StudentProfile, ParentProfile, StaffProfile
from django.contrib.auth.models import User




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        # You can add any additional fields for the user registration form if needed.


class SchoolRegistrationForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'administrator_name', 'administrator_phone_number', 'location', 'administrator_email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'School Name'
        self.fields['administrator_name'].label = 'Administrator Name'
        self.fields['administrator_phone_number'].label = 'Administrator Phone Number'
        self.fields['location'].label = 'Location'
        self.fields['administrator_email'].label = 'Administrator Email'


class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['full_name', 'date_of_birth']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'date_of_birth']

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = ['full_name', 'date_of_birth']

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['full_name', 'date_of_birth']
