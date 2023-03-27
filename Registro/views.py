from django.contrib import messages
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from Registro.models import RegistroMunicipal, Tikets, Tramites, Requisitos
from Usuario.models import Provincias, Perfil
from tramites.snippers import render_to_pdf


def return_tikets(request):
    tikes=Tikets.objects.all()
    return HttpResponse(serializers.serialize('json', tikes))

def remove_tikets(request):
    if request.GET.get('id'):
        registro=RegistroMunicipal.objects.get(id=request.GET.get('id'))
        registro.delete()
        messages.add_message(request,messages.ERROR,"El registro se ha eliminado exitosamente..!")
    return HttpResponseRedirect('tikets')

def return_tramites(request):
    tramites=Tramites.objects.all()
    return HttpResponse(serializers.serialize('json', tramites))

def tickets(request):
    if request.POST:
        print(request.POST)
        reg=RegistroMunicipal.objects.create(
            usuario=request.user,
            tiket_id=request.POST.get('t'),
            tramite_id=request.POST.get('clase'),
            formula="1",
            estado=False,
            es_usado=False,
            finalizado=True,
        )
        reg.save()
        messages.add_message(request,messages.SUCCESS,"El trámite se ha creado correctamente, por favor acerquece al "
                                                      "GAD Municipal para continuar con el proceso..!")
        return HttpResponseRedirect('tikets')
    contexto={
        'registros':RegistroMunicipal.objects.filter(usuario=request.user,tramite__nombre='Tickets'),
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request, 'tickets.html',contexto)


# URBANISMO
def certificado_linea_fabrica(request):
    tramite=Tramites.objects.get(nombre__icontains='línea de fábrica')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('linea_fabrica')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/linea_fabrica?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/linea_fabrica')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'linea_fabrica.html',contexto)

def certificado_predio_rural(request):
    tramite=Tramites.objects.get(nombre__icontains='certificado de predio rural')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('certificado_predio_rural')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')

                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')

                try:
                    reg.declaracion_juramentada = request.FILES['declaracion_juramentada']
                except:
                    print('no viene declaracion_juramentada')

                try:
                    reg.planos = request.FILES['planos']
                except:
                    print('no viene planos')

                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/certificado_predio_rural?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/certificado_predio_rural')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'certificado_predio_rural.html',contexto)

def compra_y_venta(request):
    tramite=Tramites.objects.get(nombre__icontains='compra y venta')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('compra_y_venta')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/compra_y_venta?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/compra_y_venta')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'compra_y_venta.html',contexto)

def registro_contrato_arrendamiento_cementerio(request):
    tramite=Tramites.objects.get(nombre__icontains='Contrato de Arrendamiento de Cementerio')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'solicitud' in request.GET:
        print('entro a la solicitud')
        try:
            reg = registros.get(pk=request.GET.get('solicitud'))
        except:
            reg = RegistroMunicipal.objects.get(pk=request.GET.get('solicitud'))
        contexto={
            'registro':reg,
            'perfil':Perfil.objects.get(user=request.user)
        }

        return render_to_pdf('contrato_arrendamiento_cementerio.html',contexto)

    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('contrato_arr_cementerio')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                    print(request.FILES['no_adeudar_e'])
                except:
                    print('no viene no_adeudar_e')
                try:
                    if request.POST.get('primera_vez'):
                        reg.primera_vez = True
                    else:
                        reg.primera_vez = False
                except:
                    print('no viene primera vez')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/contrato_arr_cementerio?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/contrato_arr_cementerio')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request, 'registro_contrato_arrendamiento_cementerio.html', contexto)

def division_bien_inmueble(request):
    tramite=Tramites.objects.get(nombre__icontains='División de Bien Inmueble')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('division_bien_inmueble')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/division_bien_inmueble?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/division_bien_inmueble')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'division_bien_inmueble.html',contexto)

