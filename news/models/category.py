from django.db import models
from django.urls import reverse

# Import tất cả các function từ file custom_field
from news.custom_field import *

# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from news.define import *


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)

    class Meta:
        # Thay đổi tên hiển thị của model trong admin
        verbose_name_plural = TABLE_CATEGORY_SHOW

    # Thay đổi thông tin trả về trong phần thông báo trang admin
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # category_slug --> là phần slug ở bên views, phần này sẽ được truyền giá trị slug đã nhập trong DB
        return reverse("category", kwargs={"category_slug": self.slug})