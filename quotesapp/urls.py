from django.urls import path
from . import views

app_name = "quotesapp"

urlpatterns = [
    path("", views.main, name="main"),
    path("tags/", views.tags, name="tags"),
    path("quotes/", views.quotes, name="quotes"),
    path("quotes/add/", views.add, name="add"),
]
