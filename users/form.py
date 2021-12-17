from django import forms
from . import models
from categories.models import Category
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm


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


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("옛날 비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autofocus": True}),
    )

    new_password1 = forms.CharField(
        label=("새 비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autofocus": True}),
    )
    new_password2 = forms.CharField(
        label=("새 비밀번호 확인"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autofocus": True}),
    )
    field_order = ["old_password", "new_password1", "new_password2"]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "first_name",
            "last_name",
            "bio",
            "preference",
            "language",
            "fav_book_cat",
            "fav_movie_cat",
        )

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields["fav_book_cat"].queryset = self.fields[
            "fav_book_cat"
        ].queryset.filter(Q(kind="book") | Q(kind="both"))
        self.fields["fav_movie_cat"].queryset = self.fields[
            "fav_movie_cat"
        ].queryset.filter(Q(kind="movie") | Q(kind="both"))

    def save(self, *args, **kwargs):
        user = super().save()
        return user
