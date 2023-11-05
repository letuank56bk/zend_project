import re
# thư viện template của django
from django import template
# thư viện để hiển thị dữ liệu dưới dạng html
from django.utils.html import mark_safe

register = template.Library()


# Hàm dùng để hihglight từ khóa ở kết quả khi tìm kiếm
# --> IGNORECASE: tìm kiếm không phân biệt hoa thường
# --> sub: giống với hàm replace
def highlight_shop(value, keyword):
    if keyword == "":
        return value
    else:
        # re.escape: tăng tính an toàn đối với dữ liệu phía người dùng nhập vào
        # --> Tham khảo: https://manhhomienbienthuy.github.io/2016/11/23/vai-lo-hong-thuong-gap-va-cach-phong-chong-trong-django.html
        regex = re.compile(re.escape(keyword), re.IGNORECASE)

        # trả về kết quả đã highlight dưới dạng HTML thông qua hàm mark_safe
        return mark_safe(regex.sub(f'<span class="highlight">{keyword}</span>', value))


# Đăng ký hàm tự định nghĩa (highlight) vào trong Library của template django
register.filter("highlight_shop", highlight_shop)

# Lưu ý:
# --> Sau khi sử dụng nếu xảy ra lỗi, cần kiểm tra lại trong thư mục setting đã đăng ký DIR cho templates chưa
# TEMPLATES --> "DIRS": [BASE_DIR / 'templates']
