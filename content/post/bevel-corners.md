+++
categories = ["frontend"]
tags = ["CSS"]
images = []
banner = ""
menu = ""
date = "2017-05-02T22:52:17+08:00"
title = "CSS实现切角效果"
keywords = "切角效果，CSS实现切角效果，弧形切角，"
description = "切角效果在网页设计中非常流行，大多数网页开发者倾向于使用背景图片来实现，这里提供纯CSS的解决方案，仅用CSS代码就能实现切角效果。"
url = "bevel-corners.html"

+++

扁平化设计风格中，很流行斜面切角，即把元素的一个或多个角切成45度的缺口。大多数网页开发者倾向于使用背景图片来实现切角效果。但使用背景图片会增加额外的HTTP请求，增加网页加载的时间，难以修改和维护。实际上，CSS已经足够强大，可以提供纯CSS的解决方案，我们仅用CSS代码就能实现切角效果。

## 基于`CSS渐变`的切角效果

如果你对CSS渐变不陌生的话，应该知道CSS渐变可以接受`一个角度`作为方向，还可以设置百分比的色标的位置。当然，色标的位置也可以设置为绝对的长度值。
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

### 1.普通的线性渐变

我们设置-45度为渐变方向，即从右下角到左上角渐变的方向。

```css
.demo{
    background: linear-gradient(-45deg, red, green);
}
```

渲染的效果是这样的：

<div class="demo demo1"></div>


### 2.设置色标值的线性渐变

我们给这两个色标设置一个百分比，看看会是什么效果。


```css
.demo{
    background: linear-gradient(-45deg, red 20%, green 70%);
}
```

上述代码的意思从右下角到左上角渐变的方向上，0~20%的区域是纯红色的，20%-70%的区域是渐变，70%-100%的区域是纯绿色的。
<div class="demo demo2"></div>

### 3.色标值为0的线性渐变
 
如果我们再稍微做些修改，把第二个色标值改为0，会是什么效果呢？

```css
.demo{
    background: linear-gradient(-45deg, red 20%, green 0);
}
```

<div class="demo demo3"></div>

是不是有点惊讶？！

我们得到的图形是没有渐变的。从右下角到左上角渐变的方向上，0-20%的区域是纯红色，20%-100%的区域就是纯绿色。

    注意：只要第二个色标值小于前一个色标值，那么浏览器就会默认解析为前一个色标值的。

上面的CSS代码等价于：


```css
.demo{
    background: linear-gradient(-45deg, red 20%, green 20%);
}
```

### 4.切角效果

将上面的代码再稍作改动，把右下角的`红色`改成`透明色`, 就能得到一个右下角的`切角效果`。


```css
.demo{
    background: linear-gradient(-45deg, transparent 20%, green 0);
}
```


<div class="demo demo4"></div>


其实，实际的网页开发中，我们更倾向于一个固定大小的切角。那么，我们可以把百分比改为绝对的长度值，比如把20%改为30px.


### 5.两个切角效果

如果我们需要的切角不止一个，怎么实现呢？

是不是可以声明两条渐变规则呢？我们来试一下效果。


```css
.demo{
    background: linear-gradient(-45deg, transparent 30px, green 0),
                linear-gradient(45deg, transparent 30px, red 0);
}
```

<div class="demo demo5"></div>

尝试失败。因为默认情况下，两层渐变都会填满整个元素，导致相互重叠。这个时候，我们就需要用到`background-size`和`background-repeat`,让每层渐变分别占据整个元素的一半。



```css
.demo{
    background: linear-gradient(-45deg, transparent 30px, green 0) right,
                linear-gradient(45deg, transparent 30px, red 0) left;
    background-size:50% 100%;
    background-repeat:no-repeat;
}
```

<div class="demo demo6"></div>

### 6.四个切角效果

看了两个切角的实现方式，想必你也能推断出实现`四个切角效果`的思路了。我们需要`4层渐变`，每层只占整个元素的`4分之一`。下面的例子，我用了4种不同的颜色表示，这样可以更加直观的看出来每层渐变的大小和位置。

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
