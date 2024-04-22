$(function (){
    //ajax请求
    $('#dl').click(function (){
        // 获取账号
        var user= $('#username').val();
        //获取密码
        var pwd= $('#password').val();
        // 加密处理

        //发送请求1111
        $.ajax({
            method:"POST",
            url:'/login',
            data:{"user":user,"pwd":pwd},
            dataType:"json",
            success:function (data){
                if(data.code==='1'){
                    alert(data.msg);
                }else{
                    alert(data.msg)
                }

            }
        })


        //  2222
        // $.ajax({
        //     method:"POST",
        //     url:'/login',
        //     data:{"user":user,"pwd":pwd},
        //     dataType:"json",
        // }).done(function (data){
        //     if(data.code==='1'){
        //         alert(data.msg);
        //     }else {
        //         //$(this).next().append('<h1>'+data.msg+'</h1>')
        //         alert(data.msg)
        //     }
        //
        // }).fail(function (){
        //     alert('请求失败')
        //
        // })
        //

    })


});