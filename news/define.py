APP_VALUE_LAYOUT_DEFAULT = "list"
APP_VALUE_STATUS_DEFAULT = "draft"

TABLE_CATEGORY_SHOW = "Category"
TABLE_ARTICLE_SHOW = "Article"
TABLE_FEED_SHOW = "Feed"

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