def fraccionamiento_agricola_unificacion_predio(request):
    tramite=Tramites.objects.get(nombre__icontains='Fraccionamiento Agrícola, Unificación De Predios (Urbano Y Rural)')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('fraccionamiento_agricola_unificacion_predio')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/fraccionamiento_agricola_unificacion_predio?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/fraccionamiento_agricola_unificacion_predio')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'fraccionamiento_agricola_unificacion_predio.html',contexto)

def particion_extrajudicial_y_adjudicación(request):
    tramite=Tramites.objects.get(nombre__icontains='Partición Extrajudicial y Adjudicación (Urbano y Rural)')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('particion_extrajudicial_y_adjudicación')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/particion_extrajudicial_y_adjudicación?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/particion_extrajudicial_y_adjudicación')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'particion_extrajudicial_y_adjudicación.html',contexto)

def permiso_cerramiento(request):
    tramite=Tramites.objects.get(nombre__icontains='permiso de cerramiento')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('cerramiento')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/cerramiento?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/cerramiento')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'permiso_cerramiento.html',contexto)

def construccion_cementerio(request):
    tramite=Tramites.objects.get(nombre__icontains='Permiso de Construcción en el Cementerio')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('construccion_cementerio')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_e')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/construccion_cementerio?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/construccion_cementerio')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'construccion_cementerio.html',contexto)

def permiso_construccion_mayor(request):
    tramite=Tramites.objects.get(nombre__icontains='Permiso De Construcción Mayor')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('construccion_mayor')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/construccion_mayor?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/construccion_mayor')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'construccion_mayor.html',contexto)

def permiso_construccion_menor(request):
    tramite=Tramites.objects.get(nombre__icontains='permiso de construcción menor')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('construccion_menor')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/construccion_menor?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/construccion_menor')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'construccion_menor.html',contexto)

def rect_linderos_medidas_areas(request):
    tramite=Tramites.objects.get(nombre__icontains='Rectificación de Linderos, Medidas y Áreas (Urbano y Rural)')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('rect_linderos_medidas_areas')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/rect_linderos_medidas_areas?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/rect_linderos_medidas_areas')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'rect_linderos_medidas_areas.html',contexto)

def registro_letrero(request):
    tramite=Tramites.objects.get(nombre__icontains='registro de letrero')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'solicitud' in request.GET:
        print('entro a la solicitud')
        try:
            reg = registros.get(pk=request.GET.get('solicitud'))
        except:
            reg=RegistroMunicipal.objects.get(pk=request.GET.get('solicitud'))
        contexto={
            'registro':reg,
            'perfil':Perfil.objects.get(user=request.user)
        }
        return render_to_pdf('solicitud_letrero.html',contexto)

    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('registro_letrero')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.ruc = request.FILES['ruc']
                except:
                    print('no viene ruc')
                try:
                    reg.x = request.POST.get('x')
                except:
                    print('no viene x')
                try:
                    reg.y = request.POST.get('y')
                except:
                    print('no viene y')

                try:
                    reg.nombre_negocio = request.POST.get('local')
                except:
                    print('no viene local')
                try:
                    reg.disenio = request.FILES['disenio']
                except:
                    print('no viene disenio')
                try:
                    reg.direccion_local = request.POST.get('direccion')
                except:
                    print('no viene direccion')

                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/registro_letrero?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/registro_letrero')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'registro_letrero.html',contexto)

def registro_municipal(request):
    tramite=Tramites.objects.get(nombre__icontains='registro municipal')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('registro_municipal')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/registro_municipal?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/registro_municipal')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'registro_municipal.html',contexto)
# FIN - URBANISMO

# COMISARIA MUNICIPAL
def derechos_sepultura(request):
    tramite=Tramites.objects.get(id=23)
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('derechos_sepultura')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/derechos_sepultura?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/derechos_sepultura')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'derechos_sepultura.html',contexto)

def exhumacion_cadaveres(request):
    tramite=Tramites.objects.get(nombre__icontains='Exhumación De Cadáveres')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('exhumacion_cadaveres')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/exhumacion_cadaveres?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/exhumacion_cadaveres')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'exhumacion_cadaveres.html',contexto)

