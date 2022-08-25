from django.db import models
from catalog.models import Product
from django.conf import settings

class Order(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=50, verbose_name=("Имя"))
    last_name = models.CharField(max_length=50, verbose_name=("Фамилия"))
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name=("Адрес"))
    postal_code = models.CharField(max_length=20, verbose_name=("Индекс"))
    city = models.CharField(max_length=100, verbose_name=("Город"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name=("Оплачено"))
    delivered = models.BooleanField(default=False, verbose_name=("Доставлено"))
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
