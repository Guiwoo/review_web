from django.urls import path
from people.views import PeopleView, PeopleDetail, PersonUpdate

app_name = "people"

urlpatterns = [
    path("", PeopleView.as_view(), name="people"),
    path("<int:pk>", PeopleDetail.as_view(), name="peopleDetail"),
    path("<int:pk>/update", PersonUpdate.as_view(), name="personUpdate"),
]
