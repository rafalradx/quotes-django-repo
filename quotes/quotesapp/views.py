from django.shortcuts import redirect, render
from quotesapp.forms import TagForm


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
