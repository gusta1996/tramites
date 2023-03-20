from django.db import models

# Create your models here.
from Registro.models import Tramites
from Usuario.models import Perfil


class FuncionarioTramites(models.Model):
    tramite=models.ForeignKey(Tramites,on_delete=models.CASCADE)
    usuario= models.ForeignKey(Perfil,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Permisos de Funcionario"
