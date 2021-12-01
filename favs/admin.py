from django.contrib import admin
from . import models


@admin.register(models.Fav)
class FavAdmin(admin.ModelAdmin):
    """Favorit"""

    list_display = ("created_by",)
