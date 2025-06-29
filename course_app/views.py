from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Filiere, ClassRoom

def dashboard(request):
    courses = Course.objects.all()
    filieres = Filiere.objects.all()
    classrooms = ClassRoom.objects.all()
    return render(request, 'dashboard.html', {
        'courses': courses,
        'filieres': filieres,
        'classrooms': classrooms
    })

def add_course(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        filiere_id = request.POST.get('filiere')
        salle_id = request.POST.get('salle')

        if nom and description and filiere_id and salle_id:
            filiere = get_object_or_404(Filiere, pk=filiere_id)
            salle = get_object_or_404(ClassRoom, pk=salle_id)
            Course.objects.create(
                nom=nom,
                description=description,
                filiere=filiere,
                salle=salle
            )
            return redirect('dashboard')
        else:
            error = "Tous les champs sont obligatoires."
            filieres = Filiere.objects.all()
            salles = ClassRoom.objects.all()
            return render(request, 'add_course.html', {
                'error': error,
                'filieres': filieres,
                'salles': salles,
                'nom': nom,
                'description': description,
                'filiere_id': filiere_id,
                'salle_id': salle_id,
            })

    else:
        filieres = Filiere.objects.all()
        salles = ClassRoom.objects.all()
        return render(request, 'add_course.html', {
            'filieres': filieres,
            'salles': salles,
        })

# Ajoute aussi les fonctions add_filiere et add_classroom si besoin

def add_filiere(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        if nom:
            Filiere.objects.create(nom=nom)
            return redirect('dashboard')
        else:
            error = "Le nom de la filière est obligatoire."
            return render(request, 'add_filiere.html', {'error': error, 'nom': nom})
    return render(request, 'add_filiere.html')

def add_classroom(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        capacite = request.POST.get('capacite')
        if nom and capacite:
            try:
                capacite_int = int(capacite)
                ClassRoom.objects.create(nom=nom, capacite=capacite_int)
                return redirect('dashboard')
            except ValueError:
                error = "La capacité doit être un nombre entier."
                return render(request, 'add_classroom.html', {'error': error, 'nom': nom, 'capacite': capacite})
        else:
            error = "Tous les champs sont obligatoires."
            return render(request, 'add_classroom.html', {'error': error, 'nom': nom, 'capacite': capacite})
    return render(request, 'add_classroom.html')

