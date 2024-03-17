from django.shortcuts import render, redirect
from django.http import HttpResponse

from authors.forms import AuthorForm


# Create your views here.
def authors(request):
    return HttpResponse("Authors listed")


def add(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "authors/author.html", {"form": form})

    return render(request, "authors/author.html", {"form": AuthorForm()})
