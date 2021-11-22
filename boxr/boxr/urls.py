"""boxr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Pattern
from django.contrib import admin
from django.urls import path, include
from main.views import ListView
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('search/home', views.search_home),

    # Search Item
    path('search/item', views.search_item_intial, name='search-item-inital'),
    path('search/item/barcode', views.search_item_getbarcode, name='search-item-getbarcode'),
    path('search/item/SCS', views.search_item_getSCS, name='search-item-getSCS'),
    path('search/item/<str:item_id>', views.search_item_display, name='search-item-display'),
    path('search/item/edit/<int:item_id>', views.search_item_edit, name='edit-item'),
    path('search/item/save/<int:item_id>', views.search_item_edit_value, name='search-item-save'),
    path('search/item/size/<int:change_type>', views.search_item_size_change, name='search-item-size-change'),

    # Search Pallet search_pallet_additem
    path('search/pallet', views.search_pallet, name="searchpallet"),
    path('search/pallet/barcode', views.search_pallet_barcode, name="searchpallet-barcode"),
    path('search/pallet/<int:item_id>', views.search_pallet_detail, name="searchpallet-detail"),
    path('search/pallet/edit/<int:item_id>', views.search_pallet_edit, name="searchpallet-edit"),
    path('search/pallet/save/<int:item_id>', views.search_pallet_save, name="searchpallet-save"),
    path('search/pallet/delete/<int:item_id>', views.search_pallet_delete, name="searchpallet-delete"),
    path('search/pallet/add', views.search_pallet_add, name="searchpallet-add"),
    path('search/pallet/add/qty', views.search_pallet_additem, name="searchpallet-additem"),
    path('search/pallet/add/<int:item_id>', views.search_pallet_addsave, name="searchpallet-addsave"),
    path('search/pallet/edit/location', views.search_pallet_editlocation, name="searchpallet-editlocation"),
    path('search/pallet/edit/location/<str:id>', views.search_pallet_editlocation_save, name="searchpallet-editlocationsave"),

    # Add Pallet
    path('addPallet', views.addPallet_page1),
    path('addPallet/add', views.addPallet_add, name="addpallet-add"),
    path('addPallet/add/1', views.addPallet_add_item, name="addpallet-add-item"),
    path('addPallet/add/save/<int:id>', views.addPallet_add_save, name="addpallet-add-save"),
    path('addPallet/save', views.addPallet_save, name="addpallet-save"),
    path('addPallet/edit', views.addPallet_edit, name="addpallet-edit"),
    path('addPallet/location', views.addPallet_location, name="addpallet-location"),

    #Locations
    path('locations', views.locations_display, name="location-display"),

    # Restock Requests
    path('restockRequest/page1', views.restockRequest_page1),
    path('restockRequest/page2', views.restockRequest_page2),
    path('restockRequest/page3', views.restockRequest_page3)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
