+++
keywords = ["inline element spacing bug"]
description = "Inline element spacing bug caused by html code line wrapping"
categories = ["frontend"]
tags = ["bug"]
date = "2017-01-11T21:48:19+08:00"
title = "Inline Bug"
url = "/fix-inline-bug.html"
+++

## 1. inline element:

If the code of inline elements (span, strong, b, em, i, etc.) is wrapped, there will be an undesirable gap between them. By setting `margin:0` or `padding:0`, this gap still exists, indicating that this gap is not margin or padding.


<style type="text/css">
.inline p span:first-child {
        background-color: #66d9ef;
    }
    .inline p span:nth-child(2) {
        background-color: #c191c1;
    }
    .inline p span:nth-child(3) {
        background-color: #9fe89f;
    }
    .inline p span:nth-child(4) {
        background-color: #8787f1;
    }
    .inline p span:last-child{
        background-color: #464141;
    }
    .inline p span{
        font-size:16px;
        color:#fff;
        line-height:30px;
    }
    .inline-block span{
        display: inline-block;
        width:20%;
    }
    .fs0{
        font-size: 0!important;
    }
</style>

<div class="inline ">
    <p>
<span>inline element 1</span>
        <span>inline element 2</span>
        <span>inline element 3</span>
    </p>
</div>

In order not to eliminate this gap, do we have to write the html code of the inline element in one line? The answer is no.
During development, in order to facilitate reading and debugging, we are accustomed to writing the code like this:
```html
    <p>
<span>inline element 1</span>
<span>inline element 2</span>
<span>inline element 3</span>
<span>inline element 4</span>
<span>inline element 5</span>
    </p>
```

Solution: Set the parent element `font-size:0`, and then set `font-size` separately for the child elements to fix the bug.
<div class="inline ">
    <p class="fs0">
<span>inline element 1</span>
        <span>inline element 2</span>
        <span>inline element 3</span>
    </p>
</div>

## 2. inline-block element:
To display multiple juxtaposed elements in one row, in addition to setting float `float:left;float:right`, we can also set `display:inline-block` to convert an inline element or block element into an inline-block element that can set the height and width.

If there are 5 `inline-block` elements, set their width to `20%`. We expect them to be displayed on one line. However, due to the spacing caused by line wrapping of the html code, it cannot be displayed in one line.

<div class="inline ">
    <p class="inline-block">
<span>inline-block element 1</span>
        <span>inline-block element 2</span>
        <span>inline-block element 3</span>
        <span>inline-block element 4</span>
        <span>inline-block element 5</span>
    </p>
</div>

Solution: Set `font-size:0` for the parent element, and then set `font-size` separately for the child elements.

<div class="inline ">
    <p class="inline-block fs0">
<span>inline-block element 1</span>
        <span>inline-block element 2</span>
        <span>inline-block element 3</span>
        <span>inline-block element 4</span>
        <span>inline-block element 5</span>
    </p>
</div>
