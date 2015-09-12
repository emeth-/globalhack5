var $body = $('body');

$body.on('click', '.citation-yes', function () {
    var mainContent = _.template($('#yes-form').html());
    $('.main-content').html(mainContent({yesOrNo: true}));
});
$body.on('click', '.citation-no', function () {
    var mainContent = _.template($('#yes-form').html());
    $('.main-content').html(mainContent({yesOrNo: false}));
});
$body.on('click', '.submit-form', function () {
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
                //
            } else if (response.status === 'success') {

            }
        },
        error: function () {
            debugger;
        }

    })
});