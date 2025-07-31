from django.db import models

class Visite(models.Model):
    email = models.EmailField()
    number = models.CharField(max_length=14)
    message = models.TextField(max_length=500)
    subject = models.TextField(max_length=40)
    full_name = models.CharField()
    title = models.CharField(null=True, blank=True ,max_length=100)

    def __str__(self):
        return f'{self.number}: {self.full_name} {self.title}'

