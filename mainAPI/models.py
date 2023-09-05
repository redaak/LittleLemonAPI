from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price=models.SmallIntegerField()
    inventory=models.PositiveIntegerField()
