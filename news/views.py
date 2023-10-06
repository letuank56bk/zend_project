from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Import các model
from .models import Category, Article

# Thư viện xử lý về thời gian
from django.utils import timezone

# Chức năng xử lý phân trang
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    items_article_special = (Article.objects
                             .filter(special=True, status="published", publish_date__lte=timezone.now())
                             .order_by("-publish_date"))[:5]

    items_category = Category.objects.filter(status="published", is_homepage=True).order_by("ordering")

    for item in items_category:
        item.article_filter = item.article_set.filter(status="published", publish_date__lte=timezone.now()).order_by(
            "-publish_date")

    return render(request, 'pages/index.html', {
        "items_article_special": items_article_special,
        "items_category": items_category
    })


def category(request, category_slug):
    # category_slug --> thông tin category --> article thuộc category --> đổ dữ liệu ra phía client

    # Tìm kiếm trong DB, nếu có trả ra thông tin, nếu không phản hồi lại 404
    item_category = get_object_or_404(Category, slug=category_slug, status="published")

    # Tìm kiếm trong article
    # --> Các bài viết thuộc item_category, status = published và publish date nhỏ hơn hoặc bằng ngày hiện tại
    # --> Sắp xếp theo publisd_date --> publish_date mới nhất sẽ lên đầu
    items_article = Article.objects.filter(category=item_category, status="published",
                                           publish_date__lte=timezone.now()).order_by("-publish_date")

    # Phân trang
    # --> Phân items_article thành các trang (2 items / 1 trang)
    # --> nhận số page từ phía client
    # --> lấy thông tin items_article dựa vào số page gửi lên từ clientv
    paginator = Paginator(items_article, 2)
    page = request.GET.get("page")
    items_article = paginator.get_page(page)

    return render(request, 'pages/category.html', {
        "item_category": item_category,
        "items_article": items_article,
        "paginator": paginator
    })


def article(request, article_slug):
    # Tìm kiếm trong DB, nếu có trả ra thông tin, nếu không phản hồi lại 404
    item_article = get_object_or_404(Article, slug=article_slug, status="published", publish_date__lte=timezone.now())
    # Bài viết liên quan
    # --> exclude: Loại bỏ các bài viết có tên giống với bài đang hiển thị (thông qua slug) trong mục bài viết liện quan
    # --> [:6] chỉ lấy 6 phần từ đầu tiên của kết quả trả về --> tránh trường hợp show tất cả dữ liệu
    item_article_related = (Article.objects
                            .filter(category=item_article.category, status="published",
                                    publish_date__lte=timezone.now())
                            .order_by("-publish_date")
                            .exclude(slug=article_slug)[:6]
                            )

    return render(request, 'pages/article.html', {
        "item_article": item_article,
        "item_article_related": item_article_related,
    })


def feed(request):
    return render(request, 'pages/feed.html', {})


def search(request):
    return render(request, 'pages/search.html', {})