def patente_municipal(request):
    tramite=Tramites.objects.get(id=25)
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('patente_municipal')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/patente_municipal?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/patente_municipal')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'patente_municipal.html',contexto)

def uso_de_suelo(request):
    tramite=Tramites.objects.get(nombre__icontains='Permiso de Uso de Suelo')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('uso_de_suelo')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/uso_de_suelo?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/uso_de_suelo')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'uso_de_suelo.html',contexto)

def rev_patente_municipal(request):
    tramite=Tramites.objects.get(nombre__icontains='Renovacion Patente Municipal')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('rev_patente_municipal')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/rev_patente_municipal?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/rev_patente_municipal')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'rev_patente_municipal.html',contexto)

def permiso_via_publica(request):
    tramite=Tramites.objects.get(nombre__icontains='Solicitud Permiso de Vía Pública')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('permiso_via_publica')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.no_adeudar_e = request.FILES['no_adeudar_e']
                except:
                    print('no viene no_adeudar_epaagua')
                try:
                    reg.escritura = request.FILES['escritura']
                except:
                    print('no viene escritura')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/permiso_via_publica?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/permiso_via_publica')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'permiso_via_publica.html',contexto)
# FIN - COMISARIA MUNICIPAL

# RENTAS

def alcabalas(request):
    tramite=Tramites.objects.get(nombre__icontains='Alcabalas')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('alcabalas')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/alcabalas?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/alcabalas')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'alcabalas.html',contexto)

def apertura_usuarios(request):
    tramite=Tramites.objects.get(nombre__icontains='Aperturas de usuario')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('apertura_usuarios')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/apertura_usuarios?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/apertura_usuarios')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'apertura_usuarios.html',contexto)

def cierre_patentes(request):
    tramite=Tramites.objects.get(nombre__icontains='Cierre de patentes')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('cierre_patentes')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/cierre_patentes?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/cierre_patentes')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'cierre_patentes.html',contexto)

def convenios_pago(request):
    tramite=Tramites.objects.get(nombre__icontains='Convenios De Pago')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('convenios_pago')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/convenios_pago?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/convenios_pago')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'convenios_pago.html',contexto)

def exoneracion_tercera_edad(request):
    tramite=Tramites.objects.get(nombre__icontains='Exoneración De Tercera Edad')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('exoneracion_tercera_edad')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/exoneracion_tercera_edad?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/exoneracion_tercera_edad')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'exoneracion_tercera_edad.html',contexto)

def ingreso_cert_riesgo(request):
    tramite=Tramites.objects.get(nombre__icontains='Ingreso De Certificados De Riesgo')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('ingreso_cert_riesgo')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/ingreso_cert_riesgo?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/ingreso_cert_riesgo')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'ingreso_cert_riesgo.html',contexto)

def ingreso_der_sepultura(request):
    tramite=Tramites.objects.get(nombre__icontains='Ingreso De Derechos De Sepultura')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('ingreso_der_sepultura')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/ingreso_der_sepultura?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/ingreso_der_sepultura')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'ingreso_der_sepultura.html',contexto)

def mensualidad_arr_feria_libre(request):
    tramite=Tramites.objects.get(nombre__icontains='Ingreso De Mensualidad De Arriendo De Local En La Feria Libre De La Cdla La Octubrina')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('mensualidad_arr_feria_libre')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/mensualidad_arr_feria_libre?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/mensualidad_arr_feria_libre')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'mensualidad_arr_feria_libre.html',contexto)

def ingreso_ocupacion_via_pub(request):
    tramite=Tramites.objects.get(nombre__icontains='Ingreso De Valor Por Ocupacion De Via Publica')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('ingreso_ocupacion_via_pub')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/ingreso_ocupacion_via_pub?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/ingreso_ocupacion_via_pub')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'ingreso_ocupacion_via_pub.html',contexto)

