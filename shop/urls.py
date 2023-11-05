from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),

    re_path(r"^(?P<product_slug>[\w-]+)-a(?P<product_id>\d+)\.html$", views.product, name="product"),

    path("gio-hang.html", views.cart, name="cart"),

    path("thanh-toan.html", views.checkout, name="checkout"),

    path("shop.html", views.category, name="shop"),

    path("<slug:category_slug>.html", views.category, name="category"),

    # Thư viên tinymce --> trình biên soạn HTML
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
