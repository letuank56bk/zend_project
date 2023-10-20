# thư viện template của django
from django import template

# Thư viện locale giúp format dữ liệu dạng số
import locale

register = template.Library()


# format lại định dạng giá tiền theo VND (ngắn cách các phần bằng dấu chấm)
def format_currency_vietnam(number):
    locale.setlocale(locale.LC_ALL, 'vi_VN')

    formatted_number = locale.format_string('%d', number, grouping=True) + 'đ'

    return formatted_number


# TEMPLATES --> "DIRS": [BASE_DIR / 'templates']

# Đăng ký hàm tự định nghĩa (format_currency_vietnam) vào trong Library của template django
register.filter("format_currency_vietnam", format_currency_vietnam)
