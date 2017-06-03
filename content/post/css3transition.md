+++
title = " CSS3 动画效果"
keywords = ["CSS3 动画效果", "CSS3 transition", "过渡效果"]
description = "CSS3 动画效果, CSS3 transition, transition可以代替JavaScript代码来实现动画效果"
categories = ["frontend"]
tags = ["CSS3"]
menu = ""
date = "2016-07-11T21:03:27+08:00"

+++

## 作用

用来定义样式变化的过渡效果, 在某些情况下（移动端），可以代替JavaScript代码来实现动画效果。

`transition`属性是一个简写属性，用于设置四个过渡属性：

### 1. transition-property

规定设置过渡效果的 CSS 属性的名称, 默认值为`all`, 表示所有属性，也可以单独设置某个css属性。


### 2. transition-duration

过渡时间，值以秒或毫秒计。

### 3. transition-timing-function 

过渡效果的速度曲线。该属性允许过渡效果随着时间来改变其速度。

默认值为`linear`。常见的有以下值：

    linear  匀速
    ease    慢速开始，然后变快，然后慢速结束。
    ease-in 以慢速开始
    ease-out    以慢速结束
    ease-in-out 以慢速开始和结束的过渡效果

### 4. transition-delay

过渡效果的延迟，值以秒或毫秒计。默认为0。如果为正值，则表示延迟执行过渡效果；如果为负值（如-0.1s)，则会从过渡效果的执行0.1s的状态为初始状态开始执行过渡效果。

## 兼容性

Internet Explorer 10、Firefox、Opera 和 Chrome等现代浏览器 支持 transition 属性。
Safari 支持替代的 -webkit-transition 属性。

## 示例
<style>
 .trans {
    display:block;
    width:100px;
    height:30px;
    background:#0ff;
    transition:width 2s ease;
 }
 .trans:hover{
    width:500px;
 }
</style>

<a class="trans">过渡效果</a>


