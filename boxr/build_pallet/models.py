from django.db import models

# Create your models here.
from django.db import models

class Size(models.Model):
    size_id = models.IntegerField(primary_key=True)
    size_name = models.CharField(max_length=4)

    def __str__(self):
        return self.size_name

class Style(models.Model):
    style_id = models.IntegerField(primary_key=True)
    style_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.style_id) + " - " + str(self.style_name)

class Color(models.Model):
    color_id = models.IntegerField(primary_key=True)
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name

class Carton_QTY(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.quantity)

class Product(models.Model):
    GTIN_number = models.CharField(max_length=50, primary_key=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    carton_qty = models.ForeignKey(Carton_QTY,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.style) + " " + str(self.color) + " " + str(self.size)

class Pallet(models.Model):
    name = models.CharField(max_length=128)
    items = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Product_On_Pallet(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return "Pallet_ID: " + str(self.pallet.pk) + ", Item: " + str(self.item) + ", QTY: " + str(self.quantity)