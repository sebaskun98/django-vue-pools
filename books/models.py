from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    pCompany = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')

    class Meta:
        db_table = 'book'
        ordering = ['name', 'authors']

    def __str__(self):
        return self.name
