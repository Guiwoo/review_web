from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User Definition"""

    # Preference
    PREF_BOOK = "book"
    PREF_MOVIE = "movie"
    PREF_BOTH = "both"
    PREF_CHOICES = (
        (PREF_BOOK, "Book"),
        (PREF_MOVIE, "Movie"),
        (PREF_BOTH, "Both"),
    )
    # Language
    LANG_EN = "en"
    LANG_KR = "kr"
    LANG_ALL = "all"
    LANG_CHOICES = (
        (LANG_EN, "English"),
        (LANG_KR, "Korean"),
        (LANG_ALL, "All"),
    )
    bio = models.TextField(default="")

    # GENRE
    preferenece = models.CharField(choices=PREF_CHOICES, max_length=5, blank=True)
    language = models.CharField(choices=LANG_CHOICES, max_length=7, blank=True)
    favouriteBookGenre = models.ForeignKey(
        "categories.Category",
        related_name="userCategoryBook",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    favouriteMovieGenre = models.ForeignKey(
        "categories.Category",
        related_name="userCategoryMovie",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
