from .models import *
from .define import *
from .helpers import *


def items_category_menu(request):
    items_category_menu = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by("ordering")[
                          :SETTING_CATEGORY_TOTAL_ITEMS_MENU]
    return {"items_category_menu": items_category_menu}


def item_cart_info(request):
    cart = request.session.get("cart", {})
    total_cart = 0
    quantity_cart = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total = product.price_real * quantity

        total_cart += total
        quantity_cart += quantity

    item_cart_info = {
        "total_cart": total_cart,
        "quantity_cart": quantity_cart
    }

    return {"item_cart_info": item_cart_info}
