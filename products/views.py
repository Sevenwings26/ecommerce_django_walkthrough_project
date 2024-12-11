from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm
# from .models import *

# from django.http import JsonResponse
from .models import Product


# CRUD operation 
# create/upload product
@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Associate product with logged-in user
            product.save()
            messages.success(request, "Product uploaded successfully!")
            return redirect('index')  # Replace with your desired redirect URL
    else:
        form = ProductForm()

    return render(request, 'pages/product-page/upload_product.html', {'form': form})

# List Products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'pages/product-page/product_list.html', {'products': products})


# Update Product
# @login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'pages/product-page/product_update.html', {'form': form})

# Delete Product
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'pages/product-page/product_confirm_delete.html', {'product': product})

