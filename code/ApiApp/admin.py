from django.contrib import admin

# Register your models here.
from .models.productModel import Product

admin.site.register(Product)