$(function () {

    $('#editStudentForm').find(':input').each(function () {
        $(this).attr('disabled', 'disabled');
    })

    $('#edit').removeAttr('disabled');

    function formFixer (a) {
        if (a == 0) {
            $('#editStudentForm').find(':input').each(function() {
                $(this).removeAttr('disabled');
            });
            $('#emailLink').css(
                'display', 'none'
            );
            $('#edit').css(
                'display', 'none'
            );
            $('#emailEdit').css(
                'display', 'block'
            );
            $('#save').css(
                'display', 'block'
            );
            $('#cancel').css(
                'display', 'block'
            );
        } else if (a == 1) {
            $('#editStudentForm').find(':input').each(function () {
                $(this).attr('disabled', 'disabled');
            });
            $('#emailEdit').css(
                'display', 'none'
            );
            $('#emailLink').css(
                'display', 'block'
            );
            $('#edit').removeAttr(
                'disabled'
            );
            $('#edit').css(
                'display', 'block'
            );
            $('#save').css(
                'display', 'none'
            );
            $('#cancel').css(
                'display', 'none'
            );
        }
    }

    $('#edit').click(function (e) {
        e.preventDefault();
        a = 0;
        formFixer(a);
    });

    $('#cancel').click(function () {
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

    //dj mouse ajax for clicking steps
    $('.label').click(function () {
        var idzz = $(this).attr('id');

        $.post('/changestep/'+idzz+'/', function(data) {
            if (data === 0) {
                $('#'+idzz).attr('class' ,'label label-important cursor-fix');
            } else if (data === 1) {
                $('#'+idzz).attr('class' ,'label label label-success cursor-fix');
            }
            notifys.notify(2);
        }).error(function () {
            notifys.notify(4); //There was an error, throw error notification!
        });
    });
    
    //funktion f�r val av f�retag
    $('.select_company').change(function () {
        var participate = $(this).siblings('.participate_hid').val();
        var company = $(this).val();
        
        $.post('/changecompany/'+participate+'/'+company+'/', function(data) {
            location.reload();
        });
    });
    
    //funktion f�r val av kontaktperson
    $('.select_contact_person').change(function () {
        var participate = $(this).siblings('.participate_hid').val();
        var contact_person = $(this).val();
        
        $.post('/changecontactperson/'+participate+'/'+contact_person+'/', function(data) {
            location.reload();
        });
    });

});