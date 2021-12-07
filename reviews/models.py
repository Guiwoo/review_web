from django.db import models
from core import models as core_model


class Review(core_model.TimeStampModel):
    """Review Definition"""

    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField()

    def __str__(self):
        return self.text
