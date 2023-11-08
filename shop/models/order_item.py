from django.db import models
from django.urls import reverse
# Import tất cả các function từ file custom_field
from shop.custom_field import *
# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from shop.define import *
from django.utils.timezone import now
from .product import Product
from .order import Order


# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    total = models.DecimalField(max_digits=10, decimal_places=0)

    # Thay đổi thông tin trả về trong phần thông báo trang admin
    def __str__(self):
        return ""

    class Meta:
        # Thay đổi tên hiển thị của model trong admin
        verbose_name_plural = TABLE_ORDER_ITEM_SHOW
