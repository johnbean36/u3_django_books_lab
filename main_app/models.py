from django.db import models
from django.urls import reverse

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=15)
    published = models.CharField(max_length=100)
    store = models.ManyToManyField(Store)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    
class Review(models.Model):
    name = models.CharField(max_length = 20)
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

