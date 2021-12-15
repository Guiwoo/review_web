from django import forms
from . import models
from categories.models import Category


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is Wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("Email does not exist !"))


class SignInForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "first_name",
            "last_name",
            "email",
        )

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def cleaned_password1(self):
        password1 = self.cleaned_data.get("password1")
        password = self.cleaned_data.get("password")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match!")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        username = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = username
        user.fav_book_cat = Category.objects.get(pk=1)
        user.fav_movie_cat = Category.objects.get(pk=1)
        user.set_password(password)
        user.save()
