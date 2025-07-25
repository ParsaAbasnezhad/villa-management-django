from django.db import models
from django.template.defaultfilters import length


class Properties(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='properties/')
    bathroom = models.CharField(max_length=30)
    bedrooms = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    parking = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.fullname
