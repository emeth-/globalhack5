var $body = $('body');

$body.on('click', '.resources', function () {
    var mainContent = _.template($('#resources').html());
    $('.main-content').html(mainContent());
});
$body.on('click', '.citation-yes', function () {
    var mainContent = _.template($('#yes-form').html());
    $('.main-content').html(mainContent({yesOrNo: true}));
});

$body.on('click', '.citation-no', function () {
    var mainContent = _.template($('#yes-form').html());
    $('.main-content').html(mainContent({yesOrNo: false}));
});
$body.on('click', '.submit-form', function () {

    $('.server-error').remove();

    var citationNumber = $('.citation-number').val(),
        driversLicense = $('.drivers-license').val(),
        lastName = $('.last-name').val(),
        dateOfBirth = $('.date-of-birth').val();

    $.ajax({
        type: 'GET',
        url: 'http://globalhack5.herokuapp.com/get_info_special',
        data: {
            citation: citationNumber,
            last_name: lastName,
            date_of_birth: dateOfBirth,
            drivers_license_number: driversLicense
        },
        success: function (response, status, xhr) {
            if (response.status === 'error') {
                var mainContent = _.template($('#no-citations').html());
                $('.main-content').prepend(mainContent({message: response.message}));
            } else if (response.status === 'success') {
                var data = response.citation;

                var content = _.template($('#list-citations').html());
                $('.main-content').html(content({citations: [data]}));
            }
        },
        error: function () {
            debugger;
        }

    })
});

var threeViolations = function () {
    $('.citation-number').val('282415157');
    $('.drivers-license').val('L814561589');
    $('.last-name').val('Jones');
    $('.date-of-birth').val('10/17/1962');
};
var oneViolation = function () {
    $('.citation-number').val('789674515');
    $('.drivers-license').val('O890037612');
    $('.last-name').val('Phillips');
    $('.date-of-birth').val('12/30/1975');
};
var sixViolationsMixedWarrants = function () {
    $('.citation-number').val('755184943');
    $('.drivers-license').val('P974104339');
    $('.last-name').val('Castillo');
    $('.date-of-birth').val('7/4/1973');
}