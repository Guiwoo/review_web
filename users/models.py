from django.contrib.auth.models import AbstractUser
from django.db import models


class Genre(models.Model):
    # GENRE
    # common
    GENRE_ACTION = "action"
    GENRE_FANTASY = "fantasy"
    GENRE_HORROR = "horror"
    GENRE_MYSTERY = "mystery"
    COMMON_CHOCIES = (
        (GENRE_ACTION, "Action"),
        (GENRE_FANTASY, "Fantasy"),
        (GENRE_HORROR, "Horror"),
        (GENRE_MYSTERY, "Mystery"),
    )
    # Movie
    GENRE_COMEDY = "comedy"
    GENRE_DRAMA = "drama"
    GENRE_ROMANCE = "romance"
    GENRE_THRILLER = "thriller"
    MOVIE_CHOCIES = (
        (GENRE_COMEDY, "Comedy"),
        (GENRE_DRAMA, "Drama"),
        (GENRE_ROMANCE, "Romance"),
        (GENRE_THRILLER, "Thriller"),
    )
    # book
    GENRE_ADVENTURE = "adventure"
    GENRE_CLASSICS = "classics"
    GENRE_COMIC = "comicBook"
    GENRE_DETECTIVE = "detective"
    GENRE_HISTORICAL = "historical"
    GENRE_LITERARY = "literary"
    BOOK_CHOCIES = (
        (GENRE_ADVENTURE, "Adventure"),
        (GENRE_CLASSICS, "Classics"),
        (GENRE_COMIC, "Comic Book"),
        (GENRE_DETECTIVE, "Dectective"),
        (GENRE_HISTORICAL, "Historical Fiction"),
        (GENRE_LITERARY, "Literary Fiction"),
    )
    genre = models.CharField(
        choices=(
            ("Common", COMMON_CHOCIES),
            ("Movie", MOVIE_CHOCIES),
            ("Book", BOOK_CHOCIES),
        ),
        max_length=20,
    )

    def __str__(self):
        return self.genre

    def save(self, *args, **kwargs):
        self.genre = str.capitalize(self.genre)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = str.capitalize(self.name)
        super().save(*args, **kwargs)


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
        "Genre",
        related_name="favouriteBookGenre",
        on_delete=models.CASCADE,
        default="",
        null=True,
    )
    favouriteMovieGenre = models.ForeignKey(
        "Category",
        related_name="favouriteMovieGenre",
        on_delete=models.CASCADE,
        default="",
        null=True,
    )
