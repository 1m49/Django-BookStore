from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='book_cover/', blank=True)
    author = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    translator = models.CharField(max_length=50, blank=True)
    publisher = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])
