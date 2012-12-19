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

    
    //funktion för val av företag
    $('#select_company').change(function(){

        var participate = $('#participate_hid').val();
        var company = $('#select_company').val();
        
        $.post('/changecompany/'+participate+'/'+company+'/', function(data) {
        
        location.reload();    
            
        });

    });
    
    
    //funktion för val av kontaktperson
    $('#select_contact_person').change(function(){

        var participate = $('#participate_hid').val();
        var contact_person = $('#select_contact_person').val();
        
        $.post('/changecontactperson/'+participate+'/'+contact_person+'/', function(data) {
        
        location.reload();    
            
        });

    });
    
    

})