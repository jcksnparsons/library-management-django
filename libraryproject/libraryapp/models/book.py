from django.db import models
from django.urls import reverse


class Book (models.Model):
    title = models.CharField(max_length=50)
    ISBN_num = models.CharField(max_length=13)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField(max_length=4)


    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book _detail", kwargs={"pk": self.pk})