from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    book = models.CharField()
    date = models.DateTimeField()



    def __str__(self):
        return self.title