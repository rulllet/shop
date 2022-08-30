from django.views.generic import TemplateView, ListView
from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm


class HomePageView(TemplateView):
    # Главная страница
    template_name = 'index.html'
    
class SearchResultsView(ListView):
    # Результаты посика
    result = Product.objects.all()
    template_name = 'catalog/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(name__icontains=query)

class NewProductView(ListView):
    # Сортировка товаров по новизне
    queryset = Product.objects.order_by('-created')
    template_name = 'catalog/newproducts.html'

def product_list(request, category_slug=None):
    # Каталог товаров по категориям
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        print(products)
    return render(request, 'catalog/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    # Страница товара
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/detail.html', 
                  {'product': product,
                    'cart_product_form': cart_product_form})