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
$('.sort-abstract').click(function () {
    checkClass();
    $('.item:not(.abstract)').toggleClass('hide');
});
$('.sort-geometric').click(function () {
    checkClass();
    $('.item:not(.geometric)').toggleClass('hide');
});
$('.sort-nature').click(function () {
    checkClass();
    $('.item:not(.nature)').toggleClass('hide');
});

// Active tag
$('.button').click(function () {
    $('.button').removeClass('active');
    $(this).addClass('active');
})