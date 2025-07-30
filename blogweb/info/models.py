from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField()
    date = models.DateField( auto_now_add=True)
    query = models.CharField(max_length=500)