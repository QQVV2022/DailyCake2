from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length = 200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.CharField(max_length = 300)

class Address(models.Model):
    item = models.CharField(max_length = 500)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    total_price = models.CharField(max_length = 100)


class Users(User):
    last_modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    """USER self define"""
    # mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        # db_table = 'tb_users'   # DB name https://docs.djangoproject.com/zh-hans/3.2/ref/models/options/
        verbose_name = 'USER'
        verbose_name_plural = verbose_name  # another name on Admin site

    def __str__(self):
        return self.username