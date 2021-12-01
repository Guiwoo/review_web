from django.db import models
from core import models as core_model


class Review(core_model.TimeStampModel):
    """Review Definition"""

    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    text = models.TextField()
    book = models.ForeignKey(
        "books.Book",
        related_name="reviews",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    movie = models.ForeignKey(
        "movies.Movie",
        related_name="reviews",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    rating = models.FloatField(help_text="Max Score is 10", default=5.0)
