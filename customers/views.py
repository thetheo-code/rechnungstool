from django.shortcuts import render

URL_KUNDENLISTE = "list.html"

def kundenListe(request):
    return render(request, URL_KUNDENLISTE)
