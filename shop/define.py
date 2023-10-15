APP_PATH_PAGE = "pages/"

APP_VALUE_STATUS_ACTIVE = "published"

APP_VALUE_LAYOUT_DEFAULT = "list"

APP_VALUE_STATUS_DEFAULT = "draft"

# Định nghĩa lại tên hiển thị trong trang admin
TABLE_PLANTING_METHOD_SHOW = "Planting Methods"

TABLE_CATEGORY_SHOW = "Category"

TABLE_PRODUCT_SHOW = "Products"

# Định nghĩa lại tên hiển thị trong trang admin


APP_VALUE_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

APP_VALUE_LAYOUT_CHOICES = (
    ('list', 'List'),
    ('grid', 'Grid')
)

ADMIN_SRC_JS = ('my_admin/js/general.js', 'my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js')

ADMIN_SRC_CSS = {
    'all': ('my_admin/css/custom.css',)
}

SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL = 5

SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE = 8

SETTING_ARTICLE_TOTAL_ITEMS_RELATED = 6

SETTING_ARTICLE_TOTAL_ITEMS_RECENT = 6

SETTING_ARTICLE_TOTAL_ITEMS_RANDOM = 3

SETTING_FEED_TOTAL_ITEMS_SIDEBAR = 5

SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR = 5

APP_VALUE_IMAGE_DEFAULT = "/media/news/images/feed/no-image.png"

SETTING_API_LINK_PRICE_COIN = "http://apiforlearning.zendvn.com/api/get-coin"

SETTING_API_LINK_PRICE_GOLD = "http://apiforlearning.zendvn.com/api/get-gold"

SETTING_PRICE_COIN_TOTAL_ITEM = 5

SETTING_PRICE_GOLD_TOTAL_ITEM = 5

ADMIN_HEADER_NAME = "Hệ Thống Quản Lý Thông Tin"
