from django.db import models


from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email=models.EmailField(unique=True) 

class category(models.Model):
    Title = models.CharField( max_length=500)

    def __str__(self):
        return self.Title

class products(models.Model):
    Title=models.ForeignKey(category,on_delete=models.CASCADE)
    Product = models.CharField(max_length=500)


