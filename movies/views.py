from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import redirect, reverse
from movies.models import Movie
from movies.form import CreateMovieForm
from django.contrib import messages


class MoviesView(ListView):

    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "pk"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Movies"
        return context


class MovieDetail(DetailView):
    model = Movie
    context_object_name = "movie"


class MovieUpdate(UpdateView):
    model = Movie
    template_name = "movies/movie_update.html"
    context_object_name = "movie"
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )


class MovieCreate(CreateView):
    form_class = CreateMovieForm
    template_name = "movies/movie_create.html"

    def form_valid(self, form):
        movie = form.save()
        movie.save()
        form.save_m2m()
        messages.success(self.request, "Created !")
        return redirect(reverse("movies:movieDetail", kwargs={"pk": movie.pk}))
