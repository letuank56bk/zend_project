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

    return render(request, APP_PATH_PAGE + 'index.html', {
        "title_page": "Trang chủ",
        "items_product_lastest": items_product_lastest,
        "items_category": items_category
    })
