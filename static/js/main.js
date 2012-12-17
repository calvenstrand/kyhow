$(document).ready(function() {

    /* ---------- Datable ---------- */
    $('.datatable').dataTable({
        "sDom": "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span12'i><'span12 center'p>>",
        "sPaginationType": "bootstrap"
    } );

    $('.btn-minimize').click(function(e){
        e.preventDefault();
        var $target = $(this).parent().parent().next('.box-content');
        if($target.is(':visible')) $('i',$(this)).removeClass('icon-chevron-up').addClass('icon-chevron-down');
        else 					   $('i',$(this)).removeClass('icon-chevron-down').addClass('icon-chevron-up');
        $target.slideToggle();
    });

    $('.btn-setting').click(function(e){
        e.preventDefault();
        $('#myModal').modal('show');
    });

    $('.box-content').hide();

    $('#schoolclass{{ classs.id }}').dataTable( {
        "oLanguage": {
            "sLengthMenu": "Visa _MENU_ elever per sida",
            "sZeroRecords": "Inga elever hittades",
            "sInfo": "Visar _START_ till _END_ av _TOTAL_ elever",
            "sInfoEmpty": "Visar 0 till 0 av 0 elever",
            "sInfoFiltered": "(Filtrerad från _MAX_ total elever)"
        }
    } );

} );
