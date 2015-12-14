var cname = $.cookie('cname');
$(function popup($) {
    //alert("hello!!!");
    $('#dialog-confirm').dialog({
        autoOpen: false,
        resizable: false,
        height: 300,
        modal: true,
        closeOnEscape: false,
        open: function(event, ui) { $(".ui-dialog-titlebar-close", ui.dialog | ui).hide(); },
        buttons: {
            "I agree": function () {
                $.cookie('cname', "on", { expires: 1000 });
                $("#splash").fadeOut("slow");
                $(".container").css("display", "table");
                //$("#footer1").css("display", "table");
                $(this).dialog("close");
            },
            Cancel: function () {
                $(this).dialog("close");
            }
        }
    });
    $(document).ready(function () {
        //$.cookie('cname', "off", { expires: 1000 });
        $('#splash').css("display", "table");
        $('.container').css("display", "none");
        //$('#footer1').css("display", "none");

        $('#splash').click(function () {
            var x;
            if (cname == "on") {
                $('#splash').fadeOut("slow");
                //$('.wholePage').css("display", "table");
                $('.container').css("display", "table");
                //$('#footer1').css("display", "table");
            }
            else {
                $('#dialog-confirm').dialog("open");
                popup();
            }
        });
    });
});

