from django.urls import path
from Registro.views import *
from Usuario.views import *

urlpatterns = [
    path('return_ciudad', return_ciudad),
    path('return_tikets', return_tikets),
    path('remove_tikets', remove_tikets),
    path('return_tramites', return_tramites),

    path('linea_fabrica', certificado_linea_fabrica, name='linea_fabrica'),
    path('certificado_predio_rural', certificado_predio_rural,name='certificado_predio_rural'),
    path('compra_y_venta', compra_y_venta, name='compra_y_venta'),
    path('contrato_arr_cementerio', registro_contrato_arrendamiento_cementerio, name='contrato_arr_cementerio'),
    path('division_bien_inmueble', division_bien_inmueble, name='division_bien_inmueble'),
    path('fraccionamiento_agricola_unificacion_predio', fraccionamiento_agricola_unificacion_predio, name='fraccionamiento_agricola_unificacion_predio'),
    path('particion_extrajudicial_y_adjudicación', particion_extrajudicial_y_adjudicación, name='particion_extrajudicial_y_adjudicación'),
    path('cerramiento', permiso_cerramiento,name='cerramiento'),
    path('construccion_cementerio', construccion_cementerio,name='construccion_cementerio'),
    path('construccion_mayor', permiso_construccion_mayor,name='permiso_construccion_mayor'),
    path('construccion_menor', permiso_construccion_menor,name='permiso_construccion_menor'),
    path('rect_linderos_medidas_areas', rect_linderos_medidas_areas,name='rect_linderos_medidas_areas'),
    path('registro_letrero', registro_letrero,name='registro_letrero'),
    path('registro_municipal', registro_municipal,name='registro_municipal'),

    path('derechos_sepultura', derechos_sepultura, name='derechos_sepultura'),
    path('exhumacion_cadaveres', exhumacion_cadaveres, name='exhumacion_cadaveres'),
    path('patente_municipal', patente_municipal, name='patente_municipal'),
    path('uso_de_suelo', uso_de_suelo, name='uso_de_suelo'),
    path('rev_patente_municipal', rev_patente_municipal, name='rev_patente_municipal'),
    path('permiso_via_publica', permiso_via_publica, name='permiso_via_publica'),



    path('return_registro_municipal', return_registro_municipal, name='return_registro_municipal'),

]