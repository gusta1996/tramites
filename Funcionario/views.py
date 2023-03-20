import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Registro.models import RegistroMunicipal, Tramites
from Usuario.models import *
from tramites.snippers import render_to_pdf


def perfil_funcionario(request):
    contexto={
        'perfil':Perfil.objects.get(user=request.user),
        'provincias': Provincias.objects.all().order_by('nombre'),
    }
    return render(request,'funcionario/profile.html',contexto)

def documentos(request):
    tramite=Tramites.objects.get(id=request.GET.get('id'))
    print(tramite)
    contexto={
        'perfil': Perfil.objects.get(user=request.user),
        'documentos':RegistroMunicipal.objects.filter(tramite=tramite),
    }
    return render(request, 'funcionario/documentos.html', contexto)

def aprobacion(request):
    if request.POST:
        print(request.POST)
        registro=RegistroMunicipal.objects.get(id=request.POST.get('id'))
        registro.fecha_caducidad=request.POST.get('caducidad')
        notas=""
        if 'notas2' in request.POST:
            registro.datos_observaciones=request.POST.get('notas2')
        if 'datos' in request.POST:
            registro.datos_observaciones=request.POST.get('datos')

            registro.area=request.POST.get('area')
            registro.valor_avaluo=request.POST.get('valor')
            registro.save()
            messages.add_message(request, messages.SUCCESS, 'Los datos del predio se actualizaron correctamente..!')
            return HttpResponseRedirect('/funcionario/resolve?id=%s' % registro.id)

        if 'grafico' in request.POST or 'puntos' in request.POST:
            try:
                registro.grafico=request.FILES['grafico']
            except:
                pass
            try:
                registro.puntos = request.FILES['puntos']
            except:
                pass
            registro.save()
            messages.add_message(request, messages.SUCCESS, 'Los datos del predio se actualizaron correctamente..!')
            return HttpResponseRedirect('/funcionario/resolve?id=%s' % registro.id)

        if 'comprobante' in request.POST:
            registro.n_comprobante=request.POST.get('comprobante')
            registro.fecha_pago=request.POST.get('f_pago')
            registro.n_certificado=request.POST.get('n_certificado')
            registro.f_retiro = request.POST.get('f_retiro')
            registro.nombre_retira=request.POST.get('persona_retiro')
            registro.save()
            messages.add_message(request, messages.SUCCESS, 'Los datos del predio se actualizaron correctamente..!')
            return HttpResponseRedirect('/funcionario/resolve?id=%s' % registro.id)

        if 'area' in request.POST:
            registro.area=request.POST.get('area')
            registro.codigo_nacional=request.POST.get('nacional')
            registro.codigo_local=request.POST.get('local')
            registro.sector=request.POST.get('sector')
            registro.parroquia=request.POST.get('parroquia')
            registro.sitio=request.POST.get('sitio')
            registro.calles=request.POST.get('calles')
            registro.norte=request.POST.get('norte')
            registro.sur=request.POST.get('sur')
            registro.este=request.POST.get('este')
            registro.oeste=request.POST.get('oeste')
            registro.save()
            messages.add_message(request, messages.SUCCESS, 'Los datos del predio se actualizaron correctamente..!')
            return HttpResponseRedirect('/funcionario/resolve?id=%s'%registro.id)

        if 'cedula' in request.POST:
            notas+= "Cedula de identidad inconsistente, "
            registro.estado=False
            registro.es_usado=False
            registro.finalizado=False
            registro.cedula=None

        if 'votacion' in request.POST:
            notas+= "Documento de votación no es válido, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.votacion=None

        if 'no_adeudar' in request.POST:
            notas+= "El Certificado de no adeudar al Municipio no es válido o ya caducó, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.no_adeudar=None

        if 'no_adeudar_e' in request.POST:
            notas+= "El Certificado de no adeudar a EPAAGUA no es válido o ya caducó, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.no_adeudar_e=None

        if 'senescyt' in request.POST:
            notas+= "El Certificado de Senescyt no es válido, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.senescyt=None

        if 'titulo' in request.POST:
            notas+= "El título cargado no es válido, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.titulo=None

        if 'ruc' in request.POST:
            notas+= "El RUC no es válido, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.ruc=None

        if 'disenio' in request.POST:
            notas+= "El Diseño no concuerda con el registro, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.disenio=None

        if 'escritura' in request.POST:
            notas+= "La escritura no es legible o no es posible comprobar la información pertinenete al trámite, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.escritura=None

        if 'declaracion' in request.POST:
            notas+= "La declaración juramentada no es válida, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.declaracion_juramentada=None

        if 'planos' in request.POST:
            notas+= "Los planos no son legibles o no se relacionan con el trámite, "
            registro.estado = False
            registro.finalizado = False
            registro.es_usado = False
            registro.planos=None

        if request.POST.get('costo') != '':
            print(request.POST)
            registro.costo=request.POST.get('costo')
        else:
            registro.costo=0

        if notas != '':
            registro.notas = request.POST.get('notas') +'No se puede continuar con la validación debido a que hay inconvenientes en los documentos suministrados.\n'+  "\n" + notas + "Favor verificar y volver a cargar."
        else:
            registro.notas= request.POST.get('notas')


        registro.save()
        messages.add_message(request,messages.SUCCESS,'Se registro Detalles adicionales')
        return HttpResponseRedirect('/funcionario/resolve?id=%s'%registro.id)
    if 'generar' in request.GET:
        registro=RegistroMunicipal.objects.get(id=request.GET.get('id'))
        registro.finalizado=True
        registro.estado=True
        registro.es_usado=True
        registro.save()
        messages.add_message(request, messages.INFO, 'Se registro Cambio de estado a Finalizado')
        print('generado')
        return HttpResponseRedirect('/funcionario/resolve?id=%s' % registro.id)
    contexto={
        'perfil': Perfil.objects.get(user=request.user),
        'documento':RegistroMunicipal.objects.get(id=request.GET.get('id')),
        'fecha':datetime.datetime.now().date()

    }
    return render(request, 'funcionario/resolver.html', contexto)

def certificado(request):
    registro = RegistroMunicipal.objects.get(id=request.GET.get('id'))
    contexto={
        'registro':registro,
        'fecha':datetime.datetime.now(),
        'funcionario':request.user.get_full_name(),
    }
    if 'registromunicipal' in request.GET:
        return render_to_pdf('reportes/registromunicipal.html',contexto)
    if 'prediorural' in request.GET:
        return render_to_pdf('reportes/prediorural.html',contexto)
        #return render(request,'reportes/prediorural.html',contexto)
    if 'construccionmenor' in request.GET:
        #return render(request,'reportes/construccion_menor.html',contexto)
        return render_to_pdf('reportes/construccion_menor.html', contexto)
    if 'letrero' in request.GET:
        #return render(request, 'reportes/permiso_letrero.html', contexto)
        return render_to_pdf('reportes/permiso_letrero.html', contexto)
    if 'construccioncementerio' in request.GET:
        return render_to_pdf('reportes/permiso_ccementerio.html', contexto)
    if 'lineafabrica' in request.GET:
        #return render(request,'reportes/lineafabrica.html', contexto)
        return render_to_pdf('reportes/lineafabrica.html', contexto)