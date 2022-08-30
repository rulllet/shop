from .cart import Cart

def cart(request):
    # Контекстный процессор корзины
    return {'cart': Cart(request)}