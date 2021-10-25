from django.http import Http404
from django.shortcuts import render,  get_object_or_404, get_list_or_404
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

def search_item_detail(request,id):
    context = {}
    id = (str(id).rjust(14, '0'))
    context["id"] = id
    context["products"] = Products_On_Pallets.objects.filter(product = id)

    return render(request, "main/search/item/page2.html", context)

# First page of the search item process
def search_item_page1(request):

    return render(request, 'main/search/item/page1.html')


# Second page of the search item process
def search_item_page2(request):

    context = {}

    x = request.GET['barcode']
    try:
        id = get_object_or_404(Product, pk=x)
    except Http404:
        return render(request, 'main/search/item/page1.html')

    context["item"] = id
    context['products'] = Products_On_Pallets.objects.filter(product = id)

    return render(request, 'main/search/item/page2.html', context)

# Third page of the search item process
def search_item_page3(request, item_id):
    p = Products_On_Pallets.objects.get(id=item_id)

    product = p.product
    content = {
        "item":p,
        "product":product
    }
    return render(request, 'main/search/item/page3.html', content)

def search_item_edit_value(request, item_id):
    context = {}
    x = request.POST['value']

    pop = Products_On_Pallets.objects.get(id=item_id)
    product = pop.product
    id = product.pk
    if int(x) <= 0:
        pop.delete()
    else:
        pop.qty = x
        pop.save()

    #print(product.pk)
    context["products"] = Products_On_Pallets.objects.filter(product = id)

    return render(request, 'main/search/item/page2.html', context)

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

