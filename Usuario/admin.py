from django.contrib import admin

# Register your models here.
from Usuario.models import Provincias, Ciudades, Perfil
from tramites.snippers import Attr


class CiudadInline(admin.StackedInline):
    model = Ciudades
    extra = 0

@admin.register(Provincias)
class modelo(admin.ModelAdmin):
    list_display = Attr(Provincias)
    list_display_links = Attr(Provincias)
    inlines = [CiudadInline,]

@admin.register(Ciudades)
class modelo(admin.ModelAdmin):
    list_display = Attr(Ciudades)
    list_display_links = Attr(Ciudades)

@admin.register(Perfil)
class modelo(admin.ModelAdmin):
    list_display = Attr(Perfil)
    list_display_links = Attr(Perfil)
    search_fields = ['user__first_name', 'user__last_name','user__username']



