from django.contrib import admin

from .models import User,razonSocial,unidadOperativa

admin.site.register(User)
admin.site.register(razonSocial)
admin.site.register(unidadOperativa)

admin.site.site_header = "Plataforma de Induccion Pacasmayo"
admin.site.site_title = "Plataforma de Induccion Pacasmayo"
admin.site.index_title = "Bienvenidos a la plataforma  de induccion"
