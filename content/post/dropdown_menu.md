+++ 
keywords = "常见的下拉菜单"
description = "常见的下拉菜单"
categories = ["frontend"]
tags = ["下拉菜单"]
date = "2016-03-03T23:55:37+08:00"
title = "常见的下拉菜单"
url = "dropdown-menu"
+++

## HTML结构

网页中导航栏是一个很常见的组件。通常，我们使用无序列表来制作导航栏。比如

	<div id="nav">
		<ul class="navMenu">
			<li><a href="">首页</a></li>
			<li><a href="">跟团游</a></li>
			<li><a href="">自助游</a></li>
			<li><a href="">游轮</a></li>
			<li><a href="">自驾</a></li>
		</ul>
	</div>

有些导航栏有下拉的二级菜单，那么我们在相应的位置上再加上列表构成二级菜单，比如

	<div id="nav">
		<ul class="navMenu">
			<li><a href="">首页</a></li>
			<li><a href="">跟团游</a>
				<ul class="subMenu">
					<li><a href="">出境跟团</a></li>
					<li><a href="">国内跟团</a></li>
					<li><a href="">周边跟团</a></li>
					<li><a href="">当地参团</a></li>
				</ul>
			</li>
			<li><a href="">自助游</a>
				<ul class="subMenu" >
					<li><a href="">出境自助</a></li>
					<li><a href="">国内自助</a></li>
					<li><a href="">机票+酒店</a></li>
					<li><a href="">火车+酒店</a></li>
				</ul>
			</li>
			<li><a href="">游轮</a>
				<ul class="subMenu">
					<li><a href="">包船专享</a></li>
					<li><a href="">日韩航线</a></li>
					<li><a href="">欧洲航线</a></li>
					<li><a href="">三峡航线</a></li>
					<li><a href="">美洲航线</a></li>
				</ul>
			</li>
			<li><a href="">自驾</a>
				<ul class="subMenu">
					<li><a href="">周边自驾</a></li>
					<li><a href="">国内自驾</a></li>
					<li><a href="">出境自驾</a></li>
				</ul>
			</li>
		</ul>
	</div>
 
## 基本的CSS样式

列表默认是垂直方向排列的，而常见的导航栏主菜单是水平方向排列，二级下拉菜单是垂直方向排列的，所以我们需要对主菜单的li元素设置浮动，让其水平排列。设置浮动后，应记得清除浮动。可以使用class来作为公共的浮动和清除浮动的样式，然后在需要浮动的元素上添加相应的class，在浮动元素的父元素上添加清除浮动的class。

