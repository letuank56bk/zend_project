from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

# Import tất cả các function từ file helper
from news.helpers import *

# Import tất cả các function từ file custom_field
from news.custom_field import *

# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from news.define import *
from .category import Category


# Create your models here.
class Article(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField()
    # Thay đổi tên file và upload lên thư mục được chỉ định
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        # Thay đổi tên hiển thị của model trong admin
        verbose_name_plural = TABLE_ARTICLE_SHOW

    # Thay đổi thông tin trả về trong phần thông báo trang admin
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # article_slug --> là phần slug ở bên views, phần này sẽ được truyền giá trị slug đã nhập trong DB
        return reverse("article", kwargs={"article_slug": self.slug, "article_id": self.id})
