from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models import Customer
from django.views import View


class Signup(View):

    def get(self, request):
        if request.method == 'GET':
            return render(request, 'Signup.html')

    def post(self, request):
        post_request = request.POST
        first_name = post_request.get('first_name')
        last_name = post_request.get('last_name')
        phone = post_request.get('phone')
        customer_email = post_request.get('customer_email')
        customer_password = post_request.get('customer_password')
        print(first_name, last_name, phone, customer_email, customer_password)

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, customer_email=customer_email,
                            customer_password=customer_password)

        customer.customer_password = make_password(customer.customer_password)
        customer.save()

        return redirect('homepage')
