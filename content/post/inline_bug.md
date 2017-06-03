+++
keywords = "inline元素间距bug"
description = "htlm代码换行导致的inline元素间距bug"
categories = ["frontend"]
tags = ["bug"]
date = "2017-01-11T21:48:19+08:00"
title = "代码换行导致的inline元素间距bug"
url = "fix-inline-bug"
+++

## inline 元素：

如果inline元素(span, strong, b, em, i等)代码换行，它们之间会产生我们不希望的间隔。通过设置`margin:0`或者`padding:0` , 这个都间隔仍然存在，说明这个间隔并不是margin或者padding。


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
        font-size: 0;
    }
</style>

<div class="inline ">
    <p>
        <span>inline元素 1</span>
        <span>inline元素 2</span>
        <span>inline元素 3</span>
    </p>
</div>

是否为了不消除这个间隔，就必须把inline元素的html代码写在一行内呢？答案是否定的。
开发的时候，为了方便阅读和调试，我们习惯于把代码写成这样：

    <p>
        <span>inline元素 1</span>
        <span>inline元素 2</span>
        <span>inline元素 3</span>
        <span>inline元素 4</span>
        <span>inline元素 5</span>
    </p>

解决方法：设置父元素`font-size:0`，再给子元素单独设置`font-size`，修复bug。
<div class="inline ">
    <p class="fs0">
        <span>inline元素 1</span>
        <span>inline元素 2</span>
        <span>inline元素 3</span>
    </p>
</div>

## inline-block 元素：
要在一行展示多个并列的元素，除了通过设置浮动`float:left;float:right`，我们还可以通过设置`display:inline-block` 把inline元素或block元素，转换成一个可以设置高度和宽度的inline-block元素。

如果有5个`inline-block`元素，设置它们的宽度为`20%`。我们期望它们是在一行展示的。但是因为html代码换行产生了间距，导致无法在一行内显示。
<div class="inline ">
    <p class="inline-block">
        <span>inline-block元素 1</span>
        <span>inline-block元素 2</span>
        <span>inline-block元素 3</span>
        <span>inline-block元素 4</span>
        <span>inline-block元素 5</span>
    </p>
</div>
解决方法: 设置父元素`font-size:0`，再给子元素单独设置`font-size`。
<div class="inline ">
    <p class="inline-block fs0">
        <span>inline-block元素 1</span>
        <span>inline-block元素 2</span>
        <span>inline-block元素 3</span>
        <span>inline-block元素 4</span>
        <span>inline-block元素 5</span>
    </p>
</div>
