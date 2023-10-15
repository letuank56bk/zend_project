from django.contrib import admin

# Register your models here.
# import tất cả các class model trong folder models thông qua file __init__
from .models import Category, Article, Feed

# Import các hằng số (tên mặc định của hệ thống)
# --> Các hằng số này được khai báo giúp code được tường mình và gọn gàng hơn
from .define import *


# Custom trang category trong admin
class CategoryAdmin(admin.ModelAdmin):
    # list_display --> danh sách các cột sẽ hiển thị trong view admin
    list_display = ('name', 'status', 'is_homepage', 'layout', 'ordering')
    # list_filter --> tạo bộ lọc với các trường được liệt kê
    list_filter = ['status', 'is_homepage', 'layout']
    # search_fields --> tạo thêm ô tìm kiếm theo cột name
    search_fields = ["name"]

    # Tự động sinh ra slug từ tên của category (sẽ có lỗi xảy ra nếu tên category là tiếng việt có dấu)
    # --> prepopulated_fields = {'slug': ('name',)}
    # custome tạo slug tự động, loại bỏ lỗi đối với tiếng việt
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS


class ArticleAdmin(admin.ModelAdmin):
    # list_display --> danh sách các cột sẽ hiển thị trong view admin
    list_display = ('name', 'category', 'status', 'ordering', 'special', 'publish_date')
    # list_filter --> tạo bộ lọc với các trường được liệt kê
    list_filter = ['status', 'category', 'special']
    # search_fields --> tạo thêm ô tìm kiếm theo cột name
    search_fields = ['name']

    # Tự động sinh ra slug từ tên của category (sẽ có lỗi xảy ra nếu tên category là tiếng việt có dấu)
    # prepopulated_fields = {'slug': ('name',)}
    # custome tạo slug tự động, loại bỏ lỗi đối với tiếng việt
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS


class FeedAdmin(admin.ModelAdmin):
    # list_display --> danh sách các cột sẽ hiển thị trong view admin
    list_display = ('name', 'slug', 'status', 'ordering', 'link')
    # list_filter --> tạo bộ lọc với các trường được liệt kê
    list_filter = ['status']
    # search_fields --> tạo thêm ô tìm kiếm theo cột name
    search_fields = ['name']

    # Tự động sinh ra slug từ tên của category (sẽ có lỗi xảy ra nếu tên category là tiếng việt có dấu)
    # prepopulated_fields = {'slug': ('name',)}
    # custome tạo slug tự động, loại bỏ lỗi đối với tiếng việt
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS


# Thêm view Category/ CategoryAdmin vào trang admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)

admin.site.site_header = ADMIN_HEADER_NAME
