from django import forms
from .models import User, Faculty, Course, Professor

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty

        fields = ['name', 'field']
        
class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = ['title', 'professor', 'time', 'place', 'sem']
        
class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor

        fields = ['name', 'faculty']
