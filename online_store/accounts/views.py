from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from orders.models import OrderItem, Order


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
    
class AccountView(ListView): 
    model = OrderItem
    template_name = 'accounts/account.html'
    def get_queryset(self, **kwargs):
        return Order.objects.filter(username = self.request.user)

# class AccountView(ListView): 
#     model = OrderItem
#     template_name = 'accounts/account.html'




