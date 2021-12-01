from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


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
        "first_name",
        "last_name",
        "email",
        "bio",
        "preferenece",
        "language",
        "favouriteBookGenre",
        "favouriteMovieGenre",
    )
    list_filter = (
        "preferenece",
        "language",
        "favouriteBookGenre",
        "favouriteMovieGenre",
    )
