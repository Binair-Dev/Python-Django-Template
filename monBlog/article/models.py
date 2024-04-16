from django.db import models

# Create your models here.
class Author(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{ self.last_name } - { self.first_name }"

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    content = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f"{ self.title }"