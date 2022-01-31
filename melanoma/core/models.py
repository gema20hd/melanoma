from django.db import models

# Create your models here.

#clase donde se registra la fecha de creacion, atulizacion y de un registro en la base de datos
class ClaseModelo(models.Model):
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


