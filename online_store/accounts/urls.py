from django.urls import path, re_path
from .views import SignUpView, AccountView, OrderItemDetailView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', AccountView.as_view(), name='account'),
    path('<int:pk>/', OrderItemDetailView.as_view(), name='order'),   
]