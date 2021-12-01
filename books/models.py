from django.db import models
from core import models as core_models
import datetime


def CHECK_DATE():
    return datetime.date.today().year


class Book(core_models.TimeStampModel):
    """Book Definition"""

    title = models.CharField(max_length=20)
    year = models.PositiveIntegerField(
        default=CHECK_DATE(),
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name="categories",
        on_delete=models.CASCADE,
    )
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField(help_text="Max Score is 10", default=5.0)
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="people"
    )

    def __str__(self):
        return self.title
