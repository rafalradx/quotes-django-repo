from django.urls import path
from . import views

app_name = "quotesapp"

urlpatterns = [
    path("", views.main, name="main"),
    path("tags/", views.tags, name="tags"),
    path("authors/", views.authors, name="authors"),
    path("quotes/", views.quotes, name="quotes"),
]
