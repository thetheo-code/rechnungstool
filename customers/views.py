from django.shortcuts import render
from config.settings import MENU_ITEMS

URL_KUNDENLISTE = "list.html"

def kundenListe(request):
    items = {"menu_items": MENU_ITEMS}

    for item in items:
        item['active'] = request.path.startswith(item['link'])

    return render(request, URL_KUNDENLISTE, items)
