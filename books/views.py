from django.views.generic import ListView, DetailView, UpdateView
from books.models import Book


class BooksView(ListView):

    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Books"
        return context


class BookDetail(DetailView):
    model = Book
    context_object_name = "book"


class BookUpdate(UpdateView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_update.html"
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "writer",
    )
