from django.urls import path

from Funcionario.views import *

urlpatterns = [
   path('', perfil_funcionario, name='funcionario'),
   path('tramite', documentos, name='tramite'),
   path('resolve', aprobacion, name='resolve'),
   path('generar', aprobacion, name='generar'),
   path('certificado', certificado, name='certificado'),

]