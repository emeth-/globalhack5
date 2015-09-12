$('.citation-yes').on('click', function () {
    var mainContent = _.template($('#yes-form').html());
    $('.main-content').html(mainContent({yesOrNo: true}));
});
$('.citation-no').on('click', function () {
    var mainContent = _.template($('#yes-form').html());
    $('.main-content').html(mainContent({yesOrNo: false}));
});
