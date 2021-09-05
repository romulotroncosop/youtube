from django.db import models

# Create your models here.
class Search(models.Model):
    name =  models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Result(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    views = models.CharField(max_length= 20)
    link = models.CharField(max_length=100)
    search = models.ForeignKey(Search, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
