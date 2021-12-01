from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    """ReviewAdmin Definition"""

    list_display = (
        "created_by",
        "text",
        "book",
        "movie",
        "rating",
    )
