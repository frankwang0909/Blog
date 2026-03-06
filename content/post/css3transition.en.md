+++
title = "Css3transition"
keywords = ["CSS3 animation effects", "CSS3 transition", "transition effect"]
description = "CSS3 animation effect, CSS3 transition, transition can replace JavaScript code to achieve animation effects"
categories = ["frontend"]
tags = ["CSS3"]
date = "2016-07-11T21:03:27+08:00"
url = "/css3_transition.html"
+++

## Function

It is used to define the transition effect of style changes. In some cases (mobile terminal), it can replace JavaScript code to achieve animation effects.

The `transition` attribute is a shorthand attribute used to set four transition attributes:

### 1. transition-property

Specifies the name of the CSS property for setting the transition effect. The default value is `all`, which means all properties. You can also set a CSS property individually.


### 2. transition-duration

Transition time, value in seconds or milliseconds.

### 3. transition-timing-function

The velocity curve of the transition effect. This property allows the transition effect to change its speed over time.

The default value is `linear`. Common values ​​include:

linear uniform speed
    ease starts slowly, then gets faster, then ends slowly.
    ease-in starts at a slow speed
    ease-out ends at slow speed
    ease-in-out transition effect that starts and ends at a slow speed

### 4. transition-delay

The delay of the transition effect, in seconds or milliseconds. Default is 0. If it is a positive value, it means delaying the execution of the transition effect; if it is a negative value (such as -0.1s), the transition effect will be executed from the initial state when the transition effect is executed for 0.1s.

## compatibility

Modern browsers such as Internet Explorer 10, Firefox, Opera, and Chrome support the transition attribute.
Safari supports an alternative -webkit-transition attribute.

## Example
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

<a class="trans">Transition effects</a>
