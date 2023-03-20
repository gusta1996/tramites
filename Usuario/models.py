from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Provincias(models.Model):
    nombre=models.CharField(max_length=60)

    class Meta:
        verbose_name_plural="1. Provincias"

    def __str__(self):
        return self.nombre

class Ciudades(models.Model):
    provincia=models.ForeignKey(Provincias,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="2. Ciudades"


class Perfil(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    funcionario=models.BooleanField(default=False)
    ciudad=models.ForeignKey(Ciudades, on_delete=models.CASCADE,null=True,blank=True)
    direccion=models.CharField(max_length=120,blank=True)
    telefono=models.CharField(max_length=20,blank=True)
    fecha_nacimiento=models.DateField(blank=True,null=True)
    cedula=models.FileField(upload_to='cedulas', null=True,blank=True)
    foto=models.ImageField(upload_to='avatar',null=True,blank=True)
    nacionalidad=models.CharField(max_length=120, default="ECUATORIANA")
    empresa=models.CharField(max_length=300, null=True,blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name_plural="3. Perfiles"