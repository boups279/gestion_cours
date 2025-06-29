from django.shortcuts import render, redirect
from .forms import CourseForm, FiliereForm, ClassRoomForm
from .models import Course, Filiere, ClassRoom

def dashboard(request):
    courses = Course.objects.all()
    filieres = Filiere.objects.all()
    classrooms = ClassRoom.objects.all()
    return render(request, 'dashboard.html', {'courses': courses, 'filieres': filieres, 'classrooms': classrooms})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def add_filiere(request):
    if request.method == 'POST':
        form = FiliereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FiliereForm()
    return render(request, 'add_filiere.html', {'form': form})

def add_classroom(request):
    if request.method == 'POST':
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClassRoomForm()
    return render(request, 'add_classroom.html', {'form': form})