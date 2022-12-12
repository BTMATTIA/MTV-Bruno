from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    fechaNacimiento=models.CharField(max_length=255)
    edad = models.IntegerField
    rolFamiliar=models.CharField(max_length=255, default="")
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.rolFamiliar}".format()
