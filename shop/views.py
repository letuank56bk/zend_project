import re
from django.shortcuts import render, get_object_or_404
# import tất cả các class model trong folder models thông qua file __init__
from .models import *
# Thư viện xử lý về thời gian
from django.utils import timezone

# Chức năng xử lý phân trang
from django.core.paginator import Paginator

# import tập tin define.py/ helper
from .define import *
from .helpers import *


# Create your views here.
def index(request):
    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by("ordering")

    for item in items_category:
        item.product_filter = item.product_set.filter(status=APP_VALUE_STATUS_ACTIVE, special=True).order_by(
            "ordering")[:SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX]

    items_product_lastest = Product.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE).order_by("-id")[
                            :SETTING_PRODUCT_TOTAL_ITEMS_LASTEST_INDEX]

    # 1 nhóm sẽ có 3 sản phẩm
    items_product_lastest = chunked(items_product_lastest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    items_product_hot = Product.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE).order_by("-total_sold")[
                        :SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX]

    # 1 nhóm sẽ có 3 sản phẩm
    items_product_hot = chunked(items_product_hot, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    items_product_random = Product.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE).order_by("?")[
                           :SETTING_PRODUCT_TOTAL_ITEMS_RANDOM_INDEX]

    # 1 nhóm sẽ có 3 sản phẩm
    items_product_random = chunked(items_product_random, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    return render(request, APP_PATH_PAGE + 'index.html', {
        "title_page": "Trang chủ",
        "items_product_lastest": items_product_lastest,
        "items_product_hot": items_product_hot,
        "items_product_random": items_product_random,
        "items_category": items_category
    })


def product(request, product_slug, product_id):
    # Tìm kiếm trong DB, nếu có trả ra thông tin, nếu không phản hồi lại 404
    item_product = get_object_or_404(Product, id=product_id, slug=product_slug, status=APP_VALUE_STATUS_ACTIVE)
    # Bài viết liên quan
    # --> exclude: Loại bỏ các bài viết có tên giống với bài đang hiển thị (thông qua slug) trong mục bài viết liện quan
    # --> [:SETTING_ARTICLE_TOTAL_ITEMS_RECENT] chỉ lấy 6 phần từ đầu tiên của kết quả trả về --> tránh trường hợp show tất cả dữ liệu
    item_product_related = (Product.objects
                            .filter(category=item_product.category, status=APP_VALUE_STATUS_ACTIVE)
                            .order_by("-id")
                            .exclude(id=product_id)[:SETTING_PRODUCT_TOTAL_ITEMS_RELATED])

    return render(request, APP_PATH_PAGE + 'detail.html', {
        "title_page": item_product.name,
        "item_product": item_product,
        "item_product_related": item_product_related,
    })


def category(request, category_slug):
    item_category = None
    if category_slug != "shop":
        item_category = get_object_or_404(Category, slug=category_slug, status=APP_VALUE_STATUS_ACTIVE)

    item_products = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by("-id")

    if item_category:
        item_products = Product.objects.filter(category=item_category, status=APP_VALUE_STATUS_ACTIVE).order_by("-id")

    return render(request, APP_PATH_PAGE + 'category.html', {
        "item_category": item_category,
        "item_products": item_products,
    })
