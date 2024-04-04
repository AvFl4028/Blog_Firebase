from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.main, name="index"),
    path("public_post", views.public_post, name="public_post"),
    path("posts", views.post, name="post")
]
