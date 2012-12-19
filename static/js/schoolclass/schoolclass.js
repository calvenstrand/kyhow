$('.connecter').click(function(){
    var idz = $(this).parents().parents().attr('id');
    console.log(idz);
    var classVal = $('#classSelect').val();
    var courseVal = $('#courseSelect').val();
    $.post('/mus/'+classVal+'/'+courseVal+'/', function(data) {
        $('#'+idz).modal('hide')
        location.reload();


    });

});

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

$('#course-picker').click(function(){
    var courseid = $('#course-select').val();
    console.log(courseid);

    window.location.href='/schoolclass/'+courseid+'/';


});