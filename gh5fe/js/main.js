_.templateSettings = {
  interpolate: /\{\{(.+?)\}\}/g
};

$('.citation-yes').on('click', function () {
    var mainContent = _.template($('#yes-form').html());
    $('.main-content').html(mainContent);
});
