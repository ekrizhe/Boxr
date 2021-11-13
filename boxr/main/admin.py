from django.contrib import admin

<<<<<<< HEAD
from .models import Style,Size,Color,Carton_QTY, Product,Pallets,Products_On_Pallets,Locations,Restock
=======
from .models import Style,Size,Color,Carton_QTY, Product,Pallets,Products_On_Pallets,Location,Restock
>>>>>>> b30635326b63aa558b510fd0b321f95ed74d7bf0

admin.site.register(Size)
admin.site.register(Style)
admin.site.register(Color)
admin.site.register(Carton_QTY)
admin.site.register(Product)
admin.site.register(Pallets)
admin.site.register(Products_On_Pallets)
<<<<<<< HEAD
admin.site.register(Locations)
=======
admin.site.register(Location)
>>>>>>> b30635326b63aa558b510fd0b321f95ed74d7bf0
admin.site.register(Restock)