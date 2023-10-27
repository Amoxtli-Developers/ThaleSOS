from django.contrib import admin
from .models import Warning, Categorie

# Register your models here.


class WarningAdmin(admin.ModelAdmin):
    list_display = ('id', 'keywords', 'category')  # Campos que se mostrarán en la lista
    list_filter = ('category',)  # Campos por los cuales filtrar
    search_fields = ('keywords',)  # Campos que se pueden buscar

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message')
    search_fields = ('name', 'message')


admin.site.register(Warning, WarningAdmin)
admin.site.register(Categorie, CategorieAdmin)
