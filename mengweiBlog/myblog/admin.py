from django.contrib import admin
from .models import User, Administrator, Article

# Register your models here.
admin.site.register(User)
admin.site.register(Administrator)
admin.site.register(Article)