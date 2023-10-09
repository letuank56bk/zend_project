from django.db.models import Count

from .models import *
from .define import *


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


def items_feed_sidebar_menu(request):
    items_feed_sidebar_menu = Feed.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by("ordering")[:5]

    return {
        "items_feed_sidebar_menu": items_feed_sidebar_menu
    }
