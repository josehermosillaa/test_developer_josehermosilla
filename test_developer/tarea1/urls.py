from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("description/<str:code>/", views.description, name="descripcion"),
]
