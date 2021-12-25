from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = (
            "created_by",
            "text",
            "movie",
            "book",
            "rating",
        )
        widgets = {
            "text": forms.Textarea(attrs={"class": "w-full bg-transparent h-32"})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.fields["created_by"].queryset = self.fields["created_by"].queryset.filter(
            pk=self.user.pk
        )
        self.fields["created_by"].initial = self.user

    def save(self, *args, **kwargs):
        review = super().save(commit=True)
        review.save()
        return review
