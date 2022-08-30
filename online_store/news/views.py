from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView   
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class BlogListView(ListView):
    # Отображение всех новостей
    model = Post
    paginate_by = 3
    template_name = 'news/home.html'
    def get_ordering(self):
        return '-id'
    
class BlogDetailView(DetailView): 
    # Страница с новостью
    model = Post
    template_name = 'news/post_detail.html'
   
class BlogCreateView(LoginRequiredMixin, CreateView):
    # Создание новости
    model = Post
    login_url = '/news'
    redirect_field_name = 'redirect_to'
    template_name = 'news/post_new.html'
    fields = ['image', 'title', 'author', 'thesis', 'text']
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    # Редактирование новости
    model = Post
    login_url = '/news'
    redirect_field_name = 'redirect_to'
    template_name = 'news/post_edit.html'
    fields = ['image', 'title', 'thesis', 'text']
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    # Удаление новости
    model = Post
    login_url = '/news'
    redirect_field_name = 'redirect_to'
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('home')


    
