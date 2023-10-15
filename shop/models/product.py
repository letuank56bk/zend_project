from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

# Import tất cả các function từ file helper
from shop.helpers import *

# Import tất cả các function từ file custom_field
from shop.custom_field import *

# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from shop.define import *
from .category import Category
from .planting_method import PlantingMethod


# Create your models here.
class Product(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    price_sale = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    # nếu có giá sale --> price_real = price_sale, nếu không có price_real = price
    price_real = models.DecimalField(max_digits=10, decimal_places=0, editable=False)
    total_sold = models.IntegerField(default=0, editable=False)
    summary = models.TextField()
    content = HTMLField()
    # Thay đổi tên file và upload lên thư mục được chỉ định
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Tạo mối quan hệ nhiều - nhiều với bảng planting method
    planting_methods = models.ManyToManyField(PlantingMethod)

    class Meta:
        # Thay đổi tên hiển thị của model trong admin
        verbose_name_plural = TABLE_PRODUCT_SHOW

    # Thay đổi thông tin trả về trong phần thông báo trang admin
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # article_slug --> là phần slug ở bên views, phần này sẽ được truyền giá trị slug đã nhập trong DB
        return reverse("product", kwargs={"product_slug": self.slug, "product_id": self.id})

    # Tự động gán giá trị cho price_real mỗi khi người dùng lưu thông tin
    def save(self, *args, **kwargs):
        # Phần xử lý viết ở đây
        if self.price_sale:
            self.price_real = self.price_sale
        else:
            self.price_real = self.price

        super().save(*args, **kwargs)
