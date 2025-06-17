from django.contrib import admin
from app01.models import *
# Register your models here.

class InscripcionInLine(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = "Inscripción"
    verbose_name_plural = "Inscripciones"


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'departamento', 'instructor')
    list_filter = ('departamento', 'instructor')
    search_fields = ('titulo',)
    inlines = (InscripcionInLine,)

class EntregaInLine(admin.TabularInline):
    model = Entrega
    extra = 1
    verbose_name = "Entrega"
    verbose_name_plural = "Entregas"


class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_entrega', 'curso')
    list_filter = ('curso', 'estudiantes')
    search_fields = ('titulo',)
    inlines = (EntregaInLine,)


admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Entrega)
