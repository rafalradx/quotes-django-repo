from django.forms import (
    ModelForm,
    CharField,
    ModelMultipleChoiceField,
    ModelChoiceField,
    TextInput,
    Textarea,
    CheckboxSelectMultiple,
)
from .models import Tag, Author, Quote


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]


class AuthorForm(ModelForm):
    fullname = CharField(max_length=255, widget=TextInput())
    born_date = CharField(max_length=20, widget=TextInput())
    born_location = CharField(max_length=255, widget=TextInput())
    description = CharField(max_length=1500, widget=Textarea())

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(ModelForm):
    quote = CharField(max_length=1000, widget=TextInput())

    # def __init__(self, *args, **kwargs):
    #     super(QuoteForm, self).__init__(*args, **kwargs)
    #     # Customize the author field if needed
    #     self.fields["author"].queryset = Author.objects.all()

    author = ModelChoiceField(queryset=Author.objects.all())

    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Quote
        fields = ["quote", "author", "tags"]  # Include other fields if needed


# class QuoteForm(ModelForm):
#     quote = CharField(max_length=1000, widget=TextInput())
#     author = ForeignKey(Author, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag)
