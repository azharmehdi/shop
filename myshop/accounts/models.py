from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username    
    
class Seller(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    is_seller = models.BooleanField(default=True)
    Government_ID = models.CharField(max_length=50, null=True)
    Business_License = models.CharField(max_length=50, null=True)
    Business_Name = models.CharField(max_length=100, null=True)
    Business_Address = models.CharField(max_length=255, null=True)
    Business_Phone_Number = models.CharField(max_length=15, null=True)
    Business_Email = models.EmailField(null=True)
    Business_Description = models.TextField(null=True)
    Tax_ID = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return self.user.username

