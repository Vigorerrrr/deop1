$(function (){

    $('.menu li').click(function(){
                $(this).addClass('cur').siblings().removeClass('cur');
                // 获取
                $('.content div').eq($(this).index()).addClass('active').siblings().removeClass('active');


            });

    //ajax请求
    $('.tja').click(function (){
        $.ajax({
            url:'/geturl',
            method:'GET',
            dataType:'json',
            success: function (response){
                var gt_url = response.url;
                $('.myframea').attr('src',gt_url);

            },

        });

    });
  1
    //ajax请求
    $('.tjb').click(function (){
        $.ajax({
            url:'/geturl',
            method:'GET',
            dataType:'json',
            success: function (response){
                var gt_url = response.url;
                $('.myframeb').attr('src',gt_url);


            },

        });

    });

});