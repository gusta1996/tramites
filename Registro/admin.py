from django.contrib import admin

# Register your models here.
from Registro.models import *
from tramites.snippers import Attr


@admin.register(Tikets)
class modelo(admin.ModelAdmin):
    list_display = Attr(Tikets)
    list_display_links = Attr(Tikets)

class RequisitosInline(admin.StackedInline):
    model = Requisitos
    extra = 0

@admin.register(Tramites)
class modelo(admin.ModelAdmin):
    list_display = Attr(Tramites)
    list_display_links = Attr(Tramites)
    inlines = [RequisitosInline,]

@admin.register(Requisitos)
class modelo(admin.ModelAdmin):
    list_display = Attr(Requisitos)
    list_display_links = Attr(Requisitos)


@admin.register(RegistroMunicipal)
class modelo(admin.ModelAdmin):
    list_display = Attr(RegistroMunicipal)
    list_display_links = Attr(RegistroMunicipal)