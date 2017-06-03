+++
tags = ["CSS"]
date = "2017-04-30T16:44:06+08:00"
title = "用CSS创建内容不倾斜的平行四边形"
keywords = "CSS, transform, skew, 平行四边形, 伪元素"
description = "用CSS绘制内容不倾斜的平行四边形的两种实现方式：嵌套元素方案和伪元素方案"
categories = ["frontend"]
url = "parallelograms.html"
+++

## 1.平行四边形

普通的网页元素是矩形的。但有时候，我们需要创建可以传达出一种动感的形状，比如平行四边形。

说到`倾斜`，我们会想到使用`transform`属性的`skew()`方法来对普通的矩形元素进行`斜向拉伸`。

	width:100px;
	height:60px;
	transform: skew(-30deg);

<div style="width:100px;height:60px;margin:10px auto;color:#fff;background: #673ab7;font-size: 16px;line-height: 60px;text-align: center;transform: skew(-30deg);">平行四边形</div>

如上所示，我们得到了一个平行四边形，但是内容也跟着斜向变形了。我们希望只是容器倾斜，而内容是不倾斜的。怎么办？

## 2.嵌套元素方案

首先，我们可以先在容器内部新增一个元素，包裹里面的内容，对这个元素再次进行斜向变形，值为负的外面容器的斜向变形值，这样刚好可以抵消掉斜向变形。

HTML代码

	<div class="parallelograms-container">
		<div class="parallelograms-inner">
			平行四边形
		</div>
	</div>

CSS代码 

	.parallelograms-container{
		width:100px;
		height:60px;
		transform: skew(-30deg);
	}
	
	.parallelograms-inner{
		transform:skew(30deg);
	}
<div class="parallelograms-container">
	<div class="parallelograms-inner">
		平行四边形
	</div>
</div>

## 3.伪元素方案

如果我们不想添加额外的HTML结构，能否用纯CSS来实现呢？

答案是肯定的。

我们可以考虑用CSS生成`伪元素`，然后把所有样式（背景、边框等）应用到伪元素上，用`绝对定位`将伪元素重叠在内容之下，然后再对伪元素进行`斜向拉伸`变形。这样内容就可以保持不倾斜。

HTML 代码
	
	<div class="pseudo-container">
		平行四边形
	</div>


CSS 代码

	.pseudo-container{
		position:relative;
		/* 内容的文字大小、颜色、内边距等样式在这里*/
		width:100px;
		height:60px;
		margin:0 auto;
		color:#fff;
		font-size: 16px;
		line-height: 60px;
		text-align: center;
		background:transparent;
	}
	
	.pseudo-container::before{
		content:"";
		position:absolute;
		top:0;right:0;bottom:0;left:0;
		z-index:-1;
		background: #673ab7;
		transform: skew(-30deg);
	}


效果如下：
<div class="pseudo-container">
	平行四边形
</div>

**注意：**

注意这里有个小坑。由于我们对这个伪元素设置了`z-index:-1`, 所以，必须确保这个伪元素的容器、以及容器的`祖先元素`(一直追溯到`<body>`的`直接子元素`)的背景都必须是透明的，否则将会遮盖住这个`伪元素`。