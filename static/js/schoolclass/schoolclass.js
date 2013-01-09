$(function () {
    // do stuff after DOM has loaded



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

$('#course-picker').click(function(){
    var courseid = $('#course-select').val();
    console.log(courseid);

    window.location.href='/schoolclass/'+courseid+'/';


});

    notifys.notify(3); //Visa vilken kurs man läser

});