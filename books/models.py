from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Book Model
class Book(models.Model):
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE, verbose_name='ایجاد کننده کتاب')
    title = models.CharField(max_length=150, verbose_name='عنوان کتاب')
    cover = models.ImageField(upload_to='book_cover/', blank=True, verbose_name='عکس')
    author = models.CharField(max_length=50, blank=True, verbose_name='نویسنده')
    description = models.TextField(verbose_name='توضیحات کتاب')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='قیمت')
    translator = models.CharField(max_length=50, blank=True, verbose_name='مترجم')
    publisher = models.CharField(max_length=50, blank=True, verbose_name='انتشارات')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


# Comment Model
class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='متن خود را وارد کنید')
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True, verbose_name='این کتاب و پیشنهاد میکنی؟')

    def __str__(self):
        return self.text
