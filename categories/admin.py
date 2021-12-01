from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoriesAdmin(admin.ModelAdmin):

    fieldsets = (("Detail", {"fields": ("genre", "sort")}),)
    list_display = ("__str__", "sort")
    list_filter = ("genre", "sort")
