$(function () {

    $("#tagsearch").autocomplete({
        source:"/company/tagsearch/",
        minLength:0,
        focus:function (event, ui) {
            $("#tagsearch").val(ui.item.label);
            return false;
        },
        select:function (event, ui) {
            $("#tagsearch").val(ui.item.label);
            return false;
        }
    })
        .data("autocomplete")._renderItem = function (ul, item) {
        return $("<li>")
            .data("item.autocomplete", item)
            .append("<a>" + item.label + "</a>")
            .appendTo(ul);
    };
    $("#search").click(function () {
        if ($("#tagsearch").val() != '') {

            window.location.href = "/company/companysearch/" + $("#tagsearch").val();
        }
    });


});