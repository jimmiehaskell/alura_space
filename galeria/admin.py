from django.contrib import admin
from galeria import models


# Register your models here.
class ListandoFotografias(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "legenda",
        "publicada",
    )

    list_display_links = (
        "id",
        "nome",
        "legenda",
    )

    search_fields = (
        "nome",
    )

    list_filter = (
        "categoria",
        "publicada",
    )

    list_editable = (
        "publicada",
    )

    list_per_page = 20


admin.site.register(models.Fotografia, ListandoFotografias)
