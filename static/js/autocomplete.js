
$(document).ready(function(){
    $("#search-box").keyup(function(){
        $.ajax({
            type:"GET",
            url:"/autocomplete/",
            data:"search="+$(this).val(),
            success: function(response){
                $('#suggestion-box')
                    .find('option')
                    .remove()

                $("#suggestion-box").append($('<option>',{
                    value: "",
                    text: ""
                }))
                $.each(response.values,function(index,item){
                    $("#suggestion-box").append($('<option>',{
                        value:item,
                        text:item,
                    }))
                })
            }
        })
    })

    
    $("#suggestion-box").on('change',function(){
        var selectedValue=$(this).val();
        if(selectedValue){
            window.location= "?search="+selectedValue; //redirect
        }
        return false;
    })
})


