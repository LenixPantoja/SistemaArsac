from django.contrib import admin
from .models import Persona
# Register your models here.

class PersonasAdmin(admin.ModelAdmin):
    readonly_fields=('user','fecha_creacion','fecha_actualizacion')
    search_fields=('cedula','user','fecha_creacion','fecha_actualizacion')
    list_filter=('cedula','user','fecha_creacion','fecha_actualizacion')
    list_display=('cedula','user','fecha_creacion','fecha_actualizacion')
    ordering=('fecha_creacion',)

    def save_model(self, request, obj, form ,change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(Persona, PersonasAdmin)