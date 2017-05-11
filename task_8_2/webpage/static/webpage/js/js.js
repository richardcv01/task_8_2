    $(document).ready(function (){
        singleValues = '';
        alert(singleValues)
        $("#sel").change(function() {
            //alert( "Handler for .change() called." );

            singleValues = $("#sel option:selected").text();
            // AJAX-запит на потрібну адресу
            alert(singleValues);
            $.get("/web/",{sel:singleValues}).done(function(data){
                alert(data);
               $('#tb').html(data);
            });
        });
    });