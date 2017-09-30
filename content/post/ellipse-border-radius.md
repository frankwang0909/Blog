+++
title = "用CSS绘制椭圆、半椭圆、四分之一椭圆"
keywords = ["border-radius", "绘制椭圆", "半椭圆", "四分之一椭圆"]
description = "用CSS绘制椭圆、半椭圆、四分之一椭圆"
categories = ["frontend"]
tags = ["CSS"]
date = "2017-04-30T11:25:58+08:00"
url = "/ellipse-border-radius.html"
+++

## 1. border-radius

`border-radius` 可以为元素添加圆角边框，比如 按钮。

<button style="display:block; width:160px; height:60px; margin:10px auto;color:#fff;background: #ff5722; border-radius:8px; border:none;outline:none; ">
	示例按钮
</button>

## 2. 兼容性： IE9+以上都很好地能够兼容  border-radius


## 3. border-radius 绘制圆形

如果我们给一个正方形的元素设置一个足够大的border-radius值（只要大于等于正方形边长的一半）的话，就可以被这个元素变成圆形。
但考虑到元素的高宽可能不是固定的，那么，我们可以设置百分比，这个百分比是基于元素的尺寸大小来解析的。当我们给一个正方形的元素设置border-radius：50%时，我们会得到一个自适应的圆形。
```css
	width:200px;
	height:200px;
	border-radius:50%; /*在这里等价于border-radius:100px; 建议写成百分比*/
```

如下所示：

<div style="width:200px; height:200px; border-radius: 50%; background: #03a9f4; margin: 10px auto"></div>

## 4. border-radius 绘制自适应椭圆

当元素的高宽不相等时，我们来看下会变成什么样子。

```css
	width:300px; /*宽度变长了*/
	height:200px;
	border-radius:50%; 
```


如下所示：

<div style="width:300px; height:200px; border-radius: 50%; background: #cddc39; margin: 10px auto"></div>

如上图所示，当元素的高宽不相等，`border-radius` 设置为 50%，我们将会得到一个自适应的椭圆。

## 5. border-radius 绘制半个椭圆

如果想要得到半个椭圆，怎么办呢？

<div style="width:300px; height:100px; border-radius: 50% / 100% 100% 0 0; background: #795548; margin: 10px auto"></div>

我们需要补充以下两个知识点：

- 1.`border-radius`的值是可以单独指定水平方向上的半径和垂直方向上的半径的，中间需要用一个斜杠(/)分隔开两个值。

- 2.`border-radius`是一个简写属性，我们可以单独为元素的每个角指定不同的值。`border-radius` 展开的话是以下4个属性：

	border-top-left-radius
	border-top-right-radius
	border-bottom-right-radius
	border-bottom-left-radius


我们不必分开写，可以给`border-radius`指定4个值，用空格分开。浏览器解析的时候，是按顺时针顺序应用到元素的四个角的（和`margin`、`padding`等其他的常见属性的简写类似）。

我们来分析一下这个半椭圆形。

- 1.它是垂直对称的，说明左上角和右上角的半径值是相同的；左下角和右下角的半径值也应该是相同的。

- 2.它的顶部边缘是曲线的，说明左上角和右上角的半径值之和应该是等于这个元素的宽的。

- 3.由前面两点可以推出，左上角和右上角的半径在水平方向上是50%。

- 4.再看垂直方向上，顶部的两个圆角占据了整个元素的高度，而底部完全没有任何圆角。因此，可以推断左上角和右上角的半径在垂直方向上是100%，左下角和右下角在垂直方向上是0。


综上所述，`border-radius`的值应该是`50% / 100% 100% 0 0`;

```css
	width:300px;
	height:100px;
	border-radius: 50% / 100% 100% 0 0;
```

<div style="width:300px; height:100px; border-radius: 50% / 100% 100% 0 0; background: #795548; margin: 10px auto"></div>

如果我们把垂直方向上的值改为`0 0 100% 100%`，则可以得到另一个半椭圆。

```css
	width:300px;
	height:100px;
	border-radius: 50% /0 0 100% 100% ;
```

<div style="width:300px; height:100px; border-radius: 50% / 0 0 100% 100%; background: #4caf50; margin: 10px auto"></div>

如果把`水平方向``border-raduis`设置为`50%`; `垂直方向`上，左上角和左下角设置为`100%`； 右上角和右下角设为`0`，则可以得到一个`沿Y轴劈开的半椭圆形`。
```css
	width:150px;
	height:200px;
	border-radius: 100% 0 0 100% / 50%;
```
<div style="width:150px; height:200px; border-radius: 100% 0 0 100% / 50% ; background: #9c27b0; margin: 10px auto"></div>

## 6.border-radius 绘制椭圆的四分之一

如果想要得到四分之一个椭圆呢？顺着之前的思路，我们可以设置其中一个角的`border-radius`值为`100%`，其他三个角为`0`.
```css
	width:150px;
	height:100px;
	border-radius: 100% 0 0 0;
```
<div style="width:150px; height:100px; border-radius: 100% 0 0 0 ; background: #9e9e9e; margin: 10px auto"></div>