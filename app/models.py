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
    image = models.CharField(max_length=200)
    duration = models.CharField(max_length= 20)
    

    def __str__(self):
        return self.title
