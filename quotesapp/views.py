from django.shortcuts import redirect, render
from quotesapp.forms import QuoteForm
from django.http import HttpResponse
from quotesapp.models import Quote
from django.core.paginator import Paginator


# Create your views here.
def main(request):
    return render(request, "quotesapp/index.html")


def quotes(request):
    quotes = Quote.objects.all()
    extracted_tags = [quote.tags.all() for quote in quotes]
    paginator = Paginator(list(zip(quotes, extracted_tags)), 5)
    page = request.GET.get("page")
    quotes_and_tags = paginator.get_page(page)
    return render(request, "quotesapp/display.html", {"quotes": quotes_and_tags})


def add(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/quote.html", {"form": form})

    return render(request, "quotesapp/quote.html", {"form": QuoteForm()})
