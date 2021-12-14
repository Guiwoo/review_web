from django.urls import path
from books.views import BooksView, BookDetail, BookUpdate, BookCreate

app_name = "books"

urlpatterns = [
    path("", BooksView.as_view(), name="books"),
    path("<int:pk>", BookDetail.as_view(), name="bookDeatil"),
    path("<int:pk>/update", BookUpdate.as_view(), name="bookUpdate"),
    path("create", BookCreate.as_view(), name="bookCreate"),
]
