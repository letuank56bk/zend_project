const currentUrl        = window.location.href;
const currentParams     = new URLSearchParams(window.location.search);

const currentCategory   = getSlug();
const currentPlanting   = currentParams.get('planting');
const currentOrder      = currentParams.get('order') || "-price";

$(`ul.list-category > li[data-active="${currentCategory}"]`).addClass("active")

$(`.list-planting-method > a > span[data-active="${currentPlanting}"]`).addClass("active")

$(`select#sort-product > option[data-active="${currentOrder}"]`).attr("selected", true)

$('#sort-product').change(function() {
    let selectedValue = $(this).val();
    window.location.href = selectedValue;
});

function getSlug() {
    let pathname    = new URL(currentUrl).pathname;
    let slug        = pathname.substring(1, pathname.lastIndexOf('.html'));

    return slug;
}