+++
date = "2017-05-01T22:00:03+08:00"
categories = ["frontend"]
tags = ["CSS"]
keywords = ["rhombus picture", "clipping path", "clip-path", "CSS transformation"]
description = "Cutting images into diamond shapes is a common visual design technique. The traditional implementation method is to crop the image in advance in image processing software, but now, the new features of CSS can already support the use of CSS code to implement diamond-shaped images."
url = "/diamond-picture.html"
title = "Diamond"
+++
<style>
div.diamond-pic{width:200px;transform: rotate(45deg);overflow: hidden;margin:60px auto;}
img.diamond-img{max-width:100%;transform: rotate(-45deg);}
img.diamon-pic-clip-path{clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);}
img.diamon-pic-clip-path-2{clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);transition: 1s clip-path;}
img.diamon-pic-clip-path-2:hover{clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);}
</style>

In web design, we often see pictures cut into diamond shapes.

The traditional implementation method is to crop the image in advance in the image processing software. Of course, this method has poor maintainability.

Now, as the support for new features of CSS is getting better and better, CSS is becoming more and more powerful, and we can already use CSS code to implement diamond-shaped images.

## 1. Implementation method based on transform

Original picture
<img src="/images/adamcatlace.jpg" style="display:block; max-width: 200px; margin:30px auto">
Wrap the image with a `<div>`, apply `transform:rotate(45deg)` to the container `<div>`, and rotate it 45 degrees. We will get the following effect: the image should also rotate accordingly.

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

If we reversely rotate the image inside by 45 degrees, the rotation of the image will be offset. See the effect.
```css
	div>img{
		max-width:100%;
		transform: rotate(-45deg);
	};
```

<div class="diamond-pic" >
	<img src="/images/adamcatlace.jpg" class="diamond-img" >
</div>

We get an image cut into an octagon.

What's the problem? I added a border to the outer div so it's easier to see.

<div class="diamond-pic" style="border:1px solid red;">
	<img src="/images/adamcatlace.jpg" class="diamond-img">
</div>

The problem lies in that the width of the image is equal to the `side length` of the container `div`. In fact, we should make the width of the image equal to the `diagonal`.

Using the Pythagorean theorem, we can calculate that the width of the picture should be √2 times, and we take 1.42 times.

If you enlarge the image through the `width attribute` setting, you will get the following effect.
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

Because the `upper left corner` of the picture is used as the origin for enlarging. We also need to set `margin:-45px;` to get the diamond image.
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

Of course, we can enlarge the image 1.42 times through `transform:scale(1.42)`. `scale()` scales based on the `center point` of the image, so we do not need to set additional `margin` values.

div>img{
		max-width:100%;
		transform: scale(1.42) rotate(-45deg);
	};

<div class="diamond-pic">
	<img src="/images/adamcatlace.jpg" class="diamond-img" style="transform: rotate(-45deg) scale(1.42);">
</div>


## 2. Based on the clip-path method

Although the first method can work, it has some disadvantages:

- 1. An additional layer of HTML tags is required;
- 2. The code is not intuitive enough;
- 3. If the image being processed is not square, you will not be able to get a diamond-shaped image, as shown in the figure below:

<div class="diamond-pic">
	<img src="/images/adam-sleeping.jpg" class="diamond-img" style="transform: rotate(-45deg) scale(1.42);">
</div>

In `SVG`, there is an element named `<clipPath>`, which is specially used to define the clipping path. In fact, there is a similar property in CSS, namely the `clip-path property`.

`clip-path` can clip elements into any shape we want. We specify a rhombus through the `polygon() function`, and the parameter is a series of `coordinate points` separated by `comma`.
```css
img{
	clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);
}
```

<img src="/images/adam-sleeping.jpg" class="diamon-pic-clip-path" >


As shown in the figure above, this method can be well adapted to non-square images.

In addition, because the `clip-path` attribute can participate in animation, we can also animate the transition effect of this image. For example, when our mouse hovers over the image, the diamond-shaped image smoothly expands into the complete original image.
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

Note that except for Google Chrome, other browsers do not yet have very good support for this clip-path attribute.