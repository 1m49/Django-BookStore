from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Book Model
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


# Comment Model
class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
