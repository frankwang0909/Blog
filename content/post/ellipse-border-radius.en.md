+++
title = "Ellipse Border Radius"
keywords = ["border-radius", "Draw an ellipse", "semi-oval", "quarter ellipse"]
description = "Draw ellipse, half ellipse, quarter ellipse with CSS"
categories = ["frontend"]
tags = ["CSS"]
date = "2017-04-30T11:25:58+08:00"
url = "/ellipse-border-radius.html"
+++

## 1. border-radius

`border-radius` can add rounded borders to elements, such as buttons.

<button style="display:block; width:160px; height:60px; margin:10px auto;color:#fff;background: #ff5722; border-radius:8px; border:none;outline:none; ">
Example button
</button>

## 2. Compatibility: IE9+ and above are well compatible with border-radius


## 3. border-radius draws a circle

If we set a border-radius value large enough for a square element (as long as it is greater than or equal to half the side length of the square), the element can be turned into a circle.
But considering that the height and width of the element may not be fixed, we can set a percentage, which is parsed based on the size of the element. When we set border-radius: 50% to a square element, we will get an adaptive circle.
```css
	width:200px;
	height:200px;
border-radius:50%; /*This is equivalent to border-radius:100px; it is recommended to write it as a percentage*/
```

As shown below:

<div style="width:200px; height:200px; border-radius: 50%; background: #03a9f4; margin: 10px auto"></div>

## 4. border-radius draws adaptive ellipse

Let's take a look at what will happen when the height and width of the elements are not equal.

```css
width: 300px;/* Width is longer */
	height:200px;
	border-radius:50%; 
```


As shown below:

<div style="width:300px; height:200px; border-radius: 50%; background: #cddc39; margin: 10px auto"></div>

As shown in the figure above, when the height and width of the element are not equal and `border-radius` is set to 50%, we will get an adaptive ellipse.

## 5. border-radius draws half an ellipse

What if you want to get half an ellipse?

<div style="width:300px; height:100px; border-radius: 50% / 100% 100% 0 0; background: #795548; margin: 10px auto"></div>

We need to add the following two knowledge points:

- 1. The value of `border-radius` can specify the radius in the horizontal direction and the radius in the vertical direction separately. A slash (/) needs to be used to separate the two values.

- 2.`border-radius` is a shorthand attribute, we can specify different values ​​for each corner of the element individually. `border-radius` expands into the following 4 attributes:

border-top-left-radius
	border-top-right-radius
	border-bottom-right-radius
	border-bottom-left-radius


We don't have to write them separately, we can specify 4 values ​​for `border-radius`, separated by spaces. When the browser parses, it is applied to the four corners of the element in clockwise order (similar to the abbreviations of other common attributes such as `margin` and `padding`).

Let's analyze this semi-ellipse.

- 1. It is vertically symmetrical, which means that the radius values ​​of the upper left corner and the upper right corner are the same; the radius values ​​of the lower left corner and the lower right corner should also be the same.

- 2. Its top edge is curved, which means that the sum of the radius values ​​​​of the upper left corner and the upper right corner should be equal to the width of this element.

- 3. It can be deduced from the previous two points that the radius of the upper left corner and the upper right corner is 50% in the horizontal direction.

- 4. Looking at the vertical direction, the two rounded corners at the top occupy the entire height of the element, while the bottom has no rounded corners at all. Therefore, it can be inferred that the radius of the upper left and upper right corners is 100% in the vertical direction, and the radius of the lower left and lower right corners is 0 in the vertical direction.


To sum up, the value of `border-radius` should be `50% / 100% 100% 0 0`;

```css
	width:300px;
	height:100px;
	border-radius: 50% / 100% 100% 0 0;
```

<div style="width:300px; height:100px; border-radius: 50% / 100% 100% 0 0; background: #795548; margin: 10px auto"></div>

If we change the value in the vertical direction to `0 0 100% 100%`, we can get another half-ellipse.

```css
	width:300px;
	height:100px;
	border-radius: 50% /0 0 100% 100% ;
```

<div style="width:300px; height:100px; border-radius: 50% / 0 0 100% 100%; background: #4caf50; margin: 10px auto"></div>

If you set the `horizontal` border-raduis` to `50%`; in the `vertical direction`, the upper left corner and lower left corner are set to `100%`; and the upper right corner and lower right corner are set to `0`, you can get a `semi-oval split along the Y axis`.
```css
	width:150px;
	height:200px;
	border-radius: 100% 0 0 100% / 50%;
```
<div style="width:150px; height:200px; border-radius: 100% 0 0 100% / 50%; background: #9c27b0; margin: 10px auto"></div>

## 6.border-radius draws a quarter of the ellipse

What if you want to get a quarter of an ellipse? Following the previous idea, we can set the `border-radius` value of one corner to `100%` and the other three corners to `0`.
```css
	width:150px;
	height:100px;
	border-radius: 100% 0 0 0;
```
<div style="width:150px; height:100px; border-radius: 100% 0 0 0; background: #9e9e9e; margin: 10px auto"></div>