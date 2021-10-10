from django.contrib import admin

from .models import Style,Size,Color,Carton_QTY,Product, Product_On_Pallet,Pallet

admin.site.register(Size)
admin.site.register(Style)
admin.site.register(Color)
admin.site.register(Carton_QTY)
admin.site.register(Product)
admin.site.register(Pallet)
admin.site.register(Product_On_Pallet)