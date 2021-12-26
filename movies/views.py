from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect, reverse
from .forms import MovieForm
from movies.models import Movie


class MoviesView(ListView):

    model = Movie
    paginate_by = 15
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Movies"
        return context


class MovieDetail(DetailView):
    model = Movie
    context_object_name = "movie"


class CreateMovie(CreateView):
    form_class = MovieForm
    template_name = "movies/movie_form.html"
    
    def form_valid(self, form):
        movie = form.save()
        movie.save()
        form.save_m2m()
        return redirect(reverse("movies:movie", kwargs={"pk": movie.pk}))


class UpdateMovie(UpdateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )
