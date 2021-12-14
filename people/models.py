from django.db import models
from django.urls import reverse
from core import models as core_models


class Person(core_models.TimeStampModel):
    """Person Definition"""

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"

    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=120)
    photo = models.ImageField(null=True, blank=True)
    kind = models.CharField(max_length=15, choices=KIND_CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("people:peopleDetail", kwargs={"pk": self.pk})
