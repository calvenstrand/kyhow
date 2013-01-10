//Notifys is a helperfunction for showing notifications, just follow the pattern
var notifys = {
    init : function( options ) {  },
    show : function( options ) {  },
    hide : function( ) {  },
    notify : function( number ) {

        if (number === 1){//saved forms
            $("#container").notify("create", "notify-green", {
                title: 'Formulär sparades!',
                text: ''
            });
        }else if(number === 2){//successchange of step
            $("#container").notify("create", "notify-green" , {
                title: 'Inlämningsstatusen förändrades utan fel!',
                text: ''
            },
                {expires: 750,});
        }else if(number === 3){
            $("#container").notify("create" , {
                title: 'Visar nu kurs: '+ $('.content').children('b').first().text() +'!',
                text: ''
            });
        }else if(number === 0){
            $("#container").notify("create" ,"notify-red", {
                title: 'Formulär kunde inte sparas!',
                text: ''
            });
        }else if(number === 4){//Error changing step
            $("#container").notify("create" ,"notify-red", {
                title: 'Inlämningsstatusen kunde inte förändras!',
                text: ''
            });
        }else if(number === 5){
            $("#container").notify("create" ,"notify-red", {
                title: 'Du måste fylla i ett namn!',
            });
        }else if(number === 6){
            $("#container").notify("create" ,"notify-green", {
                title: 'Kopplingen lyckades!',
            });
}
    },
};


    //Put it in hiding on the base.html page for the notifications to show up later on
    $('#notifydivs').html('<div id="container" style="display:none">'
        +'<div id="basic-template">'
        +'<a class="ui-notify-cross ui-notify-close" href="#">x</a>'
        +'<h1>#{title}</h1><p>#{text}</p></div>'
        +''
        +'<div id="notify-green" class="notify-green">'
        +'<a class="ui-notify-cross ui-notify-close" href="#">x</a>'
        +'<h1>#{title}</h1></div>'
        +''
        +'<div id="course-notify" class="notify-green">'
        +'<a class="ui-notify-cross ui-notify-close" href="#">x</a>'
        +'<h1>#{title}</h1></div>'
        +''
        +'<div id="notify-red" class="notify-red">'
        +'<a class="ui-notify-cross ui-notify-close" href="#">x</a>'
        +'<h1>#{title}</h1>'
        +'</div>'
        +''
        //End of container
        +'</div>');
