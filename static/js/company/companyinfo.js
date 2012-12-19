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
    $('#edit').css('display', 'none');
    $('#save').css('display', 'block');
    $('#cancel').css('display', 'block');
})

$('#cancel').click(function (e) {
    setTimeout(function () {
        $('#editCompanyForm').find(':input').each(function () {
            $(this).attr('disabled', 'disabled');
        })
        $('#edit').removeAttr('disabled');
        $('#edit').css('display', 'block');
        $('#save').css('display', 'none');
        $('#cancel').css('display', 'none');
    }, 1)
});

});