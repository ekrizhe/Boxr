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

class Pallets(models.Model):
    products = models.ManyToManyField(Product, through="Products_On_Pallets")

    def __str__(self):
        return str(self.pk)

class Products_On_Pallets(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallets, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pallet.pk) + " " + str(self.product) + " QTY: " + str(self.qty)




