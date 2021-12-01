from django.db import models
from core import models as core_models


class Category(core_models.TimeStampModel):
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
    BOOK = "book"
    MOVIE = "movie"
    BOTH = "both"
    SORT_CHOICES = (
        (BOOK, "Book"),
        (MOVIE, "Movie"),
    )
    genre = models.CharField(
        choices=(
            ("Common", COMMON_CHOCIES),
            ("Movie", MOVIE_CHOCIES),
            ("Book", BOOK_CHOCIES),
        ),
        max_length=20,
        blank=True,
    )
    sort = models.CharField(choices=(SORT_CHOICES), max_length=5, blank=True)

    def __str__(self):
        return self.genre

    def save(self, *args, **kwargs):
        self.genre = str.capitalize(self.genre)
        self.create_genre = str.capitalize(self.genre)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ["genre", "sort"]
