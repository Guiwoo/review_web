from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import redirect, reverse
from books.models import Book
from books.form import CreateBookForm
from django.contrib import messages


class BooksView(ListView):

    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "pk"
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


class BookCreate(CreateView):
    form_class = CreateBookForm
    template_name = "books/book_create.html"
    context_object_name = "book"

    def form_valid(self, form):
        book = form.save()
        book.save()
        messages.success(self.request, "Created !")
        return redirect(reverse("books:bookDetail", kwargs={"pk": book.pk}))