**CSS代码**

	<style type="text/css">
		/*reset*/
		body, div, ul,li, a{padding: 0; margin:0;}
		ul{list-style: none; }
		/*浮动和清除浮动*/
		.fl{float: left; }
		.clearfix:after{content:"";display:block;clear:both;}
		.clearfix{zoom:1;} 
		/*导航栏*/
		#nav{width: 600px; height: 40px; margin:0 auto; background-color: #eee; }
		.navMenu li{ text-align: center; line-height: 40px; position: relative;}
		.navMenu li a{text-decoration: none;color:#000; padding: 0 20px; display: block; width:80px; }
		.subMenu{position: absolute; top: 40px; left: 0;display: none;}/*默认隐藏二级菜单*/
		.subMenu li{float:none; background-color:#eee; margin-left: 2px; }
	</style>

**HTML代码** 改为如下所示：

	<body>
		<div id="nav">
			<ul class="navMenu clearfix">
				<li class="fl"><a href="">首页</a></li>
				<li class="fl"><a href="">跟团游</a>
					<ul class="subMenu">
						<li><a href="">出境跟团</a></li>
						<li><a href="">国内跟团</a></li>
						<li><a href="">周边跟团</a></li>
						<li><a href="">当地参团</a></li>
					</ul>
				</li>
				<li class="fl"><a href="">自助游</a>
					<ul class="subMenu" >
						<li><a href="">出境自助</a></li>
						<li><a href="">国内自助</a></li>
						<li><a href="">机票+酒店</a></li>
						<li><a href="">火车+酒店</a></li>
					</ul>
				</li>
				<li class="fl"><a href="">游轮</a>
					<ul class="subMenu">
						<li><a href="">包船专享</a></li>
						<li><a href="">日韩航线</a></li>
						<li><a href="">欧洲航线</a></li>
						<li><a href="">三峡航线</a></li>
						<li><a href="">美洲航线</a></li>
					</ul>
				</li>
				<li class="fl"><a href="">自驾</a>
					<ul class="subMenu">
						<li><a href="">周边自驾</a></li>
						<li><a href="">国内自驾</a></li>
						<li><a href="">出境自驾</a></li>
					</ul>
				</li>
			</ul>
		</div>
	<body>

## 下拉菜单效果的实现

如何实现鼠标移动到主菜单相应的li元素位置时，显示二级菜单，而移开鼠标则隐藏二级菜单。基本的实现方法纯CSS样式、jQuery、 原生JavaScript等三种实现方法。

### 方法一、 纯CSS样式：[见demo1](http://www.wangxingfeng.com/posts/demo1.html)
最简单的方式是直接使用css的 `:hover` 来实现。当鼠标移动到主菜单的对应的li上时，二级菜单设置为可见的块级元素  `display: block;`
	.navMenu li:hover .subMenu{display: block;} /*hover是显示二级菜单*/


### 方法二、 jQuery：[见demo2](http://www.wangxingfeng.com/posts/demo2.html)
使用jQuery获取li元素，绑定mouseover、mouseout事件，调用jQuery的show()、hide()方法。参考代码如下：

	<script src="js/jquery-2.2.3.min.js"></script>
	<script type="text/javascript">
		$(function() {
			$('.navMenu>li').mouseover( function() {
				$(this).children('ul').show();
			});
				$('.navMenu>li').mouseout( function() {
				$(this).children('ul').hide();
			});
		});
	</script>

### 方法三、 原生JavaScript：[见demo3](http://www.wangxingfeng.com/posts/demo3.html)
先定义显示和隐藏元素的函数

<script type="text/javascript">
	// 定义显示函数
	function showsubmenu(li) {
		var submenu = li.getElementsByClassName('subMenu')[0];
		submenu.style.display="block";
	}
	// 定义隐藏函数
	function hidesubmenu(li){
		var submenu = li.getElementsByClassName('subMenu')[0];
		submenu.style.display="none";
	}
</script>

再调用函数， 在HTML代码中对应的li元素，添加函数的调用，代码修改如下。

	<div id="nav">
		<ul class="navMenu clearfix">
			<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">首页</a></li>
			<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">跟团游</a>
				<ul class="subMenu">
					<li><a href="">出境跟团</a></li>
					<li><a href="">国内跟团</a></li>
					<li><a href="">周边跟团</a></li>
					<li><a href="">当地参团</a></li>
				</ul>
			</li>
			<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">自助游</a>
				<ul class="subMenu" >
					<li><a href="">出境自助</a></li>
					<li><a href="">国内自助</a></li>
					<li><a href="">机票+酒店</a></li>
					<li><a href="">火车+酒店</a></li>
				</ul>
			</li>
			<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">游轮</a>
				<ul class="subMenu">
					<li><a href="">包船专享</a></li>
					<li><a href="">日韩航线</a></li>
					<li><a href="">欧洲航线</a></li>
					<li><a href="">三峡航线</a></li>
					<li><a href="">美洲航线</a></li>
				</ul>
			</li>
			<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">自驾</a>
				<ul class="subMenu">
					<li><a href="">周边自驾</a></li>
					<li><a href="">国内自驾</a></li>
					<li><a href="">出境自驾</a></li>
				</ul>
			</li>
		</ul>
	</div>
