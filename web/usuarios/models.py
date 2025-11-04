from django.db import models

class Perfil(models.Model):
    nombre_completo = models.CharField(max_length=100)

    bio=models.TextField(blank=True, null=True)

    activo=models.BooleanField(default=True)
    
    fecha_creacion=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo