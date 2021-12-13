from django.views.generic import ListView, DetailView, UpdateView
from people.models import Person


class PeopleView(ListView):

    model = Person
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "people"
    template_name = "people/people_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All People"
        return context


class PeopleDetail(DetailView):
    model = Person
    context_object_name = "person"


class PersonUpdate(UpdateView):
    model = Person
    context_object_name = "person"
    template_name = "people/person_update.html"
    fields = (
        "name",
        "photo",
        "kind",
    )
