from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, ProductCategory
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .utils import searchProducts, paginateProducts
from django.db.models import Q


def products(request):
    products, search_query = searchProducts(request)
    product_order = request.GET.get('product_order')

    if product_order == 'price_asc':
        products = products.order_by('price')
    elif product_order == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('-date')

    custom_range, products = paginateProducts(request, products, 9)
    categories = ProductCategory.objects.all()

    context = {
        'products': products,
        'search_query': search_query,
        'custom_range': custom_range,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)


def product(request, pk):
    projectObj = Product.objects.get(product_id=pk)
    return render(request, 'products/product.html', {'product': projectObj})


def category_products(request, category_id):
    category = ProductCategory.objects.get(category_id=category_id)
    products = Product.objects.filter(category=category)
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/category.html', context)


@login_required(login_url='login')
def createProduct(request):
    profile = request.user.profile
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farm = profile
            product.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'products/product_form.html', context)


@login_required(login_url='login')
def updateProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(product_id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'products/product_form.html', context)


@login_required(login_url='login')
def deleteProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(product_id=pk)
    product.delete()
    return redirect('profile')
