from django.urls import reverse
from django.db import models
from core.models import CoreModel
from . import manager


class Movie(CoreModel):
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
    objects = manager.GetOrNoneManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movie", kwargs={"pk": self.pk})

    def all_reviews(self):
        return self.reviews.all()

    def get_first_reviews(self):
        if self.reviews.count() > 0:
            (text,) = self.reviews.all()[:1]
            return text
        return None

    class Meta:
        ordering = ["-created_at"]
