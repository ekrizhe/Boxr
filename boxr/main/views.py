from django.http import Http404
from django.shortcuts import render,  get_object_or_404, get_list_or_404, redirect
from .models import Style,Size,Color,Carton_QTY,Product,Pallets,Products_On_Pallets, Restock, Locations
from django.views.generic import ListView
from django.contrib.auth import authenticate, login

def verifyUser(request, renderObj):
    if(request.user is None or request.user.is_authenticated == False):
        print("Redirecting!")
        return redirect("/accounts/login")
    else:
        print("Rendering!")
        return renderObj

# This will be our login screen
def loginDirect(request):
    if(request.user.is_authenticated == True):
        return redirect("/home")
    else:
        return redirect("/accounts/login")
    

# This will be the home screen that consists of Search, Add Pallet, Locations, and Fill Requests
def home(request):
    if(request.user.is_authenticated == False):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
        request.user = user

    return verifyUser(request, render(request, 'main/home.html'))

# This will be the screen that with the Item and Pallet buttons
def search_home(request):
    return verifyUser(request, render(request, 'main/search/home.html'))

def test(request):
    return verifyUser(request, render(request, 'main/search/pallet/asearch.html'))

#====================================================================
#===================SEARCH ITEM======================================
#====================================================================


def return_to_search():
    context = {}
    context['style'] = Style.objects.all()
    context['color'] = Color.objects.all()
    context['size'] = Size.objects.all()

    return context


# First page of the search item process
def search_item_intial(request):
    context = return_to_search()

    return verifyUser(request, render(request, 'main/search/item/search_item_search.html',context))

# display search result
def search_item_display(request, item_id):
    context = {}

    id = get_object_or_404(Product, pk=item_id)

    context["item"] = id
    context['products'] = Products_On_Pallets.objects.filter(product=id)

    request.session["current_product"] = id.pk

    return verifyUser(request, render(request, 'main/search/item/search_item_display.html', context))

# processes barcode
def search_item_getbarcode(request):

    x = request.GET['barcode']
    x = (str(x).rjust(14, '0'))
    try:
        id = get_object_or_404(Product, pk=x)
    except Http404:
        context = return_to_search()

        return verifyUser(request, render(request, 'main/search/item/search_item_search.html', context))

    gtin = id.pk

    return verifyUser(request, redirect("search-item-display", item_id=gtin))

# processes search by style, color, size
def search_item_getSCS(request):

    style = request.POST['styleSelect']
    color = request.POST['colorSelect']
    size = request.POST['sizeSelect']

    if style == "" or color == "" or size == "":
        context = return_to_search()
        return verifyUser(request,  render(request, 'main/search/item/search_item_search.html', context))

    color = (str(color).rjust(3, '0'))

    try:
        id = get_object_or_404(Product, style_id=int(style), color_id=int(color),size_id=int(size))
    except Http404:
        context = return_to_search()
        return verifyUser(request, render(request, 'main/search/item/search_item_search.html', context))

    gtin = id.pk

    return verifyUser(request, redirect("search-item-display",item_id=gtin))


# Third page of the search item process
def search_item_edit(request, item_id):
    p = Products_On_Pallets.objects.get(id=item_id)

    product = p.product
    content = {
        "item":p,
        "product":product
    }
    return verifyUser(request, render(request, 'main/search/item/search_item_edit.html', content))

def search_item_edit_value(request, item_id):
    context = {}
    x = request.POST['value']

    if x == "":
        return verifyUser(request, redirect("edit-item", item_id=item_id))

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

    return verifyUser(request, redirect("search-item-display",item_id=id))


def search_item_size_change(request, change_type):
    item_id = request.session["current_product"]
    item = get_object_or_404(Product, pk=item_id)
    #if change type is 1 then the size goes up by one
    if change_type:
        size = item.size.pk + 1
    else:
        size = item.size.pk - 1
    #if next size object exists then display else return original object
    try:
        new_item = get_object_or_404(Product, style_id=item.style, color_id=item.color, size_id=size)
    except Http404:
        return verifyUser(request, redirect("search-item-display", item_id=item_id))

    return verifyUser(request, redirect("search-item-display",item_id=new_item.pk))




