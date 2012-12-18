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
        $('#edit').css('display', 'none');
        $('#save').css('display', 'block');
        $('#cancel').css('display', 'block');
    })

    $('#cancel').click(function (e) {
        $('#editStudentForm').find(':input').each(function () {
            $(this).attr('disabled', 'disabled');
        })
        $('#edit').removeAttr('disabled');
        $('#edit').css('display', 'block');
        $('#save').css('display', 'none');
        $('#cancel').css('display', 'none');
    })


    //dj mouse ajax for clicking steps
    $('.label').click(function(){
        var idzz = $(this).attr('id');
        console.log(idzz);

        $.post('/changestep/'+idzz+'/', function(data) {
            if(data === 0){
                $('#'+idzz).attr('class' ,'label label-important');
            }else if(data === 1){
                $('#'+idzz).attr('class' ,'label label label-success');

            }

            console.log(data);


        });

    });



})