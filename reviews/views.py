from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from . import models as ReviewModel, forms


class ReviewList(ListView):
    model = ReviewModel.Review
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-pk"
    context_object_name = "reviews"
    template_name = "reviews/review.html"


@login_required()
def delete_photo(request, pk):
    user = request.user
    try:
        review = ReviewModel.Review.objects.get(pk=pk)
        if review.created_by.pk != user.pk:
            return redirect(reverse("core:home"))
        else:
            ReviewModel.Review.objects.filter(pk=pk).delete()
        return redirect(reverse("reviews:review"))

    except ReviewModel.Review.DoesNotExist:
        return redirect(reverse("core:home"))


class CreateReview(CreateView):
    model = ReviewModel.Review
    form_class = forms.CreateReviewForm
    template_name = "reviews/create.html"
    success_url = reverse_lazy("reviews:review")

    def get_form_kwargs(self):
        kwargs = super(CreateReview, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
