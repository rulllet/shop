from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import redirect

def order_create(request):
    # Создание заказа
    cart = Cart(request)
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                form.instance.username = request.user
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
        else:
            form = OrderCreateForm
    else:
            return redirect("login")
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})
