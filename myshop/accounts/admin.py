from django.contrib import admin
from .models import CustomUser, Seller

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Seller)