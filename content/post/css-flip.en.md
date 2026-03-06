+++
title = "Css Flip"
tags = ["CSS"]
keywords = ["CSS3", "transform","Image flip","Page flip effect", "rotateY"]
description = "How to achieve image flipping effect with CSS, how to achieve page flipping effect with CSS, CSS3, transform,"
categories = ["frontend"]
date = "2017-04-29T21:24:00+08:00"
url ="/css-flip.html"
+++
<style>

.back, .front, .rotate-container{
	width: 320px;
    height: 380px;
    margin: 0 auto;
    text-align: center;
    color: #00f;
}
.flipper {
    transition-duration: 1s;
    transform-style: preserve-3d;
    position: relative;
}
.rotate-container.hover .flipper,.rotate-container:hover .flipper {
    transform: rotateY(180deg)
}
.back, .front {
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

## Use CSS to achieve animation effects of page or image flipping
There are often animation interactive effects in web development. In the past, we could only use JavaScript to achieve it. As browsers support the new features of CSS3 better and better, many special effects can be achieved through CSS code.

When we browse the website, we can often see the animation effect of the picture flipping, such as shown in `Demo 1`.


<div class="rotate-container" style="border:2px solid #000;">
	<div class="flipper">
		<div class="front">
<!-- Previous content -->
<p >Positive content</p>
			<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
		</div>
		<div class="back">
<p>Negative content</p>
			<img src="https://images-cn.ssl-images-amazon.com/images/G/28/kindle/merch/2014/campaign/Gen7-Launch/Associate/Associate_AssociateCenrter_300_250_Family._V325383366_.jpg" alt="">
		</div>
	</div>
</div>


Can this flip animation effect be achieved using pure CSS? The answer is yes.

We know that the `transform` property of CSS3 is very powerful and can achieve 2D or 3D rotation, scaling, movement or tilt.

The above Demo1 is a 3D flip along the Y axis. We can think of using the `rotateY()` method of the `transform` attribute to achieve this.

## Sample code

HTML code
```html
<div class="rotate-container">
	<div class="flipper">
		<div class="front">
<!-- Previous content -->
		</div>
		<div class="back">
<!-- Back content -->
		</div>
	</div>
</div>
```

CSS code
```css
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
```

## Explanation of key technical points:

### 1.transform: deformation

`transform: rotateY(180deg)` means rotating 180 degrees along the Y axis.

<p>Demo2: Rotate 180 degrees along the Y axis (rotate until the back is visible)</p>
<div class="rotateY rotateY180">
	<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
</div>
<p>Demo3: Rotate 90 degrees along the Y axis</p>
<div class="rotateY rotateY90">
	<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
</div>
<p>Demo4: Rotate 45 degrees along the Y axis</p>
<div class="rotateY rotateY45">
	<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
</div>


### 2.transform-style: Specify the space where the child elements of this element are located.

Specifies whether the element's children appear to lie in three-dimensional space or are flattened in the element's plane.

The `transform-style` attribute has two parameters, `flat` and `preserve-3d`. `flat` is the default value, specifying that the child element is located in the plane where this element is located; `preserve-3d` specifies that the child element is positioned in a three-dimensional space.

### 3.backface-visibility specifies whether the element is visible when rotated to the back.

The default is visible, that is, the back side is visible, as shown in `Demo2`.

In Demo1, since it is another picture that is flipped over, the back face is not visible when it is set to backface-visibility:hidden.

<p>Demo5: Rotate 180 degrees along the Y axis (rotate until the back is invisible)</p>
<div class="rotate-container">
	<div class="flipper" >
		<div class="front">
			<img src="https://images-cn.ssl-images-amazon.com/images/I/51fD0ZgQoXL._SL400_.jpg" alt="">
		</div>
	</div>
</div>

### 4.transition-duration: Indicates the time it takes to complete the transition effect.

`transition-duration:1s` can be used in the abbreviated form `transition:1s`.

### 5.position:absolute: absolute positioning.

Use absolute positioning `position:absolute` to place the two elements before and after flipping in the same position.
