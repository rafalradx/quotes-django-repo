from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Author(models.Model):
    fullname = models.CharField(max_length=255, unique=True)
    born_date = models.CharField(max_length=20)
    born_location = models.CharField(max_length=255)
    description = models.TextField()


class Quote(models.Model):
    quote = models.TextField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
