from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import pandas as pd
from django.core import serializers
# Create your views here.
from Usuario.models import Perfil, Ciudades, Provincias


def __login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                if Perfil.objects.get(user=user).funcionario:
                    return HttpResponseRedirect('funcionario/'+request.GET.get('next'))
                else:
                    return HttpResponseRedirect(request.GET.get('next'))
            else:
                if Perfil.objects.get(user=user).funcionario:
                    return HttpResponseRedirect('funcionario')
                return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,"Es posible que la combinación de usuario y clave no sea la correcta o que el usuario no exista, Reintente..!")
            print('usuario no existe')
            return HttpResponseRedirect('login')
    else:
        return render(request,'login.html')

@login_required(login_url='login')
def __logout(request):
    logout(request)
    return HttpResponseRedirect('login')

def create_user(request):
    if request.POST:
        user=User()
        try:
            user=User.objects.get(username=request.POST.get('username'))
            messages.add_message(request,messages.ERROR,"No es posible crear el usuario, debido a que ya existe en la base de datos")
            return HttpResponseRedirect('create_user')
        except Exception as error:
            user= User.objects.create_user(username=request.POST.get('username'),is_active=True)
            user.set_password(request.POST.get('password1'))
            user.save()
            perfil=Perfil.objects.create(user=user)
            perfil.save()
            messages.add_message(request, messages.SUCCESS,"El Usuario se registro, a partir de ahora ya puede iniciar sesión")
            return HttpResponseRedirect('create_user')
    return render(request,'registration.html')

def forgot_password(request):
    if request.GET.get('email'):
        print(request.GET.get('email'))
        print(request.session.get('usuario'))
        usuario=User.objects.get(username=request.session.get('usuario'))
        usuario.email=request.GET.get('email')
        usuario.save()
        del request.session['usuario']
        request.session.save()
        return HttpResponse('ok')

    if request.POST:
        try:
            usuario= User.objects.get(username=request.POST.get('username'))
            request.session['usuario'] = usuario.username
            if usuario.email:
                messages.add_message(request,messages.SUCCESS,"Los pasos para la activación se enviarón a su correo electrónico registrado: %s..!"%usuario.email)
                return HttpResponseRedirect('forget_password')
            else:
                request.session.save()
                messages.add_message(request,messages.ERROR,"no")
        except Exception as error:
            messages.add_message(request,messages.ERROR,"El Usuario no existe en la base de datos..!")

    return render(request,'forget_password.html')

@login_required(login_url='login')
def __profile(request):
    user = request.user
    perfil = Perfil.objects.get(user=user)
    if request.POST:
        if 'update' in request.GET:
            user.first_name=request.POST.get('nombres')
            user.last_name=request.POST.get('apellidos')
            user.email=request.POST.get('email')
            user.save()
            perfil.ciudad_id=request.POST.get('ciudad')
            perfil.direccion=request.POST.get('direccion')
            perfil.telefono=request.POST.get('telefono')
            perfil.fecha_nacimiento=request.POST.get('fecha')
            perfil.empresa=request.POST.get('empresa')

        if 'avatar' in request.GET:
            perfil.foto=request.FILES['avatar']
        if 'cedula' in request.GET:
            perfil.cedula=request.FILES['cedula']
        perfil.save()
        messages.add_message(request,messages.SUCCESS,'Los datos se actualizaron exitosamente..!')
        if perfil.funcionario:
            return HttpResponseRedirect('funcionario')
        else:
            return HttpResponseRedirect('/')
    contexto={
        'perfil':Perfil.objects.get(user=request.user),
        'provincias':Provincias.objects.all().order_by('nombre')
    }
    if perfil.funcionario:
        return HttpResponseRedirect('funcionario')
    return render(request,'profile.html',contexto)


def return_ciudad(request):
    ciudades=Ciudades.objects.all()
    if request.GET.get('id'):
        ciudades=ciudades.filter(provincia_id=request.GET.get('id'))
        print(serializers.serialize('json',ciudades))
        return HttpResponse(serializers.serialize('json',ciudades))
    else:
        print(serializers.serialize('json',ciudades))
        return JsonResponse(serializers.serialize('json', ciudades))



#migracion:
def migrarUsuarios(request):
    sheet_name = "Hoja1"
    df = pd.read_excel(io="BASE.xlsx", sheet_name=sheet_name)
    contador=0
    for i in df.values:
        contador+=1
        try:
            print("[ ",contador," ]",i[1],i[2],i[3],i[4],i[5])
            users=User.objects.create(
                username=i[1],
                first_name=i[2],
                last_name=i[3],
                is_active=True,
            )
            users.save()
            users.set_password(i[1])
            users.save()
            perfil=Perfil.objects.create(
                user=users,
                direccion=i[4],
                telefono=i[5],
                fecha_nacimiento=i[6],
            )
            perfil.save()
        except Exception as err:
            archivo=open('error-%s.txt'%str(i[1]),'w')
            archivo.write(str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
            archivo.close()
            print("Error en el registro", i[3],i[4])
    return HttpResponse("ok")