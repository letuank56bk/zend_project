from django.db import models
from django.urls import reverse
# Import tất cả các function từ file custom_field
from shop.custom_field import *
# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from shop.define import *
from django.utils.timezone import now


# Create your models here.
class Order(models.Model):
    code = models.CharField(max_length=10)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20, choices=APP_VALUE_STATUS_ORDER_CHOICES,
                              default=APP_VALUE_STATUS_ORDER_DEFAULT)
    created = models.DateTimeField(default=now)

    class Meta:
        # Thay đổi tên hiển thị của model trong admin
        verbose_name_plural = TABLE_ORDER_SHOW

    # Thay đổi thông tin trả về trong phần thông báo trang admin
    def __str__(self):
        return self.name

