from django.db import models
from django.urls import reverse
from .library import Library
from .librarian import Librarian


class Book (models.Model):
    title = models.CharField(max_length=50)
    ISBN_num = models.CharField(max_length=13)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    publisher = models.CharField(max_length=50)
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book _detail", kwargs={"pk": self.pk})
