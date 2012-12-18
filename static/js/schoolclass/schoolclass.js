$('#connect').click(function(){

    var classVal = $('#classSelect').val();
    var courseVal = $('#courseSelect').val();
    $.post('/mus/'+classVal+'/'+courseVal+'/', function() {

    });

});