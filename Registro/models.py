from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Usuario.models import Perfil


class Tikets(models.Model):
    nombre=models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Tramites(models.Model):
    nombre= models.CharField(max_length=120)
    detalle=models.TextField(null=True,blank=True)
    formula = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='1. Tramites'


class Requisitos(models.Model):
    tramite= models.ForeignKey(Tramites,on_delete=models.CASCADE)
    requisito=models.CharField(max_length=200)
    detalle=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.requisito

    class Meta:
        verbose_name_plural='2. Requisitos'

class RegistroMunicipal(models.Model):
    fecha=models.DateField(auto_now=True,null=True)
    numero=models.IntegerField(default=0)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    tramite=models.ForeignKey(Tramites,on_delete=models.CASCADE, null=True, blank=True)
    tiket=models.ForeignKey(Tikets,on_delete=models.CASCADE, null=True, blank=True)
    formula = models.CharField(max_length=120,null=True,blank=True)
    no_adeudar=models.FileField(upload_to='no_adeudar_municipio',null=True,blank=True)
    senescyt=models.FileField(upload_to='senescyt',null=True,blank=True)
    titulo=models.FileField(upload_to='titulos',null=True,blank=True)
    cedula=models.FileField(upload_to='cedulas',null=True,blank=True)
    votacion=models.FileField(upload_to='votacion',null=True,blank=True)
    profesion=models.CharField(max_length=300,null=True,blank=True)
    registro_profesional=models.CharField(max_length=300,null=True,blank=True)
    fot=models.FileField(upload_to='fotos',null=True,blank=True)
    nombre_negocio=models.TextField(null=True,blank=True)
    direccion_local=models.TextField(null=True,blank=True)
    ruc=models.FileField(upload_to='rucs',null=True,blank=True)
    x=models.DecimalField(max_digits=9,decimal_places=2,default=0)
    y=models.DecimalField(max_digits=9,decimal_places=2,default=0)
    disenio=models.FileField(upload_to='letrero',null=True,blank=True)
    escritura=models.FileField(upload_to='escritura',null=True,blank=True)
    no_adeudar_e = models.FileField(upload_to='no_adeudar_epaagua', null=True, blank=True)
    primera_vez=models.BooleanField(default=False)
    declaracion_juramentada=models.FileField(upload_to='declaracion_juramentada',null=True,blank=True)
    planos=models.FileField(upload_to='planos',null=True,blank=True)
    area=models.DecimalField(max_digits=9,decimal_places=2,default=0)
    codigo_nacional=models.CharField(max_length=20,null=True,blank=True)
    codigo_local = models.CharField(max_length=20, null=True, blank=True)
    sector=models.CharField(max_length=200,null=True,blank=True)
    parroquia = models.CharField(max_length=200, null=True, blank=True)
    sitio = models.CharField(max_length=200, null=True, blank=True)
    calles = models.CharField(max_length=200, null=True, blank=True)
    norte=models.TextField(null=True,blank=True)
    sur=models.TextField(null=True,blank=True)
    este=models.TextField(null=True,blank=True)
    oeste=models.TextField(null=True,blank=True)
    n_comprobante=models.CharField(max_length=30,null=True,blank=True)
    fecha_pago=models.DateField(null=True,blank=True)
    n_certificado=models.CharField(max_length=30,null=True,blank=True)
    f_retiro=models.DateField(null=True,blank=True)
    nombre_retira=models.CharField(max_length=100,null=True,blank=True)
    grafico=models.ImageField(upload_to='graficos', null=True,blank=True)
    puntos = models.ImageField(upload_to='puntos', null=True, blank=True)
    clave_catastral=models.CharField(max_length=200,default= '00000000000000000000')
    datos_observaciones=models.TextField(null=True,blank=True,)
    valor_avaluo=models.DecimalField(max_digits=9, decimal_places=2, default=0)

    costo = models.DecimalField(default=0, decimal_places=2, max_digits=9)
    es_usado=models.BooleanField(default=False)
    estado=models.BooleanField(default=False)
    finalizado = models.BooleanField(default=False)
    fecha_caducidad=models.DateField(null=True,blank=True)
    notas=models.TextField(null=True,blank=True)
    
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.cedula:
            perfil= Perfil.objects.get(user=self.usuario)
            perfil.cedula=self.cedula
            perfil.save()
        super(RegistroMunicipal, self).save()


