from django.db import models


# Create your models here.
class Proyecto(models.Model):
    id_proyecto = models.IntegerField(verbose_name="Id del proyecto")
    nombre_proyecto = models.CharField(
        max_length=200, verbose_name="Nombre del proyecto"
    )
    tipo_proyecto = models.CharField(max_length=200, verbose_name="Tipo")
    region = models.CharField(max_length=200, verbose_name="Región")
    tipologia = models.CharField(max_length=200, verbose_name="Tipología")
    titular = models.CharField(max_length=200, verbose_name="Titular")
    inversion = models.DecimalField(
        max_digits=9, decimal_places=4, verbose_name="Inversión(MMU$)"
    )
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    estado = models.CharField(max_length=200, verbose_name="Estado del proyecto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-fecha_ingreso"]  # se ordenen por fecha de creacion a la inversa

    def __str__(self):
        return self.nombre_proyecto
