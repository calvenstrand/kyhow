$(function () {
    $('#editStudentForm').find(':input').each(function () {
        $(this).attr('disabled', 'disabled');
    })

    $('#edit').removeAttr('disabled');

    $('#edit').click(function (e) {
        e.preventDefault();
        $('#editStudentForm').find(':input').each(function() {
            $(this).removeAttr('disabled');
        })
        $('#emailLink').css('display', 'none');
        $('#emailEdit').css('display', 'block');
        $('#edit').css('display', 'none');
        $('#save').css('display', 'block');
        $('#cancel').css('display', 'block');
    })

    $('#cancel').click(function () {
        setTimeout(function () {
            $('#editStudentForm').find(':input').each(function () {
                $(this).attr('disabled', 'disabled');
            })
            $('#emailEdit').css('display', 'none');
            $('#emailLink').css('display', 'block');
            $('#edit').removeAttr('disabled');
            $('#edit').css('display', 'block');
            $('#save').css('display', 'none');
            $('#cancel').css('display', 'none');
        }, 1)
    })

    //dj mouse ajax for clicking steps
    $('.label').click(function(){
        var idzz = $(this).attr('id');
        console.log(idzz);

        $.post('/changestep/'+idzz+'/', function(data) {
            if(data === 0){
                $('#'+idzz).attr('class' ,'label label-important cursor-fix');
            }else if(data === 1){
                $('#'+idzz).attr('class' ,'label label label-success cursor-fix');
            }
            notifys.notify(2);
            console.log(data);



        }).error(function(){
                notifys.notify(4); //There was an error, throw error notification!
            });


    });
    
    //funktion f�r val av f�retag
    $('.select_company').change(function(){
        var participate = $(this).siblings('.participate_hid').val();
        var company = $(this).val();
        
        $.post('/changecompany/'+participate+'/'+company+'/', function(data) {
            location.reload();
        });
    });
    
    //funktion f�r val av kontaktperson
    $('.select_contact_person').change(function(){
        var participate = $(this).siblings('.participate_hid').val();
        var contact_person = $(this).val();
        
        $.post('/changecontactperson/'+participate+'/'+contact_person+'/', function(data) {
            location.reload();
        });
    });
})