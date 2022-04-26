
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # default route
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    path("profile/<str:user>", views.profile, name="profile"),

    # API Routes
    path("edit/<str:post_id>", views.edit, name="edit"),
    path("like/<str:post_id>", views.like, name="like")
]
