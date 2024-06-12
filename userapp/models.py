from django.contrib.auth.models import User
from django.db import models
from app44.models import book
# Create your models here.
class cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(book)




class cartitem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)