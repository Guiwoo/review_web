from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoriesAdmin(admin.ModelAdmin):

    list_display = ("name", "kind")

    list_filter = ("kind",)
