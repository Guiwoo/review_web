from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.ReviewList.as_view(), name="review"),
    path("<int:pk>/delete/", views.delete_photo, name="delete"),
    path("create/", views.CreateReview.as_view(), name="create"),
]
