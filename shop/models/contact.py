from django.db import models
from django.urls import reverse

# Import tất cả các function từ file custom_field
from shop.custom_field import *

# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from shop.define import *

from django.utils.timezone import now


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    contacted = CustomBooleanFieldContact()
    message_admin = models.TextField(blank=True)
    created = models.DateTimeField(default=now)

    class Meta:
        # Thay đổi tên hiển thị của model trong admin
        verbose_name_plural = TABLE_CONTACT_SHOW

    # Thay đổi thông tin trả về trong phần thông báo trang admin
    def __str__(self):
        return self.name
