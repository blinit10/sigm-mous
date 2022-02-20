from django.contrib import admin
from .models import *
#inlines
#model admins
#define una clase que hereda de admin.ModelAdmin
class ReporteVariableMeteorologicaAdmin(admin.ModelAdmin):
    #define los campos que seran mostrados a manera de lista en el sitio administrativo
    list_display = ('estacion', 'meteorologo', 'fecha_hora', 'temperatura', 'humedad',
                    'presion', 'dirr', 'dirs', 'vels', 'velp')
    #define a traves de que campos se puede acceder a los detalles del objeto
    list_display_links = ('estacion', 'meteorologo', 'fecha_hora')
    #define sobre que campos se podra realizar el filtrado
    #el filtrado se realiza a traves de la barra lateral derecha
    list_filter = ('meteorologo', 'estacion', 'fecha_hora')
    #define cuantas filas se muestran por pagina
    list_per_page = 10
    #define sobre que campos se realiza la busqueda
    search_fields = ['meteorologo',]

class InformeOficialVariableMeteorologicaPronvincialAdmin(admin.ModelAdmin):
    list_display = ('provincia', 'estacion', 'tecnico', 'fecha_hora', 'viento',
                    'lluvia', 'temperatura', 'humedad', 'barometro')
    list_display_links = ('provincia', 'estacion', 'tecnico', 'fecha_hora')
    list_filter = ('tecnico', 'estacion', 'fecha_hora', 'provincia')
    list_per_page = 10
    search_fields = ['tecnico',]

class InformeVariableMeteorologicaGeneralAdmin(admin.ModelAdmin):
    list_display = ('tecnico', 'fecha_hora', 'temperatura', 'viento', 'lluvia', 'humedad', 'barometro')
    list_display_links = ('tecnico', 'fecha_hora')
    list_filter = ('tecnico', 'fecha_hora')
    list_per_page = 10
    search_fields = ['tecnico',]

class ParteMeteorologicoProvincialAdmin(admin.ModelAdmin):
    list_display = ('provincia', 'meteorologo', 'fecha_hora', 'temperatura', 'viento', 'lluvia')
    list_display_links = ('provincia', 'meteorologo', 'fecha_hora')
    list_filter = ('provincia', 'meteorologo', 'fecha_hora')
    list_per_page = 10
    search_fields = ['meteorologo', 'provincia']

class ParteMeteorologicoGeneralAdmin(admin.ModelAdmin):
    list_display = ('tecnico', 'fecha_hora', 'temperatura', 'viento', 'lluvia')
    list_display_links = ('tecnico', 'fecha_hora')
    list_filter = ('tecnico', 'fecha_hora')
    list_per_page = 10
    search_fields = ['tecnico',]

#admin.site.register
#Paso 1 - admin.site.register(ReporteVariableMeteorologica)
#Paso 2 - admin.site.register(ReporteVariableMeteorologica, ReporteVariableMeteorologicaAdmin)
admin.site.register(Estacion)
admin.site.register(ReporteVariableMeteorologica, ReporteVariableMeteorologicaAdmin)
admin.site.register(InformeOficialVariableMeteorologicaPronvincial, InformeOficialVariableMeteorologicaPronvincialAdmin)
admin.site.register(InformeVariableMeteorologicaGeneral, InformeVariableMeteorologicaGeneralAdmin)
admin.site.register(ParteMeteorologicoProvincial, ParteMeteorologicoProvincialAdmin)
admin.site.register(ParteMeteorologicoGeneral, ParteMeteorologicoGeneralAdmin)
