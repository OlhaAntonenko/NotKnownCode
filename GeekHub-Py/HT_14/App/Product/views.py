from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from Product.models import ProductModel
from Product.forms import ProductModelForm


def all_products(req):
    return render(req, 'product/all_products.html',
                  {'products': ProductModel.objects.filter(is_active=True)})


def product_info(req, pid):
    return render(req, 'product/product_info.html',
                  {'product': get_object_or_404(ProductModel, id=pid)})


def create_product(req):
    form = ProductModelForm(req.POST or None)

    if req.POST and form.is_valid():
        product = form.save(commit=True)
        return redirect(reverse('product_info', args=(product.id, )))

    return render(req, 'product/create_product.html', {'form': form})


def delete_product(req, pid):
    if req.POST:
        ProductModel.objects.filter(id=pid).delete()
    return redirect(reverse('all_product'))


def update_product(req, pid):
    if req.POST:
        product = ProductModel.objects.filter(id=pid)
        action = req.POST.get('action')
        if action == 'Activate':
            product.update(is_active=True)
        elif action == 'Deactivate':
            product.update(is_active=False)

    return redirect(reverse('product_info', args=(ProductModel.objects.get(id=pid).id, )))
