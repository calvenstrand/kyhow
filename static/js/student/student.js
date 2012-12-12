$(function () {
    $('#edit').click(function(e) {
        e.preventDefault();
        $('#editStudentForm').find(':input').each(function() {
            var input = $(this);
            input.removeAttr('disabled');
        })
        $('#edit').css('display', 'none');
        $('#save').css('display', 'block');
        $('#cancel').css('display', 'block');
    })
    $('#cancel').click(function(e) {
        e.preventDefault();
        $('#editStudentForm').find(':input').each(function() {
            var input = $(this);
            input.attr('disabled', 'disabled');
        })
        $('#edit').removeAttr('disabled');
        $('#edit').css('display', 'block');
        $('#save').css('display', 'none');
        $('#cancel').css('display', 'none');
    })
})