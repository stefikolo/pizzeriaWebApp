from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def promocje(request):
    return render(request, 'promocje.html')


def lokale(request):
    return render(request, 'lokale.html')


def o_firmie(request):
    return render(request, 'o_firmie.html')


def dzieje_sie(request):
    return render(request, 'dzieje_sie.html')


def franczyza(request):
    return render(request, 'franczyza.html')


def kariera(request):
    return render(request, 'kariera.html')


def partnerzy(request):
    return render(request, 'partnerzy.html')


def opinie(request):
    return render(request, 'opinie.html')


def regulamin(request):
    return render(request, 'regulamin.html')


def handmade_and_fresh(request):
    return render(request, 'handmade_and_fresh.html')


def alergeny(request):
    return render(request, 'alergeny.html')


def tabela_kalorii(request):
    return render(request, 'tabela_kalorii.html')


def kontakt(request):
    return render(request, 'kontakt.html')


def zamowienia(request):
    return render(request, 'zamowienia.html')
