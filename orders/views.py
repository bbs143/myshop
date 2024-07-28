from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Order, OrderItem
from cart.cart import Cart

@login_required
def order_list(request):
    orders = request.user.orders.all()

    return render(request, 'orders/list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(request.user.orders, id=order_id)

    return render(request, 'orders/order/detail.html', {'order': order})

@login_required
@require_POST
def order_create(request):
    cart = Cart(request)

    order = None
    if cart.coupon:
        order = Order.objects.create(
            account=request.user,
            coupon=cart.coupon,
            discount=cart.coupon.discount)
    else:
        order = Order.objects.create(account=request.user)

    for item in cart:
        OrderItem.objects.create(order=order,
                                    product=item['product'],
                                    price=item['price'])
    cart.clear()

    return render(request, 'orders/order/created.html',
                    {'order': order})
