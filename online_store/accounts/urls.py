from django.urls import path, re_path
from .views import SignUpView, AccountView
 
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', AccountView.as_view(), name='account'),
]