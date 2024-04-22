"""
# -*- coding: utf-8 -*-
@Filename:class2.py
@SoftWare: PyCharm
# @user: Nemo

"""

"""
CSS
1、css介绍和引用

1.1、CSS概述
    CSS:层叠样式表(英文全称:Cascading Style Sheets)是一种用来表现HTML或XML(标准通用标记语言的一
个子集)等文件样式的计算机语言。CSS不仅可以静态地修饰网页,还可可以配合各种脚本语言动态地对网页各元素
进行格式化,CSS能够对网页中元素位置的排版进行像素级精确控制,支持几乎所有的字体字号样式,拥有对网页
对象和模型样式编辑的能力


1.2、css的基本语法
CSS规则由两个主要的部分构成:选择器,以及一条或多条声明
选择器通常是您需要改变样式的HTML元素,
每条声明由一个属性和一个值组成。
属性(property)是您希望设置的样式属性(styleattribute)。每个属性有一个值,属性和值被冒号分开。


1.3、css引入方法:

1、外联式:通过link标签,链接到外部样式表到页面中。
<link rel="stylesheet" type="text/css" href="css/main.css">

2、嵌入式:通过style标签,在网页上创建嵌入的样式表。
<style type="text/css">
div{width:100px;height:100px; color:red }
</style>

3、内联式:通过标签的style属性,在标签上直接写样式。
<div style="width:100px; height:100px; color:red ">....</div>

首页采用嵌入式引入css能加快速度



2、css背景


2.1、设置背景色
background-cplor设置背景色。这个属性接受任何合法的颜色值,
这条规则把元素的背景设置为红色:
p{background-color: red:}

2.2、设置背景图像
background-image:要把图像放入背景,属性的默认值是none,表示背景上没有放置任何图像,如果需要
一个背景图像,必须为这个属性设置一个URL值:
body {background-image: url(/i/eg_bg_04.gif);}
大多数背景都应用到body元素,不过并不仅限于此。
背景图平铺
如果需要在页面上对背景图像进行平铺,可以使用background-repeat属性
属性值:
repeat导致图像在水平垂直方向上都平铺,就像以往背景图像的通常做法一样
repeat-x:图像只在水平上重复,
repeat-y:图像在垂直方向上重复
no-repeat:不允许图像在任何方



3、颜色表示法
颜色三种表示方法:
颜色名表示,比如:red,cyangold
rgb表示,比如:rgb(255,0,0)表示红色
·16进制数值表示,比如:#FFFF00表示黄色
颜色对照表地址:http://tool.oschina.net/commons?type=3




4、css文本样式
常用的应用文本的css样式:
    color设置文字的颜色,
        color:red:
    font-size设置文字的大小
        font-size:12px;
    font-family设置文字的字体
        font-family:'微软雅黑';
    font-style设置字体是否倾斜:
        不倾斜:font-style:'normal';
        倾斜:font-style:italic';
    font-weight设置文字是否加粗,
        font-weight:bold 设置加粗
        font-weight:normal设置不加粗
    line-height设置文字的行高(行高相当于在每行文字的上下同时加间距)
        line-height:30px;
    设置文字的几个属性,顺序如下:font:是否加粗字号/行高 字体
        font:normal 12px/36px'微软雅里;
    text-indent设置文字首行缩进
        text-indent:24px 设置首行缩进24px



5、css选择器

5.1、标签选择器
最常见的CSS选择器是元素选择器。换句话说,文档的元素就是最基本的选择器
如果设置HTML的样式,选择器通常将是某个HTML元素,比如p、h1、em.a,甚至可以是html本身:
<h1>h1标题</h1>
<h2>h2标题</h2>
h1{color:blue;}
h2 {color:silver:}


5.2、id选择器

首先,ID选择器前面有一个#号
通过id名来选择元素,元素的id名称不能重复,所以一个样式设置项只能对应于页面上一个元素,一个ID只能在文
档中使用一次,id名一般给程序使用,所以不推荐在css设置样式时使用id作为选择器
<inputtype="test" name="uname" id="user">

#user {font-weight:bold;}


5.3、类选择器

必须将class指定为一个适当的值,类名前有一个点号(.),通过lass类名来选择元素,一个类可应用了多个元
素,一个元素上也可以使用多个类,应用灵活,可复用,是css中应用最多的一种选择器。
<div class="menu"></div>

.menu {color:red;}


5.4、属性选择器

通过元素的属性进行选择,
选择带name属性的a标签
<a href=""Iname="nmb"></a>
<a href=""></a>
<a href=""></a>

a[name]{color:red:}


5.5、包含选择器/层级选择器

主要应用在选择父元素下的子元素,或者子元素下面的子元素,可与标签元素结合使用,减少命名,同时也可以通
过层级,防止命名冲突。
<div class="menu">
    <div>
        <p>p标签</p>
    </div>
</div>
.menu div p{color:cyan}


5.6、组选择器
多个选择器,每个选择器之间用逗号隔开如果有同样的样式设置,可以使用组选择器。
h1,h2,h3{color:blue;}


5.7、伪类及伪元素选择器

伪类
在支持CSS的浏览器中,链接的不同状态都可以不同的方式显示,这些状态包括:活动状态,已被访问状态,未
被访问状态,和鼠标悬停状态。

属性              描述
active              向被激活的元素添加样式。
focus               向拥有键盘输入焦点的元素添加样式。
:hover              当鼠标悬浮在元素上方时,向元素添加样式。
link                向未被访问的链接添加样式。
visited             向已被访问的链接添加样式。


伪元素
属性                  描述
first-letter        向文本的第一个字母添加特殊样式。
first-line          向文本的首行添加特殊样式。
:before             在元素之前添加内容。
:after              在元素之后添加内容。





6、CSS模型框

















"""
