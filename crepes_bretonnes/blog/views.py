#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def view_article(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article #{0} !".format(id_article)    
    )

def list_articles(request, year, month):
    """
    Vue qui affiche un article selon le mois et l'annee de publication
    Apres la requête elle prend l'année et le mois en parametres 
    supplémentaires
    """
    return HttpResponse(
        "Vous avez demandé l'article qui a été publié pendant le mois {mois}"\
        " l'année {annee}".format(mois=month, annee=year)
    )

def date_actuelle(request):
    """
    Méthode qui renvoie le template qui affiche l'heure en utilisant la 
    méthode render 
    """
    return render(request, 'blog/date.html', { 'date':datetime.now()})

def additionne(request, nombre1 , nombre2 ):
    """
    Methode qui renvoie le template affichant l'addition 
    de deux nombres et qui prend deux nombres en parametres
    """
    total = int(nombre1) + int(nombre2);
    return render( request, 'blog/addition.html', locals())