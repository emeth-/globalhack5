var bindDatePicker = function () {
    $('.date-of-birth').datepicker({
        startView: 2,
        orientation: 'top auto',
        autoclose: true
    });
};

bindDatePicker();
var $body = $('body');

$body.on('click', '.resources', function () {
    var mainContent = _.template($('#resources').html());
    $('.main-content').html(mainContent());
});
$body.on('click', '.look-up', function () {
    var mainContent = _.template($('#form').html());
    $('.main-content').html(mainContent({}));
    bindDatePicker();
});
$body.on('click', '.alternatepayments', function () {
    var mainContent = _.template($('#alternatepayments').html());
    $('.main-content').html(mainContent());
});
$body.on('click', '.nav-links', function () {
    $('#navbar').removeClass('in');
    $(this).closest('li').addClass('active').siblings().removeClass('active');
});
$body.on('click', '.alt-pay', function () {
    $(this).closest('.modal-body').html(_.template($('#alternatepayments').html()));
    $(this).closest('.modal-body').find('.alt-pay').remove();
});
$body.on('click', '.submit-form', function () {

    var parseDates = function (data) {
        _.each(data.citations, function (citation, index) {
            citation.citation_date = moment(citation.citation_date).format('MM/DD/YYYY');
            citation.court_date = moment(citation.court_date).format('MM/DD/YYYY');
            citation.date_of_birth = moment(citation.date_of_birth).format('MM/DD/YYYY');
        });
    };

    $('.server-error').remove();

    var importantNumber = $('.important-number').val(),
        driversLicense = $('.drivers-license').val(),
        lastName = $('.last-name').val(),
        dateOfBirth = $('.date-of-birth').val();

    $.ajax({
        type: 'GET',
        url: 'http://globalhack5.herokuapp.com/get_info_special',
        data: {
            important_number: importantNumber,
            last_name: lastName,
            date_of_birth: dateOfBirth,
            drivers_license_number: driversLicense
        },
        success: function (response, status, xhr) {

            if (response.status === 'error') {
                var mainContent = _.template($('#no-citations').html());
                $('.main-content').prepend(mainContent({message: response.message}));
            } else if (response.status === 'success') {
                parseDates(response);
                var content = _.template($('#list-citations').html());
                $('.main-content').html(content(response));
            }
        },
        error: function () {
            var mainContent = _.template($('#no-citations').html());
            $('.main-content').prepend(mainContent({message: 'A really bad error occurred.'}));
        }
    });
});

var threeViolationsWDL = function () {
    $('.important-number').val('L814561589');
    $('.last-name').val('Jones');
    $('.date-of-birth').val('10/17/1962');
};
var threeViolationsWCN = function () {
    $('.important-number').val('282415157');
    $('.last-name').val('Jones');
    $('.date-of-birth').val('10/17/1962');
};
var oneViolation = function () {
    $('.citation-number').val('789674515');
    $('.drivers-license').val('O890037612');
    $('.last-name').val('Phillips');
    $('.date-of-birth').val('12/30/1975');
};
var threeViolationsMixedWarrants = function () {
    $('.citation-number').val('755184943');
    $('.drivers-license').val('P974104339');
    $('.last-name').val('Castillo');
    $('.date-of-birth').val('7/4/1973');
};

$body.on('click', '#gold-fish', function () {
    $(this).remove();
   if($('#financial-status').val() === '1' && $('#income-bracket').val() === '1') {
        $('#results').html('Based on profiles similar to yours, you may qualify for alternative payment options such as community service or payment plans. Please make an appointment and speak with your judge to determine if you qualify.');
   } else {
        $('#results').html('Based on profiles similar to yours, you may NOT qualify for alternative payment options such as community service or payment plans. Please make an appointment and speak with your judge to determine your eligibility.');
   }
});