+++
title = "用CSS实现图片翻转的动画效果"
tags = ["CSS"]
images = []
banner = ""
menu = ""
keywords = ["CSS3", "transform","图片翻转","页面翻转效果", "rotateY"]
description = "CSS如何实现图片翻转效果，CSS如何实现页面翻转效果,CSS3, transform,"
categories = ["frontend"]
date = "2017-04-29T21:24:00+08:00"
url ="css-flip.html"
+++

## 用CSS实现页面或图片翻转的动画效果
Web开发中常常会有动画的交互效果，以前我们只能用JavaScript来实现，随着浏览器对CSS3新特性的支持度越来越好，很多的特效都可以通过CSS代码来实现。

我们在浏览网站的时候，经常能够看到图片会翻转的动画效果，比如`Demo 1`所示。


<div class="rotate-container" style="border:2px solid #000;">
	<div class="flipper">
		<div class="front">
			<!-- 前面内容 -->
			<p >正面内容</p>
			<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
		</div>
		<div class="back">
			<p>反面内容</p>
			<img src="https://images-cn.ssl-images-amazon.com/images/G/28/kindle/merch/2014/campaign/Gen7-Launch/Associate/Associate_AssociateCenrter_300_250_Family._V325383366_.jpg" alt="">
		</div>
	</div>
</div>


能否用纯CSS来实现这种翻转动画效果呢？答案是肯定的。

我们知道CSS3的`transform`属性非常强大，可以实现2D或者3D的旋转、缩放、移动或倾斜。

上述Demo1是沿着Y轴3D翻转的，我们可以想到用`transform`属性的`rotateY()`方法来实现。

## 示例代码

HTML代码

	<div class="rotate-container"">
		<div class="flipper">
			<div class="front">
				<!-- 前面内容 -->
			</div>
			<div class="back">
				<!-- 背面内容 -->
			</div>
		</div>
	</div>

CSS代码

	.rotate-container:hover .flipper{
		transform: rotateY(180deg);
	}

	.rotate-container, .front, .back {
		width: 320px;
		height: 480px;
	}

	.flipper {
		transition-duration: 1s;  
		transform-style: preserve-3d;
		position: relative;
	}

	.front, .back {
		backface-visibility: hidden;
		position: absolute;
		top: 0;
		left: 0;
	}

	.front {
		z-index: 2;
	}

	.back {
		transform: rotateY(180deg);
	}


## 关键的技术点解释：

### 1.transform：变形

`transform: rotateY(180deg)` 表示沿着Y轴旋转180度。
<style>
	.rotateY{
		transition-duration:1.5s;
	}
	.rotateY45:hover{
		transform: rotateY(45deg);
	}
	.rotateY90:hover{
		transform: rotateY(90deg);
	}
	.rotateY180:hover{
		transform: rotateY(180deg);
		
	}
	.bf-hidden{
		transform-style: preserve-3d;
		backface-visibility: hidden;
	}
</style>
<p>Demo2：沿着Y轴旋转180度(旋转到背面可见)</p>
<div class="rotateY rotateY180">
	<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
</div>
<p>Demo3：沿着Y轴旋转90度</p>
<div class="rotateY rotateY90">
	<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
</div>
<p>Demo4：沿着Y轴旋转45度</p>
<div class="rotateY rotateY45">
	<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
</div>


### 2.transform-style：指定该元素的子元素所在空间。

指定该元素的子元素是（看起来）位于三维空间内，还是在该元素所在的平面内被扁平化。

`transform-style`属性有两个参数，`flat`和`preserve-3d`。`flat`为默认值，指定子元素位于此元素所在平面内; `preserve-3d`指定子元素定位在三维空间内。

### 3.backface-visibility 指定元素旋转到背面时是否可见。

默认为visible，即背面是可见的, 如`Demo2`所示。

在Demo1中，由于翻转过来的是另外一张图片，所以设置为backface-visibility:hidden背面是不可见的。

<p>Demo5: 沿着Y轴旋转180度(旋转到背面不可见)</p>
<div class="rotate-container">
	<div class="flipper" >
		<div class="front">
			<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
		</div>
	</div>
</div>

### 4.transition-duration：表示完成过渡效果需要花费的时间。

`transition-duration：1s `可以用简写的形式`transition:1s`。

### 5.position:absolute：绝对定位。

使用绝对定位`position:absolute`把翻转前后的两个元素摆放到同一个位置。

