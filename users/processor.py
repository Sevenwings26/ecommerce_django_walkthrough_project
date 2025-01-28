# processor.py
from .models import Order

def cart_data(request):
    user = request.user if request.user.is_authenticated else None
    order = Order.objects.filter(customer=user, complete=False).first()
    cart_items = order.get_cart_items if order else 0
    cart_total = order.get_cart_total if order else 0
    
    return {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }

