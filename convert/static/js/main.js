
$(document).ready(function(){

    $("#covert-form").on("submit", function(event){
        event.preventDefault();
        var data = $("#convert").val();
        $.ajax({
            type: "POST",
            data: {
                value: data,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            dataType: "json"
        }).done(function(resp){
            $("#convert-result").val(resp);
        })
    });
});
