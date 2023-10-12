from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),

    # --> origin: path("article/<slug:article_slug>", views.article, name="article"),
    # Dùng biểu thức chính quy để định dạng lại đường dẫn thân thiện hơn với google và SEO
    # --> cần thêm giá trị article_id bên model và views vì có thêm article_id
    re_path(r"^(?P<article_slug>[\w-]+)-a(?P<article_id>\d+)\.html$", views.article, name="article"),

    # --> origin: path("feed/<slug:feed_slug>", views.feed, name="feed"),
    re_path(r"^tin-tuc-tong-hop-(?P<feed_slug>[\w-]+)\.html$", views.feed, name="feed"),

    path("search.html", views.search, name="search"),

    path("about.html", views.about, name="about"),

    path("contact.html", views.contact, name="contact"),

    # Thư viên tinymce --> trình biên soạn HTML
    path('tinymce/', include('tinymce.urls')),

    # --> origin path("category/<slug:category_slug>", views.category, name="category"),
    path("<slug:category_slug>", views.category, name="category"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
