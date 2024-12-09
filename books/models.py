from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=250)
    Author = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    rating = models.CharField(max_length=1)
    Description = models.CharField(max_length=1000)
    Cover = models.CharField(max_length=1000)