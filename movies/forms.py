from django import forms
from django.db.models import Q
from . import models


class MovieForm(forms.ModelForm):

    class Meta:
        model = models.Movie
        fields = (
            "title",
            "year",
            "cover_image",
            "rating",
            "category",
            "director",
            "cast",
        )

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = self.fields["category"].queryset.filter(
                Q(kind='movie') | Q(kind='both')
            )
        self.fields["director"].queryset = self.fields["director"].queryset.filter(
            kind="director"
        )
        self.fields["cast"].queryset = self.fields["cast"].queryset.filter(kind="actor")

    def save(self, *args, **kwargs):
        movie = super().save(commit=False)
        return movie
