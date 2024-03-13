from django.shortcuts import redirect, render
from quotesapp.forms import TagForm, AuthorForm, QuoteForm


# Create your views here.
def main(request):
    return render(request, "quotesapp/index.html")


def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/tag.html", {"form": form})

    return render(request, "quotesapp/tag.html", {"form": TagForm()})


def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/author.html", {"form": form})

    return render(request, "quotesapp/author.html", {"form": AuthorForm()})


def quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/quote.html", {"form": form})

    return render(request, "quotesapp/quote.html", {"form": QuoteForm()})
