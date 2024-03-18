from django.urls import path
from . import views

app_name = "tags"

urlpatterns = [
    path("add/", views.add, name="add"),
    path("", views.tags, name="tags"),
    path("details/<int:tag_id>", views.quotes_with_tag, name="details"),
]
