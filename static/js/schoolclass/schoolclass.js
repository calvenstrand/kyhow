$(function () {

    //This is a click bound for connecting a class with a course
    $('.connecter').click(function () {
        var idz = $(this).parents().parents().attr('id');
        console.log(idz);
        var classVal = $('#classSelect').val();
        var className = $('#classSelect').children('option').text();
        var courseVal = $('#courseSelect').val();
        //its called mus right now and should be changed to something better, but doesnt really matter, dependant on urls.py
        $.post('/mus/' + classVal + '/' + courseVal + '/', function (data) {
            $('#' + idz).modal('hide')
            window.location.href = '/schoolclass/' + courseVal + '/?answer=6';
        });

    });


//ajax for clicking steps and changing their status
    $('.label').click(function () {
        var idzz = $(this).attr('id');

        $.post('/changestep/' + idzz + '/',function (data) {
            if (data === 0) {
                $('#' + idzz).attr('class', 'label label-important cursor-fix');
            } else if (data === 1) {
                $('#' + idzz).attr('class', 'label label label-success cursor-fix');

            }
            //notify 2 for the status change worked out
            notifys.notify(2);



        }).error(function () {
                notifys.notify(4); //There was an error, throw error notification!
            });

    });
    //to change the showing course, just a kindof link
    $('#course-picker').click(function () {
        var courseid = $('#course-select').val();
        console.log(courseid);
        window.location.href = '/schoolclass/' + courseid + '/?answer=3';
    });

    //Show when you enter the page which course are showing at the moment.
    //notifys.notify(3); //Visa vilken kurs man läser

});

  $("#course-creater").click(function () {
        window.location.href = "/createpage/createcourse";
    });
