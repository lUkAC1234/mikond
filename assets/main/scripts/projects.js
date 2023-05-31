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
$('.sort-america').click(function () {
    checkClass();
    $('.item:not(.america)').toggleClass('hide');
});
$('.sort-asia').click(function () {
    checkClass();
    $('.item:not(.asia)').toggleClass('hide');
});
$('.sort-europe').click(function () {
    checkClass();
    $('.item:not(.europe)').toggleClass('hide');
});
$('.sort-middleeast').click(function () {
    checkClass();
    $('.item:not(.middleeast)').toggleClass('hide');
});

// Active tag
$('.button').click(function () {
    $('.button').removeClass('active');
    $(this).addClass('active');
})