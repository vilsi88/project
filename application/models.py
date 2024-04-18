from django.db import models

# Create your models here.
class Product(models.Model) :
    product_title = models.CharField(max_length=100 , null=True, blank=True)
    product_price = models.CharField(max_length=500 , null=True, blank=True)
    product_image = models.ImageField(upload_to="item/" , null=True, blank=True)

      