from django.db import models
# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='asswts', height_field=None, width_field=None, max_length=100)
    desc=models.TextField()
    price=models.IntegerField()