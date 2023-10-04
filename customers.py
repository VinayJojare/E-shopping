from django.core.exceptions import ValidationError
from django.db import models
from django.contrib import messages


class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(unique=True)
    customer_email = models.EmailField()
    customer_password = models.CharField(max_length=500)

    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(customer_email):
        try:
            return Customer.objects.get(customer_email=customer_email)
        except:
            return False




    # def is_exist(self):
    #     if Customer.objects.filter(customer_email =self.customer_email):
    #         return True
    #     return False








