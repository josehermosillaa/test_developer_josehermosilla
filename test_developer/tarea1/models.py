from django.db import models

# Create your models here.

class Network(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    company = models.TextField(null=True, verbose_name="Compañia")
    id = models.CharField(max_length=200, verbose_name="id")
    href = models.URLField(max_length=128)
    location = models.CharField(max_length=200, verbose_name="Dirección")
    latitude= models.DecimalField(max_digits=9, decimal_places=6, verbose_name='latitud')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='longitud')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualización")

class Station(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    id = models.CharField(max_length=200, verbose_name="id")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='latitud')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='longitud')
    free_bikes = 
    empty_slots = 
    address = models.CharField(max_length=200, verbose_name="Dirección")
    ebikes = models.IntegerField(verbose_name='bicicletas electricas')
    has_ebikes=models.BooleanField()
    normal_bikes=models.IntegerField(verbose_name='bicicletas normales')
    payment = models.TextField(null=True, verbose_name="Formas de pago")
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=200, verbose_name="numero de post")
    renting = models.IntegerField(verbose_name='bicicletas rentadas')
    returning=models.IntegerField(verbose_name='bicicletas regresadas')
    slots= models.IntegerField(verbose_name='cantidad de espacios')
    uid = models.CharField(max_length=200, verbose_name="numero uid")
    date = model.models.DateTimeField()
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualización")

