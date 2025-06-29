# from django.contrib import admin
# from django.urls import path
# from django.http import HttpResponse

# def accueil(request):
#     return HttpResponse("Bienvenue dans gestion_cours !")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', accueil),
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course_app.urls')),  # On inclut les urls de course_app
]

