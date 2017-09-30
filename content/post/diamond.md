+++
date = "2017-05-01T22:00:03+08:00"
categories = ["frontend"]
tags = ["CSS"]
keywords = ["菱形图片", "裁切路径", "clip-path", "CSS变形"]
description = "把图片裁切成菱形是一种常见的视觉设计手法。传统的实现方法是预先在图像处理软件中把图片裁切好，而现在，CSS的新特性已经可以支持用CSS代码来实现菱形图片。"
url = "/diamond-picture.html"
title = "如何用CSS代码实现网页设计中的菱形图片"
+++
<style>
div.diamond-pic{width:200px;transform: rotate(45deg);overflow: hidden;margin:60px auto;}
img.diamond-img{max-width:100%;transform: rotate(-45deg);}
img.diamon-pic-clip-path{clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);}
img.diamon-pic-clip-path-2{clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);transition: 1s clip-path;}
img.diamon-pic-clip-path-2:hover{clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);}
</style>

在网页设计中，我们常常能够看到被裁切成菱形的图片。

传统的实现方式是预先在图像处理软件中把图片裁切好，当然这种方式的可维护性差。

而现在，随着CSS的新特性的支持度越来越好了，CSS也越来越强大，我们已经可以用CSS代码来实现菱形图片了。

## 1. 基于tranform的实现方法

原图
<img src="/images/adamcatlace.jpg" style="display:block; max-width: 200px; margin:30px auto">
用一个`<div>` 把图片包裹起来，对这个容器`<div>`应用`transform:rotate(45deg)`, 进行旋转45度，我们得到如下的效果：图片应该也会跟着旋转了

```css
div{
	width:200px;
	transform: rotate(45deg);
	overflow: hidden;
};
```

<div class="diamond-pic">
	<img src="/images/adamcatlace.jpg" >
</div>

如果我们对里面的图片进行反向旋转45度，那么图片的旋转就会抵消掉。看看效果。
```css
	div>img{
		max-width:100%;
		transform: rotate(-45deg);
	};
```

<div class="diamond-pic" >
	<img src="/images/adamcatlace.jpg" class="diamond-img" >
</div>

我们得到了一个裁成`八边形`的图片。

问题出在哪里呢？我给外面的`div`加一个边框，这样就容易看出来了。

<div class="diamond-pic" style="border:1px solid red;">
	<img src="/images/adamcatlace.jpg" class="diamond-img">
</div>

问题出在了这里图片的宽度是与容器`div`的`边长`相等，其实我们应该让图片的宽度与`对角线`相等。

运用勾股定理，可以计算出图片的宽度应该是√2倍，我们取1.42倍。

如果通过`width属性`设置来放大图片,会得到如下的效果。
```css
	div>img{
		width:142%;
		max-width:142%;
		transform: rotate(-45deg);
	};
```

<div class="diamond-pic">
	<img src="/images/adamcatlace.jpg" class="diamond-img" style="width:142%;max-width:142%;">
</div>

因为是以图片的`左上角`为原点进行放大的。我们还需要在通过设置`margin:-45px;`才能得到菱形图片。
```css
	div>img{
		max-width:142%;
		transform: rotate(-45deg);
		margin:-45px;
	};
```

<div class="diamond-pic">
	<img src="/images/adamcatlace.jpg" class="diamond-img" style="width:142%;max-width:142%;margin:-45px">
</div>

当然，我们可以通过`transform:scale(1.42)`来放大图片1.42倍。`scale()`是以图片的`中心点`进行缩放的，这样我们就不用额外地设置`margin`值了。

	div>img{
		max-width:100%;
		transform: scale(1.42) rotate(-45deg);
	};

<div class="diamond-pic">
	<img src="/images/adamcatlace.jpg" class="diamond-img" style="transform: rotate(-45deg) scale(1.42);">
</div>


## 2. 基于裁切路径 clip-path 方法

第一种方法虽然可以奏效，但存在一些缺点：

- 1.需要一层额外的HTML标签；
- 2.代码不够直观；
- 3.如果处理的图片不是正方形，将无法得到一个菱形图片，如下图所示：

<div class="diamond-pic">
	<img src="/images/adam-sleeping.jpg" class="diamond-img" style="transform: rotate(-45deg) scale(1.42);">
</div>

`SVG`中，有个名叫`<clipPath>`的元素，专门用来定义剪裁路径。其实CSS中也有一个类似的属性，即`clip-path属性`。

`clip-path`可以把元素裁切成我们想要的任何形状。我们通过`polygon()函数`来指定一个菱形，参数是一系列用`逗号`分隔的`坐标点`。
```css
img{
	clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);
}
```

<img src="/images/adam-sleeping.jpg" class="diamon-pic-clip-path" >


如上图所示，这个方法可以很好的适应非正方形的图片。

另外，因为`clip-path`属性可以参与动画，我们还可以给这个图片动画过渡效果。比如，当我们的鼠标悬停到图片上时，菱形图片平滑地扩展为完整的原图。
```css
img{
	clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);
	transition: 1s clip-path;
}
img:hover{
	clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}
```


<img src="/images/adam-sleeping.jpg" class="diamon-pic-clip-path-2" >

注意，除了谷歌浏览器，其他浏览器对这个clip-path属性的支持度都还不是很好。