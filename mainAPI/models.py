from django.db import models

# Create your models here.
class Category(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title

class MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price=models.SmallIntegerField()
    inventory=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
