from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, StockMovement


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "inventory/product_list.html",
        {"products": products}
    )


def stock_in(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        quantity = int(request.POST["quantity"])

        if quantity > 0:
            product.quantity += quantity
            product.save()

            StockMovement.objects.create(
                product=product,
                movement_type="IN",
                quantity=quantity,
            )

    return redirect("product_list")


def stock_out(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        quantity = int(request.POST["quantity"])

        if 0 < quantity <= product.quantity:
            product.quantity -= quantity
            product.save()

            StockMovement.objects.create(
                product=product,
                movement_type="OUT",
                quantity=quantity,
            )

    return redirect("product_list")

def movement_list(request):
    movements = StockMovement.objects.select_related("product").order_by(
        "-created_at"
    )

    return render(
        request,
        "inventory/movement_list.html",
        {"movements": movements},
    )
