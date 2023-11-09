APP_PATH_PAGE = "shop/pages/"

APP_VALUE_STATUS_ACTIVE = "published"

APP_VALUE_LAYOUT_DEFAULT = "list"

APP_VALUE_STATUS_DEFAULT = "draft"

# Định nghĩa lại tên hiển thị trong trang admin
TABLE_PLANTING_METHOD_SHOW = "Planting Methods"

TABLE_CATEGORY_SHOW = "Category"

TABLE_PRODUCT_SHOW = "Products"

TABLE_CONTACT_SHOW = "Contact"

TABLE_ORDER_SHOW = "Order"

TABLE_ORDER_ITEM_SHOW = "Order Item"
# Định nghĩa lại tên hiển thị trong trang admin


APP_VALUE_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

APP_VALUE_LAYOUT_CHOICES = (
    ('list', 'List'),
    ('grid', 'Grid')
)

APP_VALUE_STATUS_ORDER_CHOICES = (
    ("order", "Order"),
    ("confirm", "Confirm"),
    ("delivery", "Delivery"),
    ("finish", "Finish")
)

APP_VALUE_STATUS_ORDER_DEFAULT = "order"

ADMIN_SRC_JS = ('my_admin/js/general.js', 'my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js')

ADMIN_SRC_CSS = {
    'all': ('my_admin/css/custom.css',)
}

SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX = 8

SETTING_PRODUCT_TOTAL_ITEMS_LASTEST_INDEX = 9

SETTING_PRODUCT_TOTAL_ITEMS_LASTEST_SIDEBAR = 9

SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX = 9

SETTING_PRODUCT_TOTAL_ITEMS_RANDOM_INDEX = 9

SETTING_PRODUCT_TOTAL_ITEMS_RELATED = 6

SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR = 6

SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE = 3

SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL = 5

SETTING_PRODUCT_TOTAL_ITEMS_PER_PAGE = 6

SETTING_ARTICLE_TOTAL_ITEMS_RELATED = 6

SETTING_ARTICLE_TOTAL_ITEMS_RECENT = 6

SETTING_ARTICLE_TOTAL_ITEMS_RANDOM = 3

SETTING_FEED_TOTAL_ITEMS_SIDEBAR = 5

SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR = 5

SETTING_PLANTING_METHOD_TOTAL_ITEMS_SIDEBAR = 4

APP_VALUE_IMAGE_DEFAULT = "/media/news/images/feed/no-image.png"

SETTING_API_LINK_PRICE_COIN = "http://apiforlearning.zendvn.com/api/get-coin"

SETTING_API_LINK_PRICE_GOLD = "http://apiforlearning.zendvn.com/api/get-gold"

SETTING_PRICE_COIN_TOTAL_ITEM = 5

SETTING_PRICE_GOLD_TOTAL_ITEM = 5

NOTIFY_ORDER_SUCCESS = "Cảm ơn bạn đã đặt hàng từ chúng tôi"

NOTIFY_CONTACT_SUCCESS = "Cảm ơn bạn đã liên hệ với chúng tôi"

NOTIFY_ORDER_CHECK_NOT_EXIST = "Không tìm thấy đơn hàng, vui lòng kiểm tra lại mã đơn!"

NOTIFY_ORDER_CHECK_NOT_NULL = "Vui lòng nhập mã đơn hàng!"

ADMIN_HEADER_NAME = "Hệ Thống Quản Lý Thông Tin"
