from django.urls import path

from . import views


urlpatterns = [
    path("products/", views.product_list, name="product_list"),

    path(
        "products/<int:product_id>/in/",
        views.stock_in,
        name="stock_in",
    ),

    path(
        "products/<int:product_id>/out/",
        views.stock_out,
        name="stock_out",
    ),

    path(
        "movements/",
        views.movement_list,
        name="movement_list",
    ),
]
