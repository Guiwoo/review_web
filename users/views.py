from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, views
from . import form


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = form.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogoutView(views.LogoutView):
    next_page = reverse_lazy("core:home")


class SignInView(FormView):
    template_name = "users/signin.html"
    form_class = form.SignInForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name": "test", "last_name": "test", "email": "test@test.com"}

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
