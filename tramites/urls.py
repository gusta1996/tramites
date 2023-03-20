from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from Registro.views import *
from Usuario.views import migrarUsuarios, __login, __profile, __logout, create_user, forgot_password, return_ciudad
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('token/', TokenObtainPairView.as_view(), name='obtener_token'),
   path('token/refresh/', TokenRefreshView.as_view(), name='actualizar_token'),
   path('token/verify/', TokenVerifyView.as_view(), name='verificar_token'),
   path('', include('rest_framework.urls')),
   path('', include('tramites.urlsApi')),
   path('funcionario/', include('Funcionario.urlsApi')),
   path('migrar/usuarios',migrarUsuarios),

    path('login',__login, name='login'),
    path('logouts',__logout, name='cerrar'),
    path('create_user',create_user, name='crear_usuario'),
    path('forget_password',forgot_password, name='olvido_contrasenia'),
    path('',__profile, name='perfil'),
    #app
    path('tikets',tickets,name='tickets'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
