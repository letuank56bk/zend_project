import re
from django.shortcuts import render, get_object_or_404
# import tất cả các class model trong folder models thông qua file __init__
from .models import *
# Thư viện xử lý về thời gian
from django.utils import timezone
# Chức năng xử lý phân trang
from django.core.paginator import Paginator
# Thư viện dùng để xử lý RSS
import feedparser

# Thư viện BeautifulSoup --> Dùng để phân tích cú pháp HTML/ XML, giúp cho việc trích xuất thông tin dễ dàng hơn
from bs4 import BeautifulSoup
# import tập tin define.py
from .define import *


# Create your views here.
def index(request):
    # items_article_special = (Article.objects
    #                          .filter(special=True, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte=timezone.now())
    #                          .order_by("-publish_date"))[:SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL]

    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by("ordering")

    for item in items_category:
        item.product_filter = item.product_set.filter(status=APP_VALUE_STATUS_ACTIVE, special=True).order_by("ordering")[:SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX]

    return render(request, APP_PATH_PAGE + 'index.html', {
        "title_page": "Trang chủ",
        # "items_article_special": items_article_special,
        "items_category": items_category
    })