#====================================================================
#===================SEARCH PAllET====================================
#====================================================================

# Third page of the search item process
def search_pallet(request):
    request.session["pallet_pk"] = ""

    context = {}

    context["floor_pallets"] = Pallets.objects.filter(location="Floor")
    floor_pallets_product = []
    for pallet in context["floor_pallets"]:
        product_list = Products_On_Pallets.objects.filter(pallet=pallet)
        floor_pallets_product.append((pallet,list(product_list)))

    context["floor_pallets_product"] = floor_pallets_product
    return verifyUser(request, render(request, 'main/search/pallet/search_pallet_search.html', context))

def search_pallet_detail(request, item_id):
    context = {}
    request.session["pallet_pk"] = item_id
    id = get_object_or_404(Pallets, pk=item_id)

    context["item"] = id
    context['products'] = Products_On_Pallets.objects.filter(pallet=id)

    return verifyUser(request, render(request, 'main/search/pallet/search_pallet_detail.html',context))

# Third page of the search item process
def search_pallet_barcode(request):

    location = request.POST['value']
    print(location)
    try:
        id = get_object_or_404(Locations, name=location)
    except Http404:
        return redirect("searchpallet")
    if id.pallet == None:
        return redirect("searchpallet")

    return verifyUser(request, redirect("searchpallet-detail",item_id=id.pallet.id))

# Third page of the search item process
def search_pallet_edit(request, item_id):
    p = Products_On_Pallets.objects.get(id=item_id)

    product = p.product
    content = {
        "item": p,
        "product": product
    }

    return verifyUser(request, render(request, 'main/search/pallet/search_pallet_edit.html',content))

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

    return redirect("searchpallet-detail", item_id=id)

def search_pallet_delete(request, item_id):
    context = {}
    id = get_object_or_404(Pallets, pk=item_id)
    id.delete()

    return redirect("searchpallet")

def search_pallet_add(request):
    return verifyUser(request, render(request, 'main/search/pallet/search_pallet_itemadd.html'))

def search_pallet_additem(request):
    context = {}

    x = request.POST['barcode']
    x = (str(x).rjust(14, '0'))

    try:
        item = get_object_or_404(Product, pk=x)
    except Http404:
        return verifyUser(request, render(request, 'main/search/pallet/search_pallet_itemadd.html'))

    context["item"] = item
    return verifyUser(request, render(request, 'main/search/pallet/search_pallet_itemqty.html',context))


def search_pallet_addsave(request, item_id):
    item_id = (str(item_id).rjust(14, '0'))

    id = request.session["pallet_pk"]
    value = request.POST['value']
    pallet = get_object_or_404(Pallets, pk=id)
    item = get_object_or_404(Product, pk=item_id)

    pop = Products_On_Pallets(product=item,pallet=pallet,qty=value)
    pop.save()


    return verifyUser(request,redirect("searchpallet-detail", item_id=id))

def search_pallet_editlocation(request):
    context = {}
    context["locations"] = Locations.objects.filter(pallet=None)
    return verifyUser(request, render(request, 'main/search/pallet/search_pallet_editlocation.html', context))

def search_pallet_editlocation_save(request, id):

    pallet_id = request.session["pallet_pk"]
    pallet = get_object_or_404(Pallets, pk=pallet_id)
    pallet.location = id
    #clear old location
    try:
        if pallet.locations:
            loc = Locations.objects.get(pk=pallet.locations)
            loc.pallet = None
            loc.save()
    except:
        print("")
    loc = Locations.objects.get(pk=id)
    loc.pallet = pallet
    loc.save()
    pallet.save()


    return redirect("searchpallet-detail", item_id=pallet_id)


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

    return verifyUser(request, render(request, 'main/addPallet/page1New2.html', context))

#
def addPallet_detail(request):
    context = {}
    context["item"] = request.session["item"]
    context["location"] = request.session["location"]

    return verifyUser(request, render(request, 'main/addPallet/page1New2.html', context))
    
# Third page of the search item process
def addPallet_add(request):
    return verifyUser(request, render(request, 'main/addPallet/page2New.html'))

