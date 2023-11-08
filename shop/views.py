import re
from django.shortcuts import render, get_object_or_404, redirect
# Thư viện giúp lấy đường link trực tiếp quan name từ file urls
from django.urls import reverse
# import tất cả các class model trong folder models thông qua file __init__
from .models import *
# Thư viện xử lý về thời gian
from django.utils import timezone

# Chức năng xử lý phân trang
from django.core.paginator import Paginator

# import tập tin define.py/ helper
from .define import *
from .helpers import *
from .forms import CheckoutForm, ContactForm


# Create your views here.
def index(request):
    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by("ordering")

    for item in items_category:
        item.product_filter = item.product_set.filter(status=APP_VALUE_STATUS_ACTIVE, special=True).order_by(
            "ordering")[:SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX]

    items_product_lastest = Product.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE).order_by("-id")[
                            :SETTING_PRODUCT_TOTAL_ITEMS_LASTEST_INDEX]

    # chia nhỏ items_product_lastest ra thành các nhóm có 3 sản phẩm
    items_product_lastest = chunked(items_product_lastest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    items_product_hot = Product.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE).order_by("-total_sold")[
                        :SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX]

    # 1 nhóm sẽ có 3 sản phẩm
    items_product_hot = chunked(items_product_hot, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    items_product_random = Product.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE).order_by("?")[
                           :SETTING_PRODUCT_TOTAL_ITEMS_RANDOM_INDEX]

    # 1 nhóm sẽ có 3 sản phẩm
    items_product_random = chunked(items_product_random, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    return render(request, APP_PATH_PAGE + 'index.html', {
        "title_page": "Trang chủ",
        "items_product_lastest": items_product_lastest,
        "items_product_hot": items_product_hot,
        "items_product_random": items_product_random,
        "items_category": items_category
    })


def product(request, product_slug, product_id):
    # Tìm kiếm trong DB, nếu có trả ra thông tin, nếu không phản hồi lại 404
    item_product = get_object_or_404(Product, id=product_id, slug=product_slug, status=APP_VALUE_STATUS_ACTIVE)
    # Bài viết liên quan
    # --> exclude: Loại bỏ các bài viết có tên giống với bài đang hiển thị (thông qua slug) trong mục bài viết liện quan
    # --> [:SETTING_ARTICLE_TOTAL_ITEMS_RECENT] chỉ lấy 6 phần từ đầu tiên của kết quả trả về --> tránh trường hợp show tất cả dữ liệu
    items_product_related = (Product.objects
                             .filter(category=item_product.category, status=APP_VALUE_STATUS_ACTIVE)
                             .order_by("-id")
                             .exclude(id=product_id)[:SETTING_PRODUCT_TOTAL_ITEMS_RELATED])

    return render(request, APP_PATH_PAGE + 'detail.html', {
        "title_page": item_product.name,
        "item_product": item_product,
        "items_product_related": items_product_related,
    })


def category(request, category_slug="shop"):
    item_category = None
    if category_slug != "shop":
        item_category = get_object_or_404(Category, slug=category_slug, status=APP_VALUE_STATUS_ACTIVE)

    params = {
        "order": request.GET.get("order") if request.GET.get("order") == "price" else "-price",
        "minPrice": request.GET.get("minPrice", ""),  # -> Nếu không có giá trị để mặc định là ""
        "maxPrice": request.GET.get("maxPrice", ""),  # -> Nếu không có giá trị để mặc định là ""
        "planting": request.GET.get("planting", ""),  # -> Nếu không có giá trị để mặc định là ""
        "keyword": request.GET.get("keyword", ""),  # -> Nếu không có giá trị để mặc định là ""
    }
    item_products = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by(params["order"] + "_real")

    if item_category:
        item_products = item_products.filter(category=item_category, status=APP_VALUE_STATUS_ACTIVE)
    if params["minPrice"]:
        item_products = item_products.filter(price_real__gte=params["minPrice"])
    if params["maxPrice"]:
        item_products = item_products.filter(price_real__lte=params["maxPrice"])
    if params["planting"]:
        item_products = item_products.filter(planting_methods__id=params["planting"])
    if params["keyword"]:
        item_products = item_products.filter(name__iregex=re.escape(params["keyword"]))

    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by("ordering")[
                     :SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR]

    items_planting_methods = PlantingMethod.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by("ordering")[
                             :SETTING_PLANTING_METHOD_TOTAL_ITEMS_SIDEBAR]

    # Đếm số lượng item sau khi lọc -> cần làm trước khi phân trang
    product_count = item_products.count()

    # Phân trang
    paginator = Paginator(item_products, SETTING_PRODUCT_TOTAL_ITEMS_PER_PAGE)
    page = request.GET.get("page")
    item_products = paginator.get_page(page)

    items_product_lastest = Product.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE).order_by("-id")[
                            :SETTING_PRODUCT_TOTAL_ITEMS_LASTEST_SIDEBAR]

    # chia nhỏ items_product_lastest ra thành các nhóm có 3 sản phẩm
    items_product_lastest = chunked(items_product_lastest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    return render(request, APP_PATH_PAGE + 'category.html', {
        "title_page": item_category.name if item_category else "Cửa hàng",
        "items_category": items_category,
        "item_category": item_category,
        "item_products": item_products,
        "items_planting_methods": items_planting_methods,
        "params": params,
        "paginator": paginator,
        "items_product_lastest": items_product_lastest,
        "product_count": product_count,
    })


def cart(request):
    items_product_cart = []
    total_price = 0

    if "cart" in request.session:
        cart = request.session["cart"]

        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            item_price = product.price_real * quantity

            total_price += item_price
            cart_item = {
                "id": product_id,
                "product": product,
                "quantity": quantity,
                "item_price": item_price
            }
            items_product_cart.append(cart_item)
    return render(request, APP_PATH_PAGE + "cart.html", {
        "title_page": "Giỏ hàng",
        "items_product_cart": items_product_cart,
        "total_price": total_price,
    })


def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("id")
        quantity = request.POST.get("quantity")

        # trường hợp người dùng chưa add gì vào trong cart -> để tránh lỗi cho hệ thống
        if "cart" not in request.session:
            request.session["cart"] = {}

        cart = request.session["cart"]
        # nếu sản phẩm đã được thêm vào trước đấy thì cộng thêm số lượng
        # Nếu không thì gán từ đấu
        if product_id in cart:
            cart[product_id] += int(quantity)
        else:
            cart[product_id] = int(quantity)

        request.session.modified = True

    absolute_url = request.build_absolute_uri(reverse("shop:cart"))

    return redirect(absolute_url)


def update_cart(request):
    action = request.GET.get("action")
    product_id = request.GET.get("productId")
    product_id = str(product_id)
    # lấy thông tin cart trong session, nếu không có cart -> tra ve rỗng
    cart = request.session.get("cart", {})

    if product_id in cart:
        if action == "decrease":
            if cart[product_id] > 1:
                cart[product_id] -= 1
            else:
                del cart[product_id]
        elif action == "increase":
            cart[product_id] += 1
        elif action == "delete":
            del cart[product_id]

    # gán lại giá trị cho session sau khi đã thay đổi
    request.session["cart"] = cart

    absolute_url = request.build_absolute_uri(reverse("shop:cart"))

    return redirect(absolute_url)


def checkout(request):
    cart = request.session.get("cart", {})
    form = CheckoutForm()  # validate

    if not cart:
        absolute_url = request.build_absolute_uri(reverse("shop:cart"))
        return redirect(absolute_url)

    if request.method == "POST":
        form = CheckoutForm(request.POST)  # validate
        # Xem video 4-16-4
        if form.is_valid():
            return checkout_post(request, form, cart)

    items_product_checkout = []

    total_order = 0

    if "cart" in request.session:
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            name = product.name
            total = product.price_real * quantity

            total_order += total

            items_product_checkout.append({"name": name, "total": total, "quantity": quantity})

    return render(request, APP_PATH_PAGE + "checkout.html", {
        "title_page": "Thanh toán đơn hàng",
        "items_product_checkout": items_product_checkout,
        "total_order": total_order,
        "form": form,
    })


def checkout_post(request, form, cart):
    name = form.cleaned_data["name"]
    email = form.cleaned_data["email"]
    phone = form.cleaned_data["phone"]
    address = form.cleaned_data["address"]
    code = generate_order_code(8)

    # Lưu tạm thông tin đơn hàng
    order = Order.objects.create(
        code=code,
        name=name,
        email=email,
        phone=phone,
        address=address
    )

    total_order = 0
    quantity_order = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        price = product.price_real
        total = price * quantity

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price,
            total=total
        )

        total_order += total
        quantity_order += quantity

    order.quantity = quantity_order
    order.total = total_order
    order.save()

    del request.session["cart"]

    absolute_url = request.build_absolute_uri(reverse("shop:success")) + "?t=order"
    return redirect(absolute_url)


def success(request):
    notify = NOTIFY_ORDER_SUCCESS

    if request.GET.get('t') == "contact":
        notify = NOTIFY_CONTACT_SUCCESS

    return render(request, APP_PATH_PAGE + "success.html", {
        "title_page": "Thông báo",
        "notify": notify
    })


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return contact_post(request, form)

    return render(request, APP_PATH_PAGE + "contact.html", {
        "title_page": "Liên hệ",
        "form": form,
    })


def contact_post(request, form):
    name = form.cleaned_data["name"]
    email = form.cleaned_data["email"]
    phone = form.cleaned_data["phone"]
    message = form.cleaned_data["message"]
    contacted = False

    # Lưu tạm thông tin liên hệ
    Contact.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message,
        contacted=contacted
    )

    absolute_url = request.build_absolute_uri(reverse("shop:success")) + "?t=contact"
    return redirect(absolute_url)
