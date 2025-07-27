from django.db import models
from django.template.defaultfilters import length


class Category(models.Model):
    about = models.TextField()
    title = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SingleProperty(models.Model):
    total = models.IntegerField()
    payment = models.CharField(max_length=15)
    safety = models.CharField(max_length=15)
    contract = models.CharField(max_length=100)


class Properties(models.Model):
    about = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='properties/')
    bathroom = models.CharField(max_length=30)
    bedrooms = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    parking = models.CharField(max_length=30)
    # Address vila
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    # Single Property
    SingleProperty = models.ForeignKey(SingleProperty, null=True, blank=True, on_delete=models.CASCADE,
                                       related_name='SingleProperty')
    # Category
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f'{self.title}'


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.fullname} - {self.subject}'
