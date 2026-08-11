from django.contrib import admin

from .models import Product, StockMovement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "quantity")
    search_fields = ("code", "name")


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "product",
        "movement_type",
        "quantity",
    )
    list_filter = ("movement_type", "created_at")
    search_fields = ("product__code", "product__name")
