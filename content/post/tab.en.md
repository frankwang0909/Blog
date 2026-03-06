+++
categories = ["frontend"]
tags = ["tab switching"]
description = "Several ways to implement Tab switching"
keywords = ["Tab switch"]
date = "2016-05-08T23:36:44+08:00"
title = "Tab"
url = "/tab.html"
+++

Tab switching is a common component in web pages. Used appropriately, you can save page space and display more content on the same page. The effects of tab switching vary widely. You only need to learn the basic ideas to create various effects. Below I use native js and jQuery to achieve four different tab switching effects.

## Method 1: Use native js to achieve various tab switching effects.

### 1. Mouse sliding switch:

This is the simplest tab switch. When the mouse rolls over, switch Tab.

First, obtain the corresponding elements through getElementById, getElementsByTagNameL and other methods.

Then, bind the mouseover event to the corresponding element.

For the specific code, see [js-mouseover-tab.html](https://github.com/frankwang0909/Tab/blob/master/js-mouseover-tab.html)

[DEMO](http://frankwang0909.github.io/posts/demo/js-mouseover-tab.html)

### 2. Mouse click to switch

The difference from the first one is that the bound events are different. The method of obtaining elements is the same, just change the binding mouseovers event to click event.

For the specific code, see [js-click-tab.html](https://github.com/frankwang0909/Tab/blob/master/js-click-tab.html)

[DEMO](http://frankwang0909.github.io/posts/demo/js-click-tab.html)

### 3. Mouse sliding delay switching

Delay switching involves a time issue, and the delay effect can be achieved by setting a timer. Timers can be set in two ways: setTimeout() and setInterval().

The setTimeout() method is used to call a function or calculated expression after a specified number of milliseconds. setTimeout() only executes code once. If you want to call it multiple times, you need to use setInterval().

The setInterval() method calls a function or evaluates an expression at a specified period in milliseconds. The setInterval() method will continue to call the function until clearInterval() is called or the window is closed. The ID value returned by setInterval() can be used as an argument to the clearInterval() method.

Because the delayed switching here is to achieve the switching effect after the specified delay time, setTimeout() is used.

For the specific code, see [js-delay-tab.html](https://github.com/frankwang0909/Tab/blob/master/js-delay-tab.html)

[DEMO](http://frankwang0909.github.io/posts/demo/js-delay-tab.html)

### 4. Automatic switching
Automatic switching means automatically switching to the next Tab according to the specified period. A timer is also needed here, and the function is called periodically, so the setInterval() method is used to implement it.
When the mouse slides to a tab, the current page is highlighted and automatic switching is stopped. At this time, the clearInterval() method needs to be used to clear the timer.

For the specific code, see [js-auto-tab-01.html](https://github.com/frankwang0909/Tab/blob/master/js-auto-tab-01.html)

The optimized code can be found at [js-auto-tab-02.html](https://github.com/frankwang0909/Tab/blob/master/js-auto-tab-02.html)

[DEMO](http://frankwang0909.github.io/posts/demo/js-auto-tab-02.html)

## Method 2: Use jQuery to achieve various tab switching effects: The implementation idea is the same as native JavaScript, except that jQuery encapsulates some methods to make it easier to operate DOM elements.

### 1. Mouse sliding switch

For the specific code, see [jQ-mouseover-tab.html](https://github.com/frankwang0909/Tab/blob/master/jQ-mouseover-tab.html)

[DEMO](http://frankwang0909.github.io/posts/demo/jQ-mouseover-tab.html)

### 2. Mouse click to switch

For the specific code, see [jQ-click-tab.html](https://github.com/frankwang0909/Tab/blob/master/jQ-click-tab.html)

[DEMO](http://frankwang0909.github.io/posts/demo/jQ-click-tab.html)

### 3. Mouse sliding delay switching

For the specific code, see [jQ-delay-tab.html](https://github.com/frankwang0909/Tab/blob/master/jQ-delay-tab.html)

[DEMO](http://frankwang0909.github.io/posts/demo/jQ-delay-tab.html)

### 4. Automatic switching

For the specific code, see [jQ-auto-tab-01.html](https://github.com/frankwang0909/Tab/blob/master/jQ-auto-tab-01.html)

The optimized code is shown in [jQ-auto-tab-02.html](https://github.com/frankwang0909/Tab/blob/master/jQ-auto-tab-02.html)

[DEMO](http://frankwang0909.github.io/posts/demo/jQ-auto-tab-02.html)
