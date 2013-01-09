$(function () {

$('#editCompanyForm').find(':input').each(function () {
    $(this).attr('disabled', 'disabled');

})

$('#edit').removeAttr('disabled');

$('#edit').click(function (e) {
    e.preventDefault();
    $('#editCompanyForm').find(':input').each(function() {
        $(this).removeAttr('disabled');
    })
    $('#emailLink').css('display', 'none');
    $('#emailEdit').css('display', 'block');
    $('#websiteLink').css('display', 'none');
    $('#websiteEdit').css('display', 'block');
    $('#edit').css('display', 'none');
    $('#save').css('display', 'block');
    $('#cancel').css('display', 'block');
})

$('#cancel').click(function (e) {
    setTimeout(function () {
        $('#editCompanyForm').find(':input').each(function () {
            $(this).attr('disabled', 'disabled');
        })
        $('#emailEdit').css('display', 'none');
        $('#emailLink').css('display', 'block');
        $('#websiteEdit').css('display', 'none');
        $('#websiteLink').css('display', 'block');
        $('#edit').removeAttr('disabled');
        $('#edit').css('display', 'block');
        $('#save').css('display', 'none');
        $('#cancel').css('display', 'none');
    }, 1)
});

$('#save').click(function (e) {
    if ($('#id_name').val() < 1) {
        if ($('#cheat').length == 0) {
            $('#id_name').before('<ul class="errorlist" id="cheat"><li>This field is required.</li></ul>');
            notifys.notify(0);
        }
        e.preventDefault();
    } else {
        // Carry on
    }
});

});