# Third page of the search item process
def addPallet_add_item(request):
    context = {}

    x = request.POST['barcode']
    x = (str(x).rjust(14, '0'))

    try:
        item = get_object_or_404(Product, pk=x)
    except Http404:
        return verifyUser(request, render(request, 'main/addPallet/page2New.html'))

    context["item"] = item

    return verifyUser(request, render(request, 'main/addPallet/addpallet_add_qty.html', context))


def addPallet_add_save(request, id):
    context = {}

    id = (str(id).rjust(14, '0'))
    item = get_object_or_404(Product, pk=id)
    value = request.POST['value']

    if value == '' or int(float(value)) <= 0:
        context["item"] = item
        return verifyUser(request,render(request, 'main/addPallet/addpallet_add_qty.html', context))
    value = int(float(value))

    #Update item list
    pallet_items = request.session["item"]

    pallet_items.append((str(item),value,item.pk))
    request.session["item"] = pallet_items

    location = request.session["location"]

    context["item"] = pallet_items
    context["location"] = location

    return verifyUser(request,redirect("addPallet-detail"))

def addPallet_edit(request, id):
    context = {}
    pallet_items = request.session["item"]
    item = pallet_items[int(id)]
    context["item"] = item[0]
    context["qty"] = item[1]
    context["pk"] = id
    return verifyUser(request,render(request, 'main/addPallet/addpallet_edit.html',context))

def addPallet_edit_save(request, id):
    context = {}
    pallet_items = request.session["item"]
    item = pallet_items[int(id)]
    value = request.POST['value']

    if value == '' or int(float(value)) < 0:
        return redirect('addpallet-edit', id)
    value = int(float(value))
    if value == 0:
        del pallet_items[int(id)]
        request.session["item"] = pallet_items
    else:
        item[1] = value
        pallet_items[int(id)] = item
        print(pallet_items[int(id)])
        request.session["item"] = pallet_items

    return verifyUser(request,redirect("addPallet-detail"))

def addPallet_location(request):
    context = {}
    value = request.POST['value']
    try:
        loc = get_object_or_404(Locations, pk=value)
    except Http404:
        request.session["location"] = "Floor"
        return redirect("addPallet-detail")

    if loc.pallet:
        request.session["location"] = "Floor"
    else:
        request.session["location"] = value

    return verifyUser(request, redirect("addPallet-detail"))


def addPallet_save(request):
    location = request.session["location"]
    if not location:
        location = "Floor"
    pallet_items = request.session["item"]
    #not alowed to create an empty pallet
    if not pallet_items:
        return verifyUser(request, redirect("addPallet-detail"))
    #check if location was entered
    if location != "Floor":
        pallet = Pallets(location = location)
        pallet.save()
        loc = Locations.objects.get(pk=location)
        loc.pallet = pallet
        loc.save()
    else:
        pallet = Pallets()
        pallet.save()


    for item in pallet_items:
        prod = get_object_or_404(Product, pk=item[2])
        value = int(item[1])
        pop = Products_On_Pallets(product = prod, pallet=pallet, qty=value)
        pop.save()


    return verifyUser(request,redirect(home))


#====================================================================
#===================LOCATIONS========================================
#====================================================================

def locations_display(request):
    context = {}
    context["location"] = Locations.objects.all().order_by('name')

    return verifyUser(request, render(request, 'main/locations/locations_display.html', context))


#====================================================================
#===================RESTOCK REQUEST==================================
#====================================================================

def restockRequest_page1(request):
    context = {}
    context["product"] = Restock.objects.all()
    return verifyUser(request, render(request, 'main/restockRequest/page1.html', context))

def restockRequest_page2(request):
    item_id = request.session["current_product"]
    item = get_object_or_404(Product, pk=item_id)

    try:
        get_object_or_404(Restock, product=item)
    except Http404:
        re = Restock(product=item)
        re.save()

    return verifyUser(request, redirect("search-item-display", item_id=item_id))

def restockRequest_del(request, id):
    item_id = id

    item = get_object_or_404(Product, pk=item_id)
    re = get_object_or_404(Restock, product=item)
    re.delete()

    return verifyUser(request, redirect("search-item-display", item_id=item_id))


