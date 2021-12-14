from django import forms
from django.db.models import Q
from . import models


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            "title",
            "year",
            "cover_image",
            "rating",
            "category",
            "writer",
        )

    def __init__(self, *args, **kwargs):
        super(CreateBookForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = self.fields["category"].queryset.filter(
            Q(kind="book") | Q(kind="both")
        )
        self.fields["writer"].queryset = self.fields["writer"].queryset.filter(
            kind="writer"
        )

    def save(self, *args, **kwargs):
        book = super().save(commit=False)
        return book
