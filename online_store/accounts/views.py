from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView
from orders.models import OrderItem, Order
from django.http import HttpResponse, Http404
from catalog.models import Product


class SignUpView(generic.CreateView):
    # Регистрация клиента
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
class AccountView(ListView): 
    # Личный кабинет клиента и отображение всех заказов
    template_name = 'accounts/account.html'
    def get_queryset(self):
        return Order.objects.filter(username = self.request.user)

class OrderItemDetailView(DetailView):
    # Информация о заказе
    template_name = 'accounts/order.html'
    def get_queryset(self):
        return Order.objects.filter(username = self.request.user, pk=self.kwargs.get("pk", None))
