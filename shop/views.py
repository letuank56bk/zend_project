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
    return render(request, APP_PATH_PAGE + 'index.html')