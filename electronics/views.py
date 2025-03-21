from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from .forms import ProductForm # Importing the Product model from the models.py file.
# Create your views here.

def product_details(request):
    prod = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_details')
    else:
        form = ProductForm()
        
    return render(
        request, 'electronics/product_details.html', 
                  {'prod': prod, 'form': form},
                  )

def update_product(request, id):
    prod = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('product_details')
    else:
        form = ProductForm(instance=prod)

    return render(
        request, 'electronics/update_product.html', 
                  {'prod': prod, 'form': form},
                  )

def delete_product(request, id):
    prod = get_object_or_404(Product, id=id)
    prod.delete()
    return redirect('product_details')