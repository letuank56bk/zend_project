from django.contrib.sites import requests
from django.db.models import Count

from .models import *
from .define import *
from django.utils import timezone
import requests


# Hàm lấy tất cả các Category
# -> Cần đăng ký trong settings --> TEMPLATES --> OPTIONS --> context_processors
# --> Sau khi đăng ký trong setting, hàm sẽ tự động chạy mỗi khi người dùng truy cập website
# ---> annotate(num_article=Count("article"): Đến số lượng article thuộc danh mục
# ---> [:5] lấy 5 giá trị category đầu tiền
def items_category_sidebar_menu(request):
    items_category_sidebar_menu = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by("ordering").annotate(
        num_articles=Count("article"))[:5]

    return {
        "items_category_sidebar_menu": items_category_sidebar_menu
    }


# Tin tức tổng hợp
def items_feed_sidebar_menu(request):
    items_feed_sidebar_menu = Feed.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by("ordering")[:5]

    return {
        "items_feed_sidebar_menu": items_feed_sidebar_menu
    }


# Bài viết gần đây
def items_article_sidebar_recent(request):
    # request.get_full_path() --> lấy thông tin path người dùng đang truy cập
    # -> thay thế article bằng rỗng để có thể lấy được phần slug
    skip_slug = request.get_full_path().replace("/article/", "")

    items_article_sidebar_recent = (Article.objects
                                    .filter(status=APP_VALUE_STATUS_ACTIVE,
                                            publish_date__lte=timezone.now())
                                    .exclude(slug=skip_slug)
                                    .order_by("-publish_date")[:SETTING_ARTICLE_TOTAL_ITEMS_RELATED]
                                    )

    return {
        "items_article_sidebar_recent": items_article_sidebar_recent
    }


# Bài viết ngẫu nhiên
def items_article_footer_random(request):
    # request.get_full_path() --> lấy thông tin path người dùng đang truy cập
    # -> thay thế article bằng rỗng để có thể lấy được phần slug
    # --> order_by("?") --> random order cho các phần tử
    skip_slug = request.get_full_path().replace("/article/", "")

    items_article_footer_random = (Article.objects
                                   .filter(status=APP_VALUE_STATUS_ACTIVE,
                                           publish_date__lte=timezone.now())
                                   .exclude(slug=skip_slug)
                                   .order_by("?")[:3]
                                   )

    return {
        "items_article_footer_random": items_article_footer_random
    }


# Bài viết nóng nhất
def items_article_header_trending(request):
    # request.get_full_path() --> lấy thông tin path người dùng đang truy cập
    # -> thay thế article bằng rỗng để có thể lấy được phần slug
    # --> order_by("?") --> random order cho các phần tử
    skip_slug = request.get_full_path().replace("/article/", "")

    items_article_header_trending = (Article.objects
                                     .filter(status=APP_VALUE_STATUS_ACTIVE,
                                             publish_date__lte=timezone.now())
                                     .exclude(slug=skip_slug)
                                     .order_by("?")[:1]
                                     )

    print(items_article_header_trending)
    return {
        "items_article_header_trending": items_article_header_trending
    }


def items_price_sidebar_coin(request):
    url = "http://apiforlearning.zendvn.com/api/get-coin"

    items_price_sidebar_coin = []

    response = requests.get(url)
    if response.status_code == 200:
        items_price_sidebar_coin = response.json()[:5]

    return {
        "items_price_sidebar_coin": items_price_sidebar_coin
    }


def items_price_sidebar_gold(request):
    url = "http://apiforlearning.zendvn.com/api/get-gold"

    items_price_sidebar_gold = []

    response = requests.get(url)
    if response.status_code == 200:
        items_price_sidebar_gold = response.json()[:5]

    return {
        "items_price_sidebar_gold": items_price_sidebar_gold
    }