from django.contrib import admin

# Register your models here.
from Funcionario.models import FuncionarioTramites
from tramites.snippers import Attr


@admin.register(FuncionarioTramites)
class modelo(admin.ModelAdmin):
    list_display = Attr(FuncionarioTramites)
    list_display_links = Attr(FuncionarioTramites)