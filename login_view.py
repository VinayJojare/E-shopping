from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models import Customer
from django.views import View


# for logging in to account
class Login(View):
    def get(self, request):
        if request.method == 'GET':
            return render(request, "login_page.html")

    def post(self, request):
        username = request.POST.get('customer_email')
        password = request.POST.get('customer_password')
        e_customer = Customer.get_customer_by_email(username)

        if e_customer:
            flag = check_password(password,e_customer.customer_password)
            if flag:
                request.session['username'] = e_customer.customer_email
                return redirect('homepage')
            else:
                pass
        else:
            return render(request,'login_page.html',)


def logout(request):
    request.session.clear()
    return redirect('login')
