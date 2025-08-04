from django.db import models
from django.template.defaultfilters import length, slugify


class Category(models.Model):
    about = models.TextField()
    title = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    img = models.ImageField(upload_to='Category/')

    def __str__(self):
        return self.title


class SingleProperty(models.Model):
    total = models.IntegerField()
    payment = models.CharField(max_length=15)
    safety = models.CharField(max_length=15)
    contract = models.CharField(max_length=100)
    active_parking = models.BooleanField(default=True)


class Properties(models.Model):
    about = models.TextField(verbose_name='درباره دسته')
    description = models.TextField(verbose_name='توضیحات')
    title = models.CharField(max_length=100, unique=True,verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='properties/',verbose_name='عکس')
    bathroom = models.CharField(max_length=30,verbose_name='اتاق')
    bedrooms = models.CharField(max_length=30,verbose_name='سالن')
    floor = models.CharField(max_length=30,verbose_name='طبقه')
    area = models.CharField(max_length=30)
    parking = models.CharField(max_length=30)
    # Address vila
    street = models.CharField(max_length=100,verbose_name='خیابان')
    city = models.CharField(max_length=50,verbose_name='شهر')
    state = models.CharField(max_length=20,verbose_name='کوچه')
    postal_code = models.CharField(max_length=10,verbose_name='پلاک')
    # slug
    slug = models.SlugField(unique=True,blank=True, null=True)
    # Single Property
    sing = models.ForeignKey(SingleProperty, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='SingleProperty',verbose_name='')
    # Category
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='categories',verbose_name='دسته')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Contact(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='نام شخص')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیغام')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='روز ارسال')

    def __str__(self):
        return f'{self.fullname} - {self.subject}'
