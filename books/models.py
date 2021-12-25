from django.urls import reverse
from django.db import models
from core.models import CoreModel


class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects"""

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class Book(CoreModel):

    """Book Model"""

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books"
    )
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books"
    )
    objects = GetOrNoneManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book", kwargs={"pk": self.pk})

    def all_reviews(self):
        return self.reviews.all()

    def get_first_reviews(self):
        (text,) = self.reviews.all()[:1]
        return text

    class Meta:
        ordering = ["-created_at"]
