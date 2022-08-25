from django.contrib import admin
from .models import Post
from .models import Post
 
admin.site.register(Post)
# def create_time_display(self, obj):
#     return obj.create_time.strftime("%B %d, %Y")
# create_time_display.short_description = 'data'