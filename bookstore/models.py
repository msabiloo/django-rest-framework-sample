from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=50, null=False, blank=False)
    publisher = models.CharField(max_length=50, null=False, blank=False)

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rate_time = models.DateTimeField()

class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    in_stock = models.IntegerField()
    quantity = models.IntegerField()
