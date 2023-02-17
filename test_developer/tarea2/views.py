from django.shortcuts import render, HttpResponse


# Create your views here.
def proyecto(request):
    return render(request, "proyecto.html")
