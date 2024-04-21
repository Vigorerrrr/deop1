"""
@Author:
@Filename:jqury_1.py
@SoftWare: PyCharm

"""
# https://code.jquery.com/  地址
"""
1、jquery介绍和引用
jQuery是目前使用最广泛的javascript函数库,
jQuery的版本分为1.x系列和2.x系列,1.x系列兼容低版本的浏览器,2.x.3.x系列放弃支持低版本浏览器,
目前使用最多的是1.x系列的。
jquery的口号和愿望Write Less,DoMore(写得少,做得多)
官方网站:http://jquery.com/
在线手册:https://www.runoob.com/manual/jquery/
下载
版本下载:<https://code.jquery.com/>
引入页面
jquery是一个函数库,一个js文件,页面用script标签引入这个js文件就可以使用
<script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>

<script
  src="https://code.jquery.com/jquery-1.12.4.min.js"
  integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="
  crossorigin="anonymous"></script>

简介地址
https://www.runoob.com/manual/jquery/



"""

"""

2、jquery选择器
jquery用法思想一
选择某个网页元素,然后对它进行某种操作
jquery基本的选择器
jquery选择器可以快速地选择元素,选择规则和css样式相同,使用lenggth属性判断是否选择成功。
//id选择器
$('#btn1')

//类选择器
$('.box1')

//标签选择器
$('Ti')

//层级选择器
$('#ul li span')

//属性选择器
S('input[name=user]')

选择同胞和父辈元素
//选择div元素前面紧挨的同辈元素
$('div').prev();

//选择div元素之前所有的同辈元素
$('div').prevAll();

//选择div元素后面紧挨的同辈元素
S('div').next();

//选择div元素后面所有的同辈元素
S('div').nextAll();

//选择div的父元素
S('div').parent();

//选择div的所有子元素
$('div').children();

//选择div的同级元素
$('div').siblings();

//选择div内的class等于cs的元素
$('div').find('.cs');



选择过滤
//选择包含p元素的div元素
$('div').has(p');

//选择c1ass不等于cs的div元素
S('div').not(.cs');

//选择c1ass等于cs的div元素
S('div').filter('.cs');

//选择第6个div元素
S('div').eq(5);



获取元素的索引值
有时候需要获得匹配元素相对于其同胞元素的索引位置,此时可可以用index()方法获取
var Sli = S(.list li').eq(1);
alert(Sli.index());//弹出1
<u1 class="list">
<11>1</11>
<1i>2</1i>
<1i>4</1i>
<1i>5</11>
<1i>6</1i>
</u1>




"""
"""
3、jquery操作样式
获取元素样式
//获取div的样式
S("div").css("width");
$("div").css(color");

修改元素样式
//设置div的样式
$("div").css(width","30px");
$("div").css("height", "30px");
S("div").css({fontsize: "30px",color: "red"});

添加或者移除class属性

//添加c1ass属性
$("#div1").addClass("cs2")
//移除c1ass属性
S("#div1").removeClass("cs2")
//重复切换样式
S("#div1").toggleClass("cs2")



4、绑定click事件

给元素绑定click事件,可以用如下方法:
$('#btnl').click(function(){
内部的this指的是原生对象
//使用jquery对象用S(this)

34节


"""














