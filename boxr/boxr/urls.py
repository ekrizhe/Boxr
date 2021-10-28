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
    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('search/home', views.search_home),

    # Search Item
    path('search/item/page1', views.search_item_page1),
    path('search/item/page2', views.search_item_page2, name='view-item2'),
    path('search/item/edit/<int:item_id>', views.search_item_page3, name='edit-item'),
    path('search/item/<int:id>', views.search_item_detail, name='search-item-detail'),
    path('search/item/save/<int:item_id>', views.search_item_edit_value, name='search-item-save'),

    # Search Pallet
    path('search/pallet/page1', views.search_pallet_page1),
    path('search/pallet/page2', views.search_pallet_page2),
    path('search/pallet/page3', views.search_pallet_page3),
    path('search/pallet/page4', views.search_pallet_page4),

    # Add Pallet
    path('addPallet/page1', views.addPallet_page1),
    path('addPallet/page2', views.addPallet_page2),
    path('addPallet/page3', views.addPallet_page3),
    path('addPallet/page4', views.addPallet_page4),

    #Locations
    path('locations/page1', views.locations_page1),

    # Restock Requests
    path('restockRequest/page1', views.restockRequest_page1),
    path('restockRequest/page2', views.restockRequest_page2),
    path('restockRequest/page3', views.restockRequest_page3)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
