
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Usuario.models import Provincias, Ciudades, Perfil

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','first_name','last_name','username', 'email', 'is_staff','is_active']


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProvinciasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provincias
        fields=['id','nombre']

class ProvinciasViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Provincias.objects.all()
    serializer_class = ProvinciasSerializer



class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ciudades
        fields='__all__'

class CiudadesViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['provincia',]

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Perfil
        fields='__all__'

class PerfilViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
