from django.db import models
from core import models as core_models


class Fav(core_models.TimeStampModel):
    """Favorit List"""

    created_by = models.OneToOneField("users.User", on_delete=models.CASCADE)
    books = models.ManyToManyField("books.Book", blank=True)
    movies = models.ManyToManyField("movies.Movie", blank=True)

    def __str__(self):
        return self.created_by.username
