from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()


    def __str__(self):
        return self.name
