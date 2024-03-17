from django.shortcuts import redirect, render
from quotesapp.forms import TagForm, QuoteForm
from django.http import HttpResponse


# Create your views here.
def main(request):
    return render(request, "quotesapp/index.html")


def tags(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/tag.html", {"form": form})

    return render(request, "quotesapp/tag.html", {"form": TagForm()})


def quotes(request):
    return HttpResponse("List of Authors")


def add(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/quote.html", {"form": form})

    return render(request, "quotesapp/quote.html", {"form": QuoteForm()})
