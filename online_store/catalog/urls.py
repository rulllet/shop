from django.urls import re_path, path
from . import views
from .views import SearchResultsView, HomePageView, NewProductView

urlpatterns = [
    re_path(r'^catalog/$', views.product_list, name='product_list'),
    re_path(r'^catalog/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^catalog/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='base'),
    path('newproducts/', NewProductView.as_view(), name='newproducts'),
]     

