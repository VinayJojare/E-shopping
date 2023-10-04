from django.db import models
from store.models.Category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products')        # this upload_to is used specify the image storage


    @staticmethod
    def get_all_ids(IDS):
        return Product.objects.filter(id__in = IDS)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_filter_products(category_id):
        if category_id:
            return Product.objects.filter(category_id=category_id)
        else:
            return Product.get_all_products()

