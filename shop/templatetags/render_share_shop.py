# thư viện template của django
from django import template

from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def render_share_shop(src_template, items):
    return render_to_string("shop/pages/share/" + src_template, {'items': items})
