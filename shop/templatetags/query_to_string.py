# thư viện template của django
from django import template
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag
def query_to_string(params, query_add=None, value_add=None):
    # Xem kỹ lại video 4-8-2, chu ý tham chiếu và tham trị
    params_obj = params.copy()
    if query_add and value_add:
        params_obj[query_add] = value_add

    # Loại bỏ các thành phần rỗng trong params
    params_obj = {k: v for k, v in params_obj.items() if v}
    return urlencode(params_obj)
