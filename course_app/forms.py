from django import forms
from .models import Course, Filiere, ClassRoom

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['nom', 'description', 'filiere', 'salle']

class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['nom']

class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['nom', 'capacite']
