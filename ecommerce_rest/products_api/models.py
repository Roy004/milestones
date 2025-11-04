from django.db import models

class Color(models.Model):
    nombre=models.CharField(max_length=100)

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.FloatField()
    color=models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True,
        related_name='productos',
    )
    