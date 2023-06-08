// Check active classes
var checkClass = function () {
    if ($('.item').hasClass('hide')) {
        $('.item').removeClass('hide');
    }
};

// Category filters
$('.sort-all').click(function () {
    checkClass();
});
$('.sort-residential').click(function () {
    checkClass();
    $('.item:not(.residential)').toggleClass('hide');
});
$('.sort-commercial').click(function () {
    checkClass();
    $('.item:not(.commercial)').toggleClass('hide');
});
$('.sort-mosque').click(function () {
    checkClass();
    $('.item:not(.mosque)').toggleClass('hide');
});

// Active tag
$('.button').click(function () {
    $('.button').removeClass('active');
    $(this).addClass('active');
})