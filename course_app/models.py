
# # Create your models here.
# from django.db import models

# class Course(models.Model):
#     nom = models.CharField(max_length=100)
#     description = models.TextField()
#     # ...

# class Filiere(models.Model):
#     nom = models.CharField(max_length=100)
#     # ...

# class ClassRoom(models.Model):
#     nom = models.CharField(max_length=100)
#     capacite = models.IntegerField()
#     # ...

from django.db import models

class Filiere(models.Model):
    nom = models.CharField(max_length=100)

class ClassRoom(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.IntegerField()

class Course(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    salle = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
