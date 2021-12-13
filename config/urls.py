from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("movies/", include("movies.urls", namespace="movies")),
    path("books/", include("books.urls", namespace="books")),
    path("genres", include("categories.urls", namespace="genres")),
    path("people", include("people.urls", namespace="people/")),
    path("admin/", admin.site.urls),
]
