from django.db import models

# Create your models here.

class report(models.Model):
    user_name   = models.CharField(max_length=30)
    email       = models.EmailField()
    location    = models.CharField(max_length=50)
    date_time   = models.DateTimeField()
    discription = models.TextField()
    image       = models.ImageField(upload_to="Images")
