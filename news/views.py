import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Import các model
from .models import Category, Article, Feed
# Thư viện xử lý về thời gian
from django.utils import timezone
# Chức năng xử lý phân trang
from django.core.paginator import Paginator
# Thư viện dùng để xử lý RSS
import feedparser
# Thư viện json
import json
# Thư viện BeautifulSoup --> Dùng để phân tích cú pháp HTML/ XML, giúp cho việc trích xuất thông tin dễ dàng hơn
from bs4 import BeautifulSoup
# import tập tin define.py
from .define import *


# Create your views here.
def index(request):
    items_article_special = (Article.objects
                             .filter(special=True, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte=timezone.now())
                             .order_by("-publish_date"))[:SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL]

    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by("ordering")

    for item in items_category:
        item.article_filter = item.article_set.filter(status=APP_VALUE_STATUS_ACTIVE, publish_date__lte=timezone.now()).order_by(
            "-publish_date")

    return render(request, APP_PATH_PAGE + 'index.html', {
        "title_page": "Trang chủ",
        "items_article_special": items_article_special,
        "items_category": items_category
    })


def category(request, category_slug):
    # category_slug --> thông tin category --> article thuộc category --> đổ dữ liệu ra phía client

    # Tìm kiếm trong DB, nếu có trả ra thông tin, nếu không phản hồi lại 404
    item_category = get_object_or_404(Category, slug=category_slug, status=APP_VALUE_STATUS_ACTIVE)

    # Tìm kiếm trong article
    # --> Các bài viết thuộc item_category, status = published và publish date nhỏ hơn hoặc bằng ngày hiện tại
    # --> Sắp xếp theo publisd_date --> publish_date mới nhất sẽ lên đầu
    items_article = Article.objects.filter(category=item_category, status=APP_VALUE_STATUS_ACTIVE,
                                           publish_date__lte=timezone.now()).order_by("-publish_date")

    # Phân trang
    # --> Phân items_article thành các trang (2 items / 1 trang)
    # --> nhận số page từ phía client
    # --> lấy thông tin items_article dựa vào số page gửi lên từ clientv
    paginator = Paginator(items_article, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE)
    page = request.GET.get("page")
    items_article = paginator.get_page(page)

    return render(request, APP_PATH_PAGE + 'category.html', {
        "title_page": item_category.name,
        "item_category": item_category,
        "items_article": items_article,
        "paginator": paginator
    })


def article(request, article_slug, article_id):
    # Tìm kiếm trong DB, nếu có trả ra thông tin, nếu không phản hồi lại 404
    item_article = get_object_or_404(Article, id=article_id, slug=article_slug, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte=timezone.now())
    # Bài viết liên quan
    # --> exclude: Loại bỏ các bài viết có tên giống với bài đang hiển thị (thông qua slug) trong mục bài viết liện quan
    # --> [:SETTING_ARTICLE_TOTAL_ITEMS_RECENT] chỉ lấy 6 phần từ đầu tiên của kết quả trả về --> tránh trường hợp show tất cả dữ liệu
    item_article_related = (Article.objects
                            .filter(category=item_article.category, status=APP_VALUE_STATUS_ACTIVE,
                                    publish_date__lte=timezone.now())
                            .order_by("-publish_date")
                            .exclude(slug=article_slug)[:SETTING_ARTICLE_TOTAL_ITEMS_RELATED]
                            )

    return render(request, APP_PATH_PAGE + 'article.html', {
        "title_page": item_article.name,
        "item_article": item_article,
        "item_article_related": item_article_related,
    })


def feed(request, feed_slug):
    # Để sự dụng được tính năng của RSS, cần import thư viện feedparser
    # --> pip install feedparser
    # Tìm kiếm trong DB, nếu có trả ra thông tin, nếu không phản hồi lại 404
    item_feed = get_object_or_404(Feed, slug=feed_slug, status=APP_VALUE_STATUS_ACTIVE)
    feed = feedparser.parse(item_feed.link)

    # Khởi tạo mảng rỗng items_feed
    items_feed = []

    for entry in feed.entries:
        # Sử dụng thư viện BeautifulSoup để phân tích cụm dữ liệu summary dưới dạng HTML
        # -> tìm kiểm thẻ img trong soup sau đó gán vào biến img_tag
        # --> khởi tạo biến src_img --> nếu img_tag khác rỗng, gán biến src_img là phân src của img_tag
        soup = BeautifulSoup(entry.summary, 'html.parser')
        img_tag = soup.find('img')

        # Đặt hình ảnh mặc định cho bài viết, phòng trường hợp RSS của bài viết không có hình ảnh
        src_img = APP_VALUE_IMAGE_DEFAULT
        # Nếu bài viết có hình ảnh, sử dụng hình ảnh của bài viết
        if img_tag:
            src_img = img_tag["src"]

        item = {
            "title": entry.title,
            "link": entry.link,
            "pub_date": entry.published,
            "img": src_img,
        }
        # Thêm item vào trong mảng items_feed
        items_feed.append(item)

    # Kiểm tra dạng dữ liệu JSON sau khi parse, chỉ dùng khi muốn xem các trường để dev, khi chạy không cần thiết
    # Ghi dữ liệu RSS sau khi parse vào 1 file json
    # encoding='utf-8' --> encode dưới dạng utf-8 (tiếng việt) tránh trường hợp lỗi tiếng việt khi ghi vào file json
    # ensure_ascii=False --> Không mã hóa khi ghi vào file
    #####################################################
    with open('feed.json', 'w', encoding='utf-8') as f:
        json.dump(feed, f, ensure_ascii=False)
    #####################################################

    return render(request, APP_PATH_PAGE + 'feed.html', {
        "title_page": "Tin tức tổng hợp " + item_feed.name,
        "item_feed": item_feed,
        "items_feed": items_feed,
    })


def search(request):
    keyword = request.GET.get("keyword")

    # name__iregex: tìm kiếm keyword trong cột name, không phân biệt hoa thường
    # re.escape: tăng tính an toàn đối với dữ liệu phía người dùng nhập vào
    # --> Tham khảo: https://manhhomienbienthuy.github.io/2016/11/23/vai-lo-hong-thuong-gap-va-cach-phong-chong-trong-django.html
    items_article = Article.objects.filter(name__iregex=re.escape(keyword), status=APP_VALUE_STATUS_ACTIVE,
                                           publish_date__lte=timezone.now()).order_by("-publish_date")

    # Phân trang
    # --> Phân items_article thành các trang (2 items / 1 trang)
    # --> nhận số page từ phía client
    # --> lấy thông tin items_article dựa vào số page gửi lên từ clientv
    paginator = Paginator(items_article, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE)
    page = request.GET.get("page")
    items_article = paginator.get_page(page)

    return render(request, APP_PATH_PAGE + 'search.html', {
        "title_page": "Tìm kiếm cho từ khóa" + keyword,
        "items_article": items_article,
        "keyword": keyword,
        "paginator": paginator
    })


def about(request):
    return render(request, APP_PATH_PAGE + 'about.html', {
        "title_page": "Giới thiệu"
    })


def contact(request):
    return render(request, APP_PATH_PAGE + 'contact.html', {
        "title_page": "Liên hệ"
    })
