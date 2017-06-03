+++
keywords = ["返回顶部"]
description = "实现返回顶部效果的3种方式"
categories = ["frontend"]
tags = ["返回顶部"]
date = "2016-04-22T22:56:30+08:00"
title = "实现返回顶部效果的3种方式"
url = "back-to-top"
+++


现在的网页内容比较多，基本上无法在一屏完全显示出来。这个时候，用户需要移动滚动条（滑动鼠标滚轮）来查看全部内容，如果想要返回顶部同样需要移动滚动条。如果页面太长，这样的体验显然不够好。因此，`返回顶部`的按钮就应运而生了。

返回顶部的实现方式主要有以下3种。

## 实现方式一：设置锚链接 

最简单快捷的方式是设置锚链接`<a href="#">` 。`京东`就是使用这种方式。

优点：简单快速，没有浏览器兼容问题。

参考代码如下：

HTML代码

		<div id="go-top">
			<a href="#"  id="gotop-btn"></a><!-- 直接使用锚链接来返回顶部 -->
		</div>


## 实现方式二：借助jQuery来实现

参考代码如下：

HTML代码

	<div id="go-top">
		<a href="javascript:;"  id="gotop-btn"></a>
	</div>

JavaScript代码

	<script type="text/javascript">
		$(function() {
			$(window).scroll(function(){
				// 当滚动条距顶部超过100像素时，返回顶部按钮出现，否则消失
		if ($(window).scrollTop()>=100){
			$("#gotop-btn").fadeIn(500);
		}
		else{
			$("#gotop-btn").fadeOut(500);
		}
		});
		//当点击跳转链接后，回到页面顶部位置
		$("#gotop-btn").click(function(){
			$('body,html').animate({scrollTop:0},300);
		});
	});
	</script>


## 实现方式三：通过原生JavaScript来动态操作。

需要用到以下知识

### DOM 操作：

1.根据ID获取元素：`document.getElementById`

2.滚动条的数值，可读写：`document.documentElment.scrollTop`

### 事件运用：

1.页面加载完毕后触发`window.onload`

2.点击后触发`onclick`

3.滚动条滚动时触发 `window.onscroll`


### 定时器：

1.`setInterval()` : 设置定时器，需要传两个参数。

2.`clearInterval()`: 关闭定时器，需要传两个参数。

参考代码：

	HTML代码
	<div id="go-top">
		<a href="javascript:;"  id="gotop-btn"></a>
	</div>

	js代码
	<script  type="text/javascript" >
		// 加载后触发事件
		window.onload = function() {
			var obtn = document.getElementById('gotop-btn');
			// 获取页面可视区域高度
			var clientHeight = document.documentElement.clientHeight;
			var timer = null;
			var isTop = true;
			// 滚动条滚动时触发事件，清除定时器，停在当前位置。
			window.onscroll = function() {
				// 获取滚动条距离顶部的数值
				var osTop = document.documentElement.scrollTop || document.body.scrollTop; 

				if(osTop >= clientHeight){
					// 显示返回按钮
					obtn.style.display = "block";
				}
				else{
					// 隐藏返回按钮
					obtn.style.display = "none";
				}
				if(!isTop){
					clearInterval(timer);
				}
				isTop = false;
			}
			obtn.onclick = function() {
				// 设置定时器
				timer = setInterval(function() {
					var osTop = document.documentElement.scrollTop || document.body.scrollTop; 
					// chrome使用document.body.scrollTop 来获取滚动条到顶部的距离。
					// 滚动条滚动由快到慢，即减少的距离从大到小。
					var ispeed = Math.floor(-osTop /6);
					// Math.floor()向下取整, 如果ispeed去正数，会导致osTop最后无法等于0，从而无法消除定时器。
					document.documentElement.scrollTop = document.body.scrollTop = osTop + ispeed;
					//滚动条到了顶部之后，清除定时器，否则会一直返回顶部没法下拉滚动条看底下的网页内容。
					isTop = true;
					// console.log(osTop-ispeed);
					if(osTop == 0){
						clearInterval(timer);
					}
				},50)
			}
		}
	</script>
