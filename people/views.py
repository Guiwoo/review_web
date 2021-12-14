from django.urls.base import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import redirect
from django.contrib import messages
from people.models import Person
from people.form import CreatePersonForm


class PeopleView(ListView):

    model = Person
    paginate_by = 10
    paginate_orphans = 5
    ordering = "pk"
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


class PersonCreate(CreateView):
    form_class = CreatePersonForm
    template_name = "people/person_create.html"
    context_object_name = "person"

    def form_valid(self, form):
        person = form.save()
        person.save()
        messages.success(self.request, "Created !")
        return redirect(reverse("people:peopleDetail", kwargs={"pk": person.pk}))
