from django.shortcuts import render, redirect
from django.http import HttpResponse

from tags.forms import TagForm


# Create your views here.
def tags(request):
    return HttpResponse("list of tags")


def add(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "tags/tag.html", {"form": form})

    return render(request, "tags/tag.html", {"form": TagForm()})
