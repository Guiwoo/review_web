import datetime
from core import models as core_models
from django.db import models
from django.urls import reverse


def CHECK_DATE():
    return datetime.date.today().year


class Book(core_models.TimeStampModel):
    """Book Definition"""

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField()
    rating = models.FloatField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books"
    )
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:bookDetail", kwargs={"pk": self.pk})
