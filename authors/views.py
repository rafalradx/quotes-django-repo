from django.shortcuts import get_object_or_404, render, redirect
from quotesapp.models import Author, Quote
from authors.forms import AuthorForm
from django.core.paginator import Paginator


# Create your views here.
def authors(request):
    # authors = Author.objects.all()
    paginator = Paginator(Author.objects.all(), 10)
    page = request.GET.get("page")
    authors = paginator.get_page(page)
    return render(request, "authors/display.html", {"authors": authors})


def details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    quotes_by_author = Quote.objects.filter(author_id=author_id)
    return render(
        request, "authors/details.html", {"author": author, "quotes": quotes_by_author}
    )


def add(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "authors/author.html", {"form": form})

    return render(request, "authors/author.html", {"form": AuthorForm()})
