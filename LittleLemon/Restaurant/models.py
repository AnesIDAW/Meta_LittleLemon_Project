from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self) -> str:
        return self.first_name
    

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_desc = models.TextField(max_length=1000, default="")

    def __str__(self) -> str:
        return f'{self.name} : {self.price}'
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'