$(function (){
    //ajax请求
    $('#tj').click(function (){
        $.ajax({
            url:'/geturl',
            method:'GET',
            dataType:'json',
            success: function (response){
                var gt_url = response.url;
                $('#myframe').attr('src',gt_url);
            },

        });

    });

});