+++
categories = ["frontend"]
tags = ["CSS"]
title = "Bevel Corners Svg"
keywords = ["Corner effect", "SVG", "border-image"]
description = "The corner cutting effect is very popular in web design. Most web developers tend to use background images to achieve it. In fact, we can use border-image+SVG to achieve the corner cutting effect."
url = "/bevel-corners-svg.html"
date = "2017-05-06T16:19:48+08:00"

+++

I wrote an article before, introducing the method of [achieving corner cutting effect based on CSS gradient](http://frankwang0909.github.io/bevel-corners.html). Today I will introduce another method, which is to use `border-image`+`SVG` to achieve the `corner cutting effect`.

## How border-image works
To set a border for an element, we will use the `border` attribute. `border` is the abbreviation of `border-width`, `border-style` and `border-color`.

We set a border with a width of 20px, a solid line, and a color of `#58a` for the div.

```css
	div{
		width:200px;
		height:150px; 
		margin:20px auto;
		border:40px solid #58a;
	}
```
<div style="width:200px; height:150px; margin:20px auto; border:40px solid #58a;"></div>


`border-image` is a new attribute of CSS3, used to specify the background image of the element border. When using border-image, the border style solid, dashed or dotted set by the border-style property will have no effect.

The `border-image` attribute is also an abbreviation: including `border-image-source`, `border-image-slice`, `border-image-width`, `border-image-outset`, `border-image-repeat` and other 5 attributes.

### 1. `border-image-source`:

From the English name of this attribute, we can know that it represents the path of the border background image resource, and the default value is `none`.

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

The `border-image-slice` attribute specifies that the border of the image is offset inwards.


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
