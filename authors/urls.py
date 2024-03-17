from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [
    path("add/", views.add, name="add"),
    path("", views.authors, name="authors"),
]
