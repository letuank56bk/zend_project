from django.contrib import admin

# Register your models here.
# import tất cả các class model trong folder models thông qua file __init__
from .models import Category, Product, PlantingMethod

# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from .define import *


# Custom trang category trong admin
class CategoryAdmin(admin.ModelAdmin):
    # list_display --> danh sách các cột sẽ hiển thị trong view admin
    list_display = ('name', 'status', 'is_homepage', 'ordering')
    # list_filter --> tạo bộ lọc với các trường được liệt kê
    list_filter = ['status', 'is_homepage']
    # search_fields --> tạo thêm ô tìm kiếm theo cột name
    search_fields = ["name"]

    # Tự động sinh ra slug từ tên của category (sẽ có lỗi xảy ra nếu tên category là tiếng việt có dấu)
    # --> prepopulated_fields = {'slug': ('name',)}
    # custome tạo slug tự động, loại bỏ lỗi đối với tiếng việt
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS


# Custom trang product trong admin
class ProductAdmin(admin.ModelAdmin):
    # list_display --> danh sách các cột sẽ hiển thị trong view admin
    list_display = (
        'name', 'status', 'ordering', 'special', 'price', 'price_sale', 'price_real', 'get_planting_methods',
        'total_sold')
    # list_filter --> tạo bộ lọc với các trường được liệt kê
    list_filter = ['status', 'special', 'planting_methods', ]
    # search_fields --> tạo thêm ô tìm kiếm theo cột name
    search_fields = ["name"]

    # Tự động sinh ra slug từ tên của product (sẽ có lỗi xảy ra nếu tên category là tiếng việt có dấu)
    # --> prepopulated_fields = {'slug': ('name',)}
    # general js trong ADMIN_SRC_JS sẽ custom tạo slug tự động, loại bỏ lỗi đối với tiếng việt
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

    def get_planting_methods(self, obj):
        # obj là từng phần tử trong product.
        methods = [method.name for method in obj.planting_methods.all()]
        # ['Đất nền', 'Thủy sinh'] --> 'Đất nền, Thủy sinh'
        return ', '.join(methods)

    # Định nghĩa lại tên cột trong bảng admin thông qua short_description
    get_planting_methods.short_description = "planting method"


# Thêm view Category/ CategoryAdmin vào trang admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PlantingMethod)

admin.site.site_header = ADMIN_HEADER_NAME
