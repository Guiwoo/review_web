from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("<int:pk>/profile/", views.ProfileView.as_view(), name="profile"),
    # path("<int:pk>/update/", views.ProfileView.as_view(), name="profile"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="updateProfile"),
    path("update-password/", views.UpdatePasswordView.as_view(), name="updatePassword"),
]
