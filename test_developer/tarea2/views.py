from django.shortcuts import render
from .models import Proyecto


# Create your views here.
def proyecto(request):
    proyectos = Proyecto.objects.all()
    data = {"proyectos": proyectos}
    return render(request, "proyectos.html", data)
