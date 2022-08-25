from django.db import models
from django.urls import reverse



class Post(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    thesis = models.TextField(max_length=200, default="")
    text = models.TextField()
 
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    

