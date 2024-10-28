from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.profil_umum, name='profil_umum'),
    path('informasi-kontak/', views.informasi_kontak, name='informasi_kontak'),
    path('kemampuan/', views.kemampuan, name='kemampuan'),
    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('pengalaman/', views.pengalaman, name='pengalaman'),
    path('ALL/', views.ALL, name='ALL'),
]
