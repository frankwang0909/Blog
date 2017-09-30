+++
categories = ["frontend"]
tags = ["CSS"]
title = "用border-image+SVG实现切角效果"
keywords = ["切角效果", "SVG", "border-image"]
description = "切角效果在网页设计中非常流行，大多数网页开发者倾向于使用背景图片来实现，其实我们可以用border-image+SVG实现切角效果"
url = "/bevel-corners-svg.html"
date = "2017-05-06T16:19:48+08:00"

+++

之前写了一篇文章，介绍了[基于CSS渐变来实现切角效果](http://www.wangxingfeng.com/bevel-corners.html)的方法。今天再来介绍另一种方法，即使用`border-image`+`SVG`的方式来实现`切角效果`。

##  border-image的工作原理
给一个元素设置边框，我们会使用`border`这个属性。`border`是`border-width`、`border-style`、`border-color`等3个属性的简写形式。

我们给div设置一个宽20px、实线、颜色为`#58a`的边框。

```css
	div{
		width:200px;
		height:150px; 
		margin:20px auto;
		border:40px solid #58a;
	}
```
<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a;"></div>


`border-image`是CSS3的新属性，用于指定元素边框的背景图片。使用 border-image 时，border-style属性所设置的边框样式solid、dashed或dotted将不起作用。

`border-image`属性也是一个简写：包含`border-image-source`、`border-image-slice`、`border-image-width`、`border-image-outset`、`border-image-repeat`等5个属性。

### 1. `border-image-source`: 

从这个属性的英文命名，我们就可以知道它表示的是边框背景图片资源的路径，默认值是`none`。

```css
	div{
		width:200px;
		height:150px;
		margin:20px auto;
		border:40px solid #58a;
		border-image-source:url(/images/adamcatlace.jpg);
	}
```

<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a; border-image-source:url(/images/adamcatlace.jpg)"></div>


### 2. `border-image-slice`: 

`border-image-slice`属性指定图像的边界向内偏移。


```css
	div{
		width:200px;
		height:150px;
		margin:20px auto;
		border:40px solid #58a;
		border-image-source:url(/images/adamcatlace.jpg);
		border-image-slice:10% 20% 30% 40%; 
		border-image-repeat: none;
	}
```

<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a; border-image:url(/images/adamcatlace.jpg);border-image-slice:10% 20% 30% 40%; border-image-repeat: round stretch;"></div>


```css
	div{
		width:200px;
		height:150px;
		margin:20px auto;
		border:40px solid #58a;
		border-image-source:url(/images/adamcatlace.jpg);
		border-image-slice: 10% 30%;
	}
```

<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a; border-image:url(/images/adamcatlace.jpg); border-image-slice: 10% 30%;"></div>


```css
	div{
		width:200px;
		height:150px;
		margin:20px auto;
		border:40px solid #58a;
		border-image-source:url(/images/adamcatlace.jpg);
		border-image-slice: 30 30% 45;
	}
```

<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a; border-image:url(/images/adamcatlace.jpg); border-image-slice: 30 30% 45;"></div>

```css
	div{
		width:200px;
		height:150px;
		margin:20px auto;
		border:40px solid #58a;
		border-image-source:url(/images/adamcatlace.jpg);
		border-image-slice: 7 12 14 5; 
	}
```

<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a; border-image:url(/images/adamcatlace.jpg); border-image-slice: 7 12 14 5; "></div>

```css
	div{
		width:200px;
		height:150px;
		margin:20px auto;
		border:40px solid #58a;
		border-image-source:url(/images/adamcatlace.jpg);
		border-image-slice: 10% fill 7 12; 
	}
```

<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a; border-image:url(/images/adamcatlace.jpg); border-image-slice: border-image-slice: 10% fill 7 12; "></div>



```css
    .demo{
        border:30px solid transparent;
        border-image:1 url('data:image/svg+xml,\
            <svg xmlns="http://www.w3.org/2000/svg" width="3" height="3" fill="red">\
              <polygon points="0,1 1,0 2, 0 3, 1 3, 2 2, 3 1, 3 0, 2"/>\
            </svg>');
    }
```

<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" fill="purple">
    <polygon points="0, 100 100, 0 200, 0 300, 100 300, 200 200, 300 100, 300 0, 200"/>
</svg>
<div class="demo bevel-corners-8">
</div>

<div>
	
</div>
