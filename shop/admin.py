from django.contrib import admin

# Register your models here.
# import tất cả các class model trong folder models thông qua file __init__
from .models import Category, Product, PlantingMethod

# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from .define import *
from .helpers import *

# Thư viện hỗ trợ format HTML
from django.utils.html import format_html


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
    list_display = ('display_image', 'name', 'status', 'ordering', 'special', 'price_formatted', 'price_sale_formatted',
                    'price_real_formatted', 'get_planting_methods', 'total_sold')
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

    @admin.display(description="planting_method")
    def get_planting_methods(self, obj):
        # obj là từng phần tử trong product.
        methods = [method.name for method in obj.planting_methods.all()]
        # ['Đất nền', 'Thủy sinh'] --> 'Đất nền, Thủy sinh'
        return ', '.join(methods)

    # C1: Định nghĩa lại tên cột trong bảng admin thông qua short_description
    # get_planting_methods.short_description = "planting method"

    # @admin.display(description="price") --> C2: phương pháp khác để ghi lại tên cột trong admin
    @admin.display(description="price")
    def price_formatted(self, obj):
        return format_currency_vietnam(obj.price)

    @admin.display(description="price_real")
    def price_real_formatted(self, obj):
        return format_currency_vietnam(obj.price_real)

    @admin.display(description="price_sale")
    def price_sale_formatted(self, obj):
        # Sử dụng toán từ 3 ngôi để kiểm tra thông tin trường price_sale
        # -> Nếu có thông tin (dạng số) thì format
        # --> Nếu không có thông tin thì giữ mặc định price_sale (rỗng)
        return format_currency_vietnam(obj.price_sale) if obj.price_sale else obj.price_sale

    @admin.display(description="image")
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)


# Thêm view Category/ CategoryAdmin vào trang admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PlantingMethod)

admin.site.site_header = ADMIN_HEADER_NAME
