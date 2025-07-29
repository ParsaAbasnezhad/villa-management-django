from django.db import models

class Visite(models.Model):
    email = models.EmailField()
    number = models.CharField(max_length=14)
    message = models.TextField()
    title = models.CharField()
    fullname = models.CharField()

    def __str__(self):
        return f'{self.number}: {self.fullname}'