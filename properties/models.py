from django.db import models

class Visite(models.Model):
    email = models.EmailField()
    number = models.CharField(max_length=14, verbose_name='شماره تلفن')
    message = models.TextField(max_length=500,verbose_name='پیغام')
    subject = models.TextField(max_length=40, verbose_name='موضوع')
    full_name = models.CharField(verbose_name='نام شخص')
    title = models.CharField(null=True, blank=True ,max_length=100, verbose_name='ویلای مورد نظر')

    class Meta:
        verbose_name = "ملاقات"
        verbose_name_plural = "ملاقات ها"


    def __str__(self):
        return f'{self.number}: {self.full_name} {self.title}'

