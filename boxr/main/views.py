from django.shortcuts import render
from .models import Style,Size,Color,Carton_QTY,Product,Pallets,Products_On_Pallets
from django.views.generic import ListView

# This will be our login screen
def login(request):
    return render(request, 'main/login.html')

# This will be the home screen that consists of Search, Add Pallet, Locations, and Fill Requests
def home(request):
    return render(request, 'main/home.html')

# This will be the screen that with the Item and Pallet buttons
def search_home(request):
    return render(request, 'main/search/home.html')

#====================================================================
#===================SEARCH===========================================
#====================================================================

# First page of the search item process
def search_item_page1(request):
    return render(request, 'main/search/item/page1.html')

#
class ListView(ListView):

    model = Products_On_Pallets
    template_name = 'main/search/item/page2.html'
    context_object_name = 'products'
    queryset = Products_On_Pallets.objects.filter(product = '00051054000027')
    ordering = ['pallet']

# Second page of the search item process
def search_item_page2(request, product_id):
    p = Products_On_Pallets.objects.filter(product = product_id)

    return render(request, 'main/search/item/page2.html', {'products':p})

# Third page of the search item process
def search_item_page3(request):
    return render(request, 'main/search/item/page3.html')

# Third page of the search item process
def search_pallet_page1(request):
    return render(request, 'main/search/pallet/page1.html')
    
# Third page of the search item process
def search_pallet_page2(request):
    return render(request, 'main/search/pallet/page2.html')

# Third page of the search item process
def search_pallet_page3(request):
    return render(request, 'main/search/pallet/page3.html')

# Third page of the search item process
def search_pallet_page4(request):
    return render(request, 'main/search/pallet/page4.html')

#====================================================================
#===================ADD PALLET=======================================
#====================================================================

# Third page of the search item process
def addPallet_page1(request):
    return render(request, 'main/addPallet/page1.html')
    
# Third page of the search item process
def addPallet_page2(request):
    return render(request, 'main/addPallet/page2.html')

# Third page of the search item process
def addPallet_page3(request):
    return render(request, 'main/addPallet/page3.html')

# Third page of the search item process
def addPallet_page4(request):
    return render(request, 'main/addPallet/page4.html')

#====================================================================
#===================LOCATIONS========================================
#====================================================================

def locations_page1(request):
    return render(request, 'main/locations/page1.html')

#====================================================================
#===================RESTOCK REQUEST==================================
#====================================================================

def restockRequest_page1(request):
    return render(request, 'main/restockRequest/page1.html')

def restockRequest_page2(request):
    return render(request, 'main/restockRequest/page2.html')

def restockRequest_page3(request):
    return render(request, 'main/restockRequest/page3.html')

