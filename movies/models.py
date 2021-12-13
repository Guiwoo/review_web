from django.db import models
from core.models import TimeStampModel
from django.urls import reverse


class Movie(TimeStampModel):

    """Movie Model"""

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies"
    )
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies"
    )
    cast = models.ManyToManyField("people.Person", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movieDetail", kwargs={"pk": self.pk})
