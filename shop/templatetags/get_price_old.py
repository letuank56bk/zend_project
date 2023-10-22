# thư viện template của django
from django import template
from .format_currency_vietnam import format_currency_vietnam

register = template.Library()


@register.simple_tag
def get_price_old(price, price_sale):
    return format_currency_vietnam(price) if price_sale else ""
