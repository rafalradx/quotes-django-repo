from django.shortcuts import redirect, render
from quotesapp.forms import QuoteForm
from django.http import HttpResponse
from quotesapp.models import Quote


# Create your views here.
def main(request):
    return render(request, "quotesapp/index.html")


def quotes(request):
    quotes = Quote.objects.all()
    extracted_tags = [quote.tags.all() for quote in quotes]
    return render(
        request, "quotesapp/display.html", {"quotes": zip(quotes, extracted_tags)}
    )


def add(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/quote.html", {"form": form})

    return render(request, "quotesapp/quote.html", {"form": QuoteForm()})
