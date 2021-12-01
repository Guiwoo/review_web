from django.db import models
from core import models as core_models
import datetime


def CHECK_DATE():
    return datetime.date.today().year


class Movie(core_models.TimeStampModel):
    """Movie Definition"""

    title = models.CharField(max_length=20)
    year = models.PositiveIntegerField(
        default=CHECK_DATE(),
    )
    cover_image = models.ImageField()
    rating = models.IntegerField(help_text="Max Score is 10", default=5.0)
    category = models.ManyToManyField("categories.Category", related_name="movies")
    director = models.ForeignKey(
        "people.Person", related_name="peopleDirector", on_delete=models.CASCADE
    )
    cast = models.ManyToManyField("people.Person", related_name="poepleCast")

    def __str__(self):
        return self.title
