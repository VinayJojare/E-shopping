from django.contrib import admin
from .models.product_model import Product
from .models.Category import Category
from .models.customers import Customer


# for showing category type inside the Product section:
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


# for showing name of category inside the Category section
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# here AdminProduct and AdminCategory is for connect it to above classes
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
