from django.views import View
from django.shortcuts import render
from store.models.product_model import Product


class Orders(View):
    def get(self, request):
        IDS =(list(request.session.get('cart').keys()))
        ordered_item = Product.get_all_ids(IDS)
        print(ordered_item)
        return render(request, 'order.html', {"products":ordered_item})
