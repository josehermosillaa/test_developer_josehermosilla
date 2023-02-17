from django.shortcuts import render
from .models import Station


# Create your views here.
def home(request):
    stations = Station.objects.all()
    data = {"stations": stations}
    return render(request, "home.html", data)


def description(request, code):
    station = Station.objects.get(id=code)
    lista = station.payment.replace("[", "")
    lista1 = lista.replace("]", "")
    medios = lista1.split(",")
    data = {"station": station, "code": code, "medios": medios}
    return render(request, "description.html", data)
