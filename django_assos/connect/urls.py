from django.urls import path
from . import views


urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('demande_reunion', views.demande_reunion, name='demande_reunion'),
    path('index', views.index, name='index'),
    path('', views.accueil, name='accueil'),
]
