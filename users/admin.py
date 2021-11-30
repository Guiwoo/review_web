from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre Admin"""

    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""

    pass


@admin.register(models.User)
class CoustomUserAdmin(UserAdmin):
    """CoustomUserAdmin Definition"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Profile",
            {"fields": ("bio", "language")},
        ),
        (
            "Preference",
            {"fields": ("preferenece", "favouriteBookGenre", "favouriteMovieGenre")},
        ),
    )
    list_display = (
        "username",
        "bio",
        "preferenece",
        "language",
    )
    list_filter = (
        "preferenece",
        "language",
        "favouriteBookGenre",
        "favouriteMovieGenre",
    )
