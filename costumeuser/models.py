from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('account:profile', kwargs={'user_id': self.user.id})

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="worker")
    image = models.ImageField(default="default.jpeg", upload_to='profile_pics')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="company")
    image = models.ImageField(default="default.jpeg", upload_to='company_pics')
    company_name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
