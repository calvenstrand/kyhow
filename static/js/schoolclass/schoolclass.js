$('#connect').click(function(){
    var idz = $(this).parents().parents().attr('id');
    console.log(idz);
    var classVal = $('#classSelect').val();
    var courseVal = $('#courseSelect').val();
    $.post('/mus/'+classVal+'/'+courseVal+'/', function(data) {
        $('#'+idz).modal('hide')


    });

});