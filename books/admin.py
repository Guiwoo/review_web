from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    """BookAdmin Definition"""

    list_display = ("title", "year", "category")
