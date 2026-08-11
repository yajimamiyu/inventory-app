from django.db import models


class Product(models.Model):
    code = models.CharField("商品コード", max_length=50, unique=True)
    name = models.CharField("商品名", max_length=100)
    quantity = models.IntegerField("在庫数", default=0)

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ("IN", "入庫"),
        ("OUT", "出庫"),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="商品",
    )
    movement_type = models.CharField(
        "種別",
        max_length=3,
        choices=MOVEMENT_TYPES,
    )
    quantity = models.PositiveIntegerField("数量")
    created_at = models.DateTimeField("日時", auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.get_movement_type_display()}"

