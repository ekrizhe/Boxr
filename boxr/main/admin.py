from django.contrib import admin

from .models import Style,Size,Color,Carton_QTY, Product,Pallets,Products_On_Pallets

admin.site.register(Size)
admin.site.register(Style)
admin.site.register(Color)
admin.site.register(Carton_QTY)
admin.site.register(Product)
admin.site.register(Pallets)
admin.site.register(Products_On_Pallets)