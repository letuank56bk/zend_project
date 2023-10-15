$('#sort-product').change(function() {
    let selectedValue = $(this).val();
    window.location.href = selectedValue;
});