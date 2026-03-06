+++
categories = ["frontend"]
tags = ["CSS"]
date = "2017-05-02T22:52:17+08:00"
title = "Bevel Corners"
keywords = ["Corner effect", "CSS to achieve corner cutting effect", "Arc chamfer"]
description = "The corner-cutting effect is very popular in web design. Most web developers tend to use background images to achieve it. Here is a pure CSS solution that can achieve the corner-cutting effect using only CSS code."
url = "/bevel-corners.html"

+++

In the flat design style, bevel corners are very popular, that is, cutting one or more corners of an element into a 45-degree notch. Most web developers tend to use background images to achieve the corner cutout effect. However, using background images will add additional HTTP requests, increase web page loading time, and make it difficult to modify and maintain. In fact, CSS is powerful enough to provide a pure CSS solution, and we can achieve the corner cutting effect using only CSS code.

## Corner effect based on `CSS gradient`

If you are familiar with CSS gradients, you should know that CSS gradients can accept an angle as the direction, and you can also set the position of the percentage color scale. Of course, the position of the color mark can also be set to an absolute length value.
<style>
.demo{
        width:300px;
        height: 200px;
        margin:10px auto;
    }
    .demo1{
        background: linear-gradient(-45deg, red, green);
    }
    .demo2{
        background: linear-gradient(-45deg, red 20%, green 70%);
    }
    .demo3{
        background: linear-gradient(-45deg, red 20%, green 0);
    }
    .demo4{
        background: linear-gradient(-45deg, transparent 20%, green 0);
    }
    .demo5{
        background: linear-gradient(-45deg, transparent 30px, green 0),
                    linear-gradient(45deg, transparent 30px, red 0);
    }
    .demo6{
        background: linear-gradient(-45deg, transparent 30px, green 0) right,
                    linear-gradient(45deg, transparent 30px, red 0) left;
        background-size:50% 100%;
        background-repeat:no-repeat;
    }
    .demo7{
        background: linear-gradient(135deg, transparent 30px, green 0) top left,
            linear-gradient(-135deg, transparent 30px, red 0) top right,
            linear-gradient(-45deg, transparent 30px, pink 0) bottom right,
            linear-gradient(45deg, transparent 30px, blue 0) bottom left;
        background-size: 50% 50%;
        background-repeat: no-repeat;
    }
</style>

### 1. Ordinary linear gradient

We set -45 degrees as the gradient direction, that is, the direction of the gradient from the lower right corner to the upper left corner.

```css
.demo{
    background: linear-gradient(-45deg, red, green);
}
```

The rendering effect is like this:

<div class="demo demo1"></div>


### 2. Set the linear gradient of the color scale value

Let's set a percentage for these two color stops and see what the effect will be.


```css
.demo{
    background: linear-gradient(-45deg, red 20%, green 70%);
}
```

The meaning of the above code is that in the direction of the gradient from the lower right corner to the upper left corner, 0~20% of the area is pure red, 20%-70% of the area is gradient, and 70%-100% of the area is pure green.
<div class="demo demo2"></div>

### 3. Linear gradient with color scale value 0
 
If we make some slight modifications and change the second color scale value to 0, what will be the effect?

```css
.demo{
    background: linear-gradient(-45deg, red 20%, green 0);
}
```

<div class="demo demo3"></div>

A little surprised? !

The graph we get has no gradient. In the direction of the gradient from the lower right corner to the upper left corner, the 0-20% area is pure red, and the 20%-100% area is pure green.

Note: As long as the second color scale value is smaller than the previous color scale value, the browser will parse it to the previous color scale value by default.

The above CSS code is equivalent to:


```css
.demo{
    background: linear-gradient(-45deg, red 20%, green 20%);
}
```

### 4. Corner cutting effect

Modify the above code slightly and change the `red` in the lower right corner to `transparent`, and you will get a `corner cutting effect` in the lower right corner.


```css
.demo{
    background: linear-gradient(-45deg, transparent 20%, green 0);
}
```


<div class="demo demo4"></div>


In fact, in actual web development, we prefer a fixed-size corner cut. Then, we can change the percentage to an absolute length value, such as changing 20% ​​to 30px.


### 5. Two corner cutting effects

If we need more than one corner cut, how to achieve it?

Is it possible to declare two gradient rules? Let's try it out.


```css
.demo{
    background: linear-gradient(-45deg, transparent 30px, green 0),
                linear-gradient(45deg, transparent 30px, red 0);
}
```

<div class="demo demo5"></div>

The attempt failed. Because by default, both gradients will fill the entire element, causing them to overlap. At this time, we need to use `background-size` and `background-repeat`, so that each gradient layer occupies half of the entire element.



```css
.demo{
    background: linear-gradient(-45deg, transparent 30px, green 0) right,
                linear-gradient(45deg, transparent 30px, red 0) left;
    background-size:50% 100%;
    background-repeat:no-repeat;
}
```

<div class="demo demo6"></div>

### 6. Four corner cutting effects

After looking at the implementation of two corner cuts, you must be able to deduce the idea of ​​​​achieving the "four corner cut effects". We need 4 layers of gradients, each of which only takes up 1/4 of the entire element. In the example below, I used 4 different colors to express the size and position of each layer's gradient more intuitively.

```css
.demo{
    background: linear-gradient(135deg, transparent 30px, green 0) top left,
        linear-gradient(-135deg, transparent 30px, red 0) top right,
        linear-gradient(-45deg, transparent 30px, pink 0) bottom right,
        linear-gradient(45deg, transparent 30px, blue 0) bottom left;
    background-size: 50% 50%;
    background-repeat: no-repeat;
}
```
<div class="demo demo7"></div>
