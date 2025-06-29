from django import forms
from .models import Course, Filiere, ClassRoom

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'filiere', 'date']

class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['name']

class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['name', 'capacity']