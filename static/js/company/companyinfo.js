$(function () {

    $('#editCompanyForm').find(':input').each(function () {
        $(this).attr('disabled', 'disabled');
    });

    $('#edit').removeAttr('disabled');
    $('#create').removeAttr('disabled');

    $('#create').click(function () {
        window.location.href = "/createpage/createcompany";
    });

    function formFixer (a) {
        if (a == 0) {
            $('#editCompanyForm').find(':input').each(function() {
                $(this).removeAttr('disabled');
            });
            $('#emailLink').css(
                'display', 'none'
            );
            $('#websiteLink').css(
                'display', 'none'
            );
            $('#edit').css(
                'display', 'none'
            );
            $('#emailEdit').css(
                'display', 'block'
            );
            $('#websiteEdit').css(
                'display', 'block'
            );
            $('#save').css(
                'display', 'block'
            );
            $('#cancel').css(
                'display', 'block'
            );
        } else if (a == 1) {
            $('#editCompanyForm').find(':input').each(function () {
                $(this).attr('disabled', 'disabled');
            });
            $('#emailEdit').css(
                'display', 'none'
            );
            $('#websiteEdit').css(
                'display', 'none'
            );
            $('#save').css(
                'display', 'none'
            );
            $('#cancel').css(
                'display', 'none'
            );
            $('#emailLink').css(
                'display', 'block'
            );
            $('#websiteLink').css(
                'display', 'block'
            );
            $('#edit').removeAttr(
                'disabled'
            );
            $('#edit').css(
                'display', 'block'
            );
        }
    }

    $('#edit').click(function (e) {
        e.preventDefault();
        a = 0;
        formFixer(a);
    });

    $('#cancel').click(function (e) {
        a = 1;
        setTimeout(function () {
            formFixer(a);
        }, 1)
    });

    $('#save').click(function (e) {
        if ($('#id_name').val() < 1) {
            notifys.notify(5);
            e.preventDefault();
        } else {
            // Carry on
        }
    });

});