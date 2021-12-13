from django.urls import path
from movies.views import MoviesView, MovieDetail, MovieUpdate, MovieCreate

app_name = "movies"

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
    path("<int:pk>/", MovieDetail.as_view(), name="movieDetail"),
    path("<int:pk>/update", MovieUpdate.as_view(), name="movieUpdate"),
    path("create", MovieCreate.as_view(), name="movieCreate"),
]
