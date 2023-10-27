import os
import uuid
import re

# Thư viện locale giúp format dữ liệu dạng số
import locale


# Hàm random tên hình ảnh
# --> Sử dụng trong models (trường image)
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('shop/images/product', filename)


def get_skip_slug_article(path):
    # Lấy phần cuối của chuỗi path --> đảm bảo slug luôn đúng kể cả trong trường hợp có thay đổi phần đầu của đường dẫn
    last_path = path.split("/")[-1]

    skip_slug = None

    match = re.search(r"^(?P<article_slug>[\w-]+)-a\d+\.html", last_path)

    if match:
        skip_slug = match.group("article_slug")

    return skip_slug


# format lại định dạng giá tiền theo VND (ngắn cách các phần bằng dấu chấm)
def format_currency_vietnam(number):
    locale.setlocale(locale.LC_ALL, 'vi_VN')

    formatted_number = locale.format_string('%d', number, grouping=True) + 'đ'

    return formatted_number


def chunked(items, quantity_per_group):
    result = []
    for i in range(0, len(items), quantity_per_group):
        chunk = items[i:i + quantity_per_group]
        result.append(chunk)
    return result


