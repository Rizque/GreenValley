from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .utils import searchProducts, paginateProducts


def products(request):
    products, search_query = searchProducts(request)
    products = products.order_by('-p_datums')
    custom_range, products = paginateProducts(request, products, 6)

    context = {'products': products,
               'search_query': search_query,  'custom_range': custom_range}
    return render(request, 'produkcija/products.html', context)

# def produkcija(request):
#     produkcija = Produkts.objects.all()
#     context = {'produkcija': produkcija}
#     return render(request, 'produkcija/produkcija.html', context)


# def produkts(request, pk):
#     produkts_k = Produkts.objects.get(id=pk)
#     context = {'produkts': produkts_k}
#     return render(request, 'produkcija/produkts.html', context)


def product(request, pk):
    projectObj = Product.objects.get(id=pk)
    # form = ReviewForm()

    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     review = form.save(commit=False)
    #     review.project = projectObj
    #     review.owner = request.user.profile
    #     review.save()

    #     projectObj.getVoteCount

    #     messages.success(request, 'Your review was successfully submited!')
    #     return redirect('project', pk=projectObj.id)

    return render(request, 'produkcija/product.html', {'product': projectObj})


@login_required(login_url='login')
def createProduct(request):
    profile = request.user.profile
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.saimnieciba = profile
            product.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'produkcija/product_form.html', context)


@login_required(login_url='login')
def updateProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'produkcija/product_form.html', context)


@login_required(login_url='login')
def deleteProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(id=pk)
    product.delete()
    return redirect('account')
# def deleteProduct(request, pk):
#     profile = request.user.profile
#     product = profile.product_set.get(id=pk)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('account')

#     context = {'object': product}
#     return render(request, 'delete_template.html', context)
