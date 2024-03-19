from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
#Para que en el admin de la pagina aparesca el servicio que creamos en models
admin.site.register(Servicio,ServicioAdmin)

