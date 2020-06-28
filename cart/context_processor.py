from .cart import Cart


def cart_total_amount(request):
    if request.session.get('cart'):
        cart = Cart(request)
        total_bill = 0
        for key, value in request.session['cart'].items():
            total_bill = total_bill + (int(value['price']) * value['quantity'])
        return {'cart_total_amount': total_bill}
    else:
        return {'cart_total_amount': 0}


# cart item count
def cart_total_count(request):
    if request.session.get('cart'):
        return {'cart_total_count': len(request.session.get('cart').items())}
    else:
        return {'cart_total_count': 0}