def ingreso_energia_centro_com(request):
    tramite=Tramites.objects.get(nombre__icontains='Ingresos De Energía Eléctrica Del Centro Comercial')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('ingreso_energia_centro_com')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/ingreso_energia_centro_com?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/ingreso_energia_centro_com')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'ingreso_energia_centro_com.html',contexto)

def mensualidad_solares(request):
    tramite=Tramites.objects.get(nombre__icontains='Mensualidades De Solares Municipales')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('mensualidad_solares')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/mensualidad_solares?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/mensualidad_solares')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'mensualidad_solares.html',contexto)

def patentes(request):
    tramite=Tramites.objects.get(id=40)
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('patentes')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/patentes?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/patentes')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'patentes.html',contexto)

def plusvalia(request):
    tramite=Tramites.objects.get(nombre__icontains='Plusvalía')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('plusvalia')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/plusvalia?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/plusvalia')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'plusvalia.html',contexto)

def revision_vehicular(request):
    tramite=Tramites.objects.get(nombre__icontains='Revisión Vehicular')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('revision_vehicular')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/revision_vehicular?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/revision_vehicular')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'revision_vehicular.html',contexto)

def rodaje(request):
    tramite=Tramites.objects.get(nombre__icontains='rodaje')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('rodaje')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/rodaje?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/rodaje')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'rodaje.html',contexto)

def notas_creditos(request):
    tramite=Tramites.objects.get(nombre__icontains='Notas De Créditos')
    registros=RegistroMunicipal.objects.filter(usuario=request.user,tramite=tramite)
    reg = None
    if 'remove' in request.GET:
        reg = registros.get(pk=request.GET.get('remove'))
        reg.delete()
        messages.add_message(request, messages.SUCCESS, "Registro Eliminado..!")
        return HttpResponseRedirect('notas_creditos')
    if request.POST:
        if 'enviar' in request.POST:
            reg = registros.filter(pk=request.POST.get('id')).last()
            reg.estado=True
            reg.save()
            return HttpResponse('ok')
        else:
            if 'id' in request.GET:
                reg = registros.filter(pk=request.GET.get('id')).last()
                reg.formula='1'
                print(request.POST)
                cedula = Perfil.objects.get(user=request.user).cedula
                if cedula:
                    reg.cedula = cedula
                try:
                    reg.cedula = request.FILES['cedula']
                except:
                    print('no viene cedula')
                try:
                    reg.votacion = request.FILES['votacion']
                except:
                    print('no viene votacion')
                try:
                    reg.no_adeudar = request.FILES['no_adeudar']
                except:
                    print('no viene no_adeudar')
                try:
                    reg.senescyt = request.FILES['senescyt']
                except:
                    print('no viene senescyt')
                try:
                    reg.titulo = request.FILES['titulo']
                except:
                    print('no viene titulo')
                reg.registro_profesional=request.POST.get('n_senescyt')
                reg.profesion = request.POST.get('profesion')
                try:
                    reg.save()
                    messages.add_message(request, messages.SUCCESS, "El documento se cargo exitosamente..!")
                    return HttpResponseRedirect('/notas_creditos?id='+request.GET.get('id'))
                except:
                    return HttpResponseRedirect('/notas_creditos')
            else:
                reg = RegistroMunicipal()
                reg.usuario=request.user
                reg.tramite_id=request.POST.get('clase')
                reg.formula="1"
                reg.estado=False
                reg.es_usado=False
                reg.finalizado=False
                reg.save()
                messages.add_message(request, messages.SUCCESS, "El trámite se ha creado correctamente..!")
    contexto={
        'tramite':tramite,
        'requisitos':Requisitos.objects.filter(tramite=tramite),
        'registro':reg,
        'registros':registros,
        'perfil':Perfil.objects.get(user=request.user)
    }
    return render(request,'notas_creditos.html',contexto)

# FIN - RENTAS

def return_registro_municipal(request):
    registro=RegistroMunicipal.objects.get(id=request.GET.get('id'))
    print(registro.usuario)
    return HttpResponse(serializers.serialize('json', [registro]))