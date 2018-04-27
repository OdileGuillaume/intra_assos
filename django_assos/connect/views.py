
from django.shortcuts import render


def demande_reunion(request):
    return render(
        request,
        'demande_reunion.html',
    )


def accueil(request):
    return render(
        request,
        'accueil.html',
    )


def index(request):
    return render(
        request,
        'index.html',
    )
