
from django.shortcuts import render


def index(request):

    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    """
    return HttpResponse(

        <h1>Bienvenue sur mon blog !</h1>

        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>

    )"""
    return render(
        request,
        'index.html',
    )
