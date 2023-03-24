from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey("Author", null=True, on_delete=models.DO_NOTHING)
    publishingCompany = models.ForeignKey("PublishingCompany", null=True, on_delete=models.DO_NOTHING)
    category = models.ForeignKey("Category", null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'book'
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name


class PublishingCompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    book_id = models.ForeignKey("Book", on_delete=models.DO_NOTHING)
    rating = models.ForeignKey("Rating", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment


class Rating(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.rating}'
