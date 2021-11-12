from django.http import Http404
from django.shortcuts import render,  get_object_or_404, get_list_or_404, redirect
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

def return_to_search():
    context = {}
    context['style'] = Style.objects.all()
    context['color'] = Color.objects.all()
    context['size'] = Size.objects.all()

    return context



# First page of the search item process
def search_item_page1(request):
    context = return_to_search()

    return render(request, 'main/search/item/page1.html',context)


# Second page of the search item process
def search_item_page2(request):

    context = {}

    x = request.GET['barcode']
    x = (str(x).rjust(14, '0'))
    try:
        id = get_object_or_404(Product, pk=x)
    except Http404:
        context = return_to_search()

        return render(request, 'main/search/item/page1.html', context)

    context["item"] = id
    context['products'] = Products_On_Pallets.objects.filter(product = id)

    return render(request, 'main/search/item/page2results.html', context)

def search_get_item(request):

    context = {}

    style = request.GET['styleSelect']
    color = request.GET['colorSelect']
    size = request.GET['sizeSelect']

    if style == "" or color == "" or size == "":
        context = return_to_search()
        return render(request, 'main/search/item/page1.html', context)

    color = (str(color).rjust(3, '0'))

    try:
        id = get_object_or_404(Product, style_id=int(style), color_id=int(color),size_id=int(size))
    except Http404:
        context = return_to_search()
        return render(request, 'main/search/item/page1.html', context)

    context["item"] = id
    context['products'] = Products_On_Pallets.objects.filter(product = id)

    return render(request, 'main/search/item/page2results.html', context)

# Third page of the search item process
def search_item_page3(request, item_id):
    p = Products_On_Pallets.objects.get(id=item_id)

    product = p.product
    content = {
        "item":p,
        "product":product
    }
    return render(request, 'main/search/item/page3New.html', content)

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

    context["item"] = product
    context["products"] = Products_On_Pallets.objects.filter(product = id)

    return render(request, 'main/search/item/page2results.html', context)

# Third page of the search item process
def search_pallet(request):
    return render(request, 'main/search/pallet/page1.html')
    
# Third page of the search item process
def search_pallet_detail(request):
    context = {}

    location = request.POST['value']
    try:
        id = get_object_or_404(Pallets, location=location)
    except Http404:
        return render(request, 'main/search/pallet/page1.html')

    context["item"] = id
    context['products'] = Products_On_Pallets.objects.filter(pallet=id)

    return render(request, 'main/search/pallet/page2.html',context)

# Third page of the search item process
def search_pallet_edit(request, item_id):
    p = Products_On_Pallets.objects.get(id=item_id)

    product = p.product
    content = {
        "item": p,
        "product": product
    }

    return render(request, 'main/search/pallet/page3New.html',content)

# Third page of the search item process
def search_pallet_save(request, item_id):
    context = {}
    x = request.POST['value']

    pop = Products_On_Pallets.objects.get(id=item_id)
    pallet = pop.pallet
    id = pallet.pk
    if int(x) <= 0:
        pop.delete()
    else:
        pop.qty = x
        pop.save()
    context["item"] = pallet
    context["products"] = Products_On_Pallets.objects.filter(pallet=id)

    return render(request, 'main/search/pallet/page2.html', context)


#====================================================================
#===================ADD PALLET=======================================
#====================================================================

# Third page of the search item process
def addPallet_page1(request):
    context = {}
    #create session vars
    request.session["item"] = []
    request.session["location"] = ""
    #send empty vars to html
    context["item"] = []
    context["location"] = ""

    return render(request, 'main/addPallet/page1New2.html', context)
    
# Third page of the search item process
def addPallet_add(request):
    return render(request, 'main/addPallet/page2New.html')

# Third page of the search item process
def addPallet_add_item(request):
    context = {}

    x = request.POST['barcode']
    x = (str(x).rjust(14, '0'))

    try:
        item = get_object_or_404(Product, pk=x)
    except Http404:
        return render(request, 'main/addPallet/page2New.html')

    context["item"] = item



    return render(request, 'main/addPallet/page3New.html', context)

def addPallet_edit(request):


    return render(request, 'main/addPallet/page2New.html')

def addPallet_location(request):
    context = {}
    value = request.POST['value']
    request.session["location"] = value
    context["item"] = request.session["item"]
    context["location"] = value

    return render(request, 'main/addPallet/page1New2.html', context)


def addPallet_add_save(request, id):
    context = {}
    id = (str(id).rjust(14, '0'))
    value = request.POST['value']
    item = get_object_or_404(Product, pk=id)
    #Update item list
    pallet_items = request.session["item"]

    pallet_items.append((str(item),value,item.pk))
    request.session["item"] = pallet_items

    location = request.session["location"]

    context["item"] = pallet_items
    context["location"] = location
    return render(request, 'main/addPallet/page1New2.html',context)

def addPallet_save(request):
    location = request.session["location"]
    pallet_items = request.session["item"]
    #not alowed to create an empty pallet
    if not pallet_items:
        context = {}
        context["item"] = pallet_items
        context["location"] = location
        return render(request, 'main/addPallet/page1New2.html', context)
    #check if location was entered
    if location:
        pallet = Pallets(location = location)
    else:
        pallet = Pallets()
    pallet.save()

    for item in pallet_items:
        prod = get_object_or_404(Product, pk=item[2])
        value = int(item[1])
        pop = Products_On_Pallets(product = prod, pallet=pallet, qty=value)
        pop.save()


    return redirect(home)


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

