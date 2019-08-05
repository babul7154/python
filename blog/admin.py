from django.contrib import admin

# Register your models here.
from .models import post
admin.site,admin.site.register(post)