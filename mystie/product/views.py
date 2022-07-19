from django.shortcuts import get_object_or_404, render
from .models import product
# Create your views here.

def product_list(request):
    products = product.objects.all()
    
    context = {
        "products" : list(products),
    }
    return render(request,"product/product_list.html",context)

def product_detail(request,id):
    
    selected_product = get_object_or_404(product,id=id)
    
    context = {
        "s_product" : selected_product
        
    }
    return render(request,"product/product_detail.html",context)

