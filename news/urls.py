from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),

    path("category/<slug:category_slug>", views.category, name="category"),

    path("article/<slug:article_slug>", views.article, name="article"),

    path("feed/<slug:feed_slug>", views.feed, name="feed"),

    path("search", views.search, name="search"),

    path("about", views.about, name="about"),

    path("contact", views.contact, name="contact"),

    # Thư viên tinymce --> trình biên soạn HTML
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
