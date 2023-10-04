from django import template
register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for ID in keys:
        if int(ID) == product.id:
            return True
    return False


@register.filter(name='count_cart')
def count_cart(product,cart):
    keys = cart.keys()
    for ID in keys:
        if int(ID) == product.id :
            return cart.get(ID)
    return 0


@register.filter(name='price_total')
def price_total(product,cart):
    return product.price * count_cart(product,cart)


@register.filter(name='sum_price')
def sum_price(products,cart):
    sum = 0
    for pro in products:
        sum += price_total(pro, cart)
    return sum




