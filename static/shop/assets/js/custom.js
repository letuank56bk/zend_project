const currentUrl = window.location.href;
const currentParams = new URLSearchParams(window.location.search);

// Chỉ lấy path name, bỏ qua domain và query
const currentPath = new URL(currentUrl).pathname;

const currentCategory = getSlug();
const currentPlanting = currentParams.get('planting');
const currentOrder = currentParams.get('order') || "-price";

$(`ul.main-nav > li > a[href="${currentPath}"]`).parent().addClass("active")

$(`ul.main-nav > li[data-active="${currentCategory}"]`).addClass("active")

$(`ul.list-category > li[data-active="${currentCategory}"]`).addClass("active")

$(`.list-planting-method > a > span[data-active="${currentPlanting}"]`).addClass("active")

$(`select#sort-product > option[data-active="${currentOrder}"]`).attr("selected", true)

$('#sort-product').change(function () {
    let selectedValue = $(this).val();
    window.location.href = selectedValue;
});

function getSlug() {
    let slug = currentPath.substring(1, currentPath.lastIndexOf('.html'));

    return slug;
}