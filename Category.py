from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

# str method is for overriding the name obj for showing the specific name
    def __str__(self):
        return self.name


