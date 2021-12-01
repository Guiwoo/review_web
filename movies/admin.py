from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    """Movie Admin Definition"""

    list_display = (
        "title",
        "year",
        "rating",
        "director",
    )
