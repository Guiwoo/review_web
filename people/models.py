from django.db import models
from core import models as core_models


class Person(core_models.TimeStampModel):
    """Person Definition"""

    SORT_ACTOR = "actor"
    SORT_ACTRESS = "actress"
    SORT_DIRECTOR = "director"
    SORT_WRITER = "writer"
    SORT_CHOICE = (
        (SORT_ACTOR, "Actor"),
        (SORT_ACTRESS, "Actress"),
        (SORT_DIRECTOR, "Director"),
        (SORT_WRITER, "Writer"),
    )

    name = models.CharField(max_length=20, default="Unknown")
    sort = models.CharField(max_length=9, choices=SORT_CHOICE)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
