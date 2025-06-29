from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_filiere/', views.add_filiere, name='add_filiere'),
    path('add_classroom/', views.add_classroom, name='add_classroom'),
]