from django.views.generic import ListView, DetailView, UpdateView, CreateView
from movies.models import Movie


class MoviesView(ListView):

    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
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
    model = Movie
    template_name = "movies/movie_create.html"
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
