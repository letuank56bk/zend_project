from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def check_and_show_value(value):
    return value if value else ""
