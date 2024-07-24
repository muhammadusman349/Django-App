from django.db import models
from account.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year  = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-id']