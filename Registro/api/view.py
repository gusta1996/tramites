from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from Registro.models import *


class TramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tramites
        fields='__all__'

class TramiteViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Tramites.objects.all()
    serializer_class = TramiteSerializer


class RequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Requisitos
        fields='__all__'

class RequisitoViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Requisitos.objects.all()
    serializer_class = RequisitoSerializer

class TiketsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tikets
        fields='__all__'

class TiketsViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Tikets.objects.all()
    serializer_class = TiketsSerializer

class RegistrosSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegistroMunicipal
        fields='__all__'

class RegistroViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = RegistroMunicipal.objects.all()
    serializer_class = RegistrosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario','tramite__nombre']