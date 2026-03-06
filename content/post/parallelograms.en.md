+++
tags = ["CSS"]
date = "2017-04-30T16:44:06+08:00"
title = "Parallelograms"
keywords = ["CSS transform", "skew", "parallelogram", "Pseudo element"]
description = "Two ways to use CSS to draw parallelograms with non-skewed content: nested element scheme and pseudo-element scheme"
categories = ["frontend"]
url = "/parallelograms.html"
+++

## 1. Parallelogram

Ordinary web elements are rectangular. But sometimes, we need to create shapes that convey a sense of movement, like a parallelogram.

Speaking of `skew`, we will think of using the `skew()` method of the `transform` attribute to `obliquely stretch` ordinary rectangular elements.

width:100px;
	height:60px;
	transform: skew(-30deg);

<div style="width:100px;height:60px;margin:10px auto;color:#fff;background: #673ab7;font-size: 16px;line-height: 60px;text-align: center;transform: skew(-30deg);">Parallelogram</div>

As shown above, we get a parallelogram, but the content is also deformed diagonally. We want only the container to be tilted, but not the content. what to do?

## 2. Nested element solution

First, we can first add an element inside the container, wrap the content inside, and perform diagonal deformation on this element again. The value is the negative diagonal deformation value of the outer container, which can just offset the oblique deformation.

HTML code

	<div class="parallelograms-container">
		<div class="parallelograms-inner">
parallelogram
		</div>
	</div>

CSS code

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
parallelogram
	</div>
</div>

## 3. Pseudo element scheme

If we don't want to add additional HTML structures, can we do it with pure CSS?

The answer is yes.

We can consider using CSS to generate `pseudo-elements`, then apply all styles (background, borders, etc.) to the pseudo-elements, use `absolute positioning` to overlap the pseudo-elements under the content, and then perform `diagonal stretch` deformation on the pseudo-elements. This way the content remains unskewed.

HTML code
	
	<div class="pseudo-container">
parallelogram
	</div>


CSS code

.pseudo-container{
		position:relative;
		/* The text size, color, padding and other styles of the content are here*/
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


The effect is as follows:
<div class="pseudo-container">
parallelogram
</div>

**Notice:**

Note that there is a small pit here. Since we set `z-index:-1` for this pseudo-element, we must ensure that the background of the container of this pseudo-element and the `ancestor element` of the container (the `direct child element` that goes back to `<body>`) must be transparent, otherwise the `pseudo-element` will be covered.