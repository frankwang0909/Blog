+++
title = "Dropdown Menu"
keywords = ["Common drop-down menus"]
description = "Draw ellipse, half ellipse, quarter ellipse with CSS"
categories = ["frontend"]
tags = ["drop down menu"]
date = "2016-03-03T23:55:37+08:00"
url = "/dropdown-menu.html"
+++

## HTML structure

The navigation bar is a very common component in web pages. Usually, we use unordered lists to make navigation bars. for example

```html
	<div id="nav">
		<ul class="navMenu">
<li><a href="">Home</a></li>
<li><a href="">Group tour</a></li>
<li><a href="">Self-guided tour</a></li>
<li><a href="">Cruise</a></li>
<li><a href="">Self-driving</a></li>
		</ul>
	</div>
```

Some navigation bars have drop-down secondary menus, so we add a list at the corresponding position to form a secondary menu, such as

```html
	<div id="nav">
		<ul class="navMenu">
<li><a href="">Home</a></li>
<li><a href="">Group tour</a>
				<ul class="subMenu">
<li><a href="">Outbound tour group</a></li>
<li><a href="">Domestic tour group</a></li>
<li><a href="">Peripheral tours</a></li>
<li><a href="">Local tour</a></li>
				</ul>
			</li>
<li><a href="">Self-guided tour</a>
				<ul class="subMenu" >
<li><a href="">Outbound self-service</a></li>
<li><a href="">Domestic self-service</a></li>
<li><a href="">Flight + Hotel</a></li>
<li><a href="">Train + Hotel</a></li>
				</ul>
			</li>
<li><a href="">Cruise</a>
				<ul class="subMenu">
<li><a href="">Exclusive charter boat</a></li>
<li><a href="">Japan and South Korea routes</a></li>
<li><a href="">European routes</a></li>
<li><a href="">Three Gorges Route</a></li>
<li><a href="">American routes</a></li>
				</ul>
			</li>
<li><a href="">Self-driving</a>
				<ul class="subMenu">
<li><a href="">Self-driving around the area</a></li>
<li><a href="">Domestic self-driving</a></li>
<li><a href="">Outbound self-driving</a></li>
				</ul>
			</li>
		</ul>
	</div>
```

## Basic CSS styles

The list is arranged vertically by default, while the common navigation bar main menu is arranged horizontally, and the secondary drop-down menu is arranged vertically, so we need to float the li element of the main menu so that it can be arranged horizontally. After setting the float, you should remember to clear it. You can use class as a common float and clear-float style, then add the corresponding class to the element that needs to be floated, and add the clear-float class to the parent element of the floated element.

**CSS code**
```css
	/*reset*/
	body, div, ul,li, a{padding: 0; margin:0;}
	ul{list-style: none; }
/*Floating and clearing floats*/
	.fl{float: left; }
	.clearfix:after{content:"";display:block;clear:both;}
	.clearfix{zoom:1;} 
/*Navigation bar*/
	#nav{width: 600px; height: 40px; margin:0 auto; background-color: #eee; }
	.navMenu li{ text-align: center; line-height: 40px; position: relative;}
	.navMenu li a{text-decoration: none;color:#000; padding: 0 20px; display: block; width:80px; }
.subMenu{position: absolute; top: 40px; left: 0;display: none;}/*Hide the secondary menu by default*/
	.subMenu li{float:none; background-color:#eee; margin-left: 2px; }
```


**HTML code** changes to the following:

```html
	<body>
		<div id="nav">
			<ul class="navMenu clearfix">
<li class="fl"><a href="">Home</a></li>
<li class="fl"><a href="">Group tour</a>
					<ul class="subMenu">
<li><a href="">Outbound tour group</a></li>
<li><a href="">Domestic tour group</a></li>
<li><a href="">Peripheral tours</a></li>
<li><a href="">Local tour</a></li>
					</ul>
				</li>
<li class="fl"><a href="">Self-guided tour</a>
					<ul class="subMenu" >
<li><a href="">Outbound self-service</a></li>
<li><a href="">Domestic self-service</a></li>
<li><a href="">Flight + Hotel</a></li>
<li><a href="">Train + Hotel</a></li>
					</ul>
				</li>
<li class="fl"><a href="">Cruise</a>
					<ul class="subMenu">
<li><a href="">Exclusive charter boat</a></li>
<li><a href="">Japan and South Korea routes</a></li>
<li><a href="">European routes</a></li>
<li><a href="">Three Gorges Route</a></li>
<li><a href="">American routes</a></li>
					</ul>
				</li>
<li class="fl"><a href="">Self-driving</a>
					<ul class="subMenu">
<li><a href="">Self-driving around the area</a></li>
<li><a href="">Domestic self-driving</a></li>
<li><a href="">Outbound self-driving</a></li>
					</ul>
				</li>
			</ul>
		</div>
	<body>
```

## Implementation of drop-down menu effect

How to implement that when the mouse moves to the corresponding li element position of the main menu, the secondary menu is displayed, and when the mouse is removed, the secondary menu is hidden. Basic implementation methods: `Pure CSS style`, `jQuery`, `Native JavaScript` and other three implementation methods.

### Method 1, pure CSS style: [see demo1](http://frankwang0909.github.io/posts/demo1.html)

The simplest way is to directly use css `:hover` to achieve this.

When the mouse moves over the corresponding li of the main menu, the secondary menu is set to the visible block-level element `display: block;`
```csss
	.navMenu li:hover .subMenu{
		display: block;
	}
/* Display the secondary menu when hovering */
```

### Method 2, jQuery: [see demo2](http://frankwang0909.github.io/posts/demo2.html)

Use `jQuery` to get the li element, bind the `mouseover` and `mouseout` events, and call the `show()` and `hide()` methods of `jQuery`. The reference code is as follows:
```html
	<script src="js/jquery-2.2.3.min.js"></script>
	<script type="text/javascript">
		$(function() {
			$('.navMenu>li').mouseover( function() {
				$(this).children('ul').show();
			});
				$('.navMenu>li').mouseout( function() {
				$(this).children('ul').hide();
			});
		});
	</script>
````

### Method three, native JavaScript: [See demo3](http://frankwang0909.github.io/posts/demo3.html)

First define functions to show and hide elements

```javascript
	// Define display function
	function showsubmenu(li) {
		var submenu = li.getElementsByClassName('subMenu')[0];
		submenu.style.display="block";
	}
	// Define hidden functions
	function hidesubmenu(li){
		var submenu = li.getElementsByClassName('subMenu')[0];
		submenu.style.display="none";
	}
```

Then call the function, add the function call to the corresponding li element in the HTML code, and modify the code as follows.
```html
	<div id="nav">
		<ul class="navMenu clearfix">
<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">Home</a></li>
<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">Group tour</a>
				<ul class="subMenu">
<li><a href="">Outbound tour group</a></li>
<li><a href="">Domestic tour group</a></li>
<li><a href="">Peripheral tours</a></li>
<li><a href="">Local tour</a></li>
				</ul>
			</li>
<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">Self-guided tour</a>
				<ul class="subMenu" >
<li><a href="">Outbound self-service</a></li>
<li><a href="">Domestic self-service</a></li>
<li><a href="">Flight + Hotel</a></li>
<li><a href="">Train + Hotel</a></li>
				</ul>
			</li>
<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">Cruise ship</a>
				<ul class="subMenu">
<li><a href="">Exclusive charter boat</a></li>
<li><a href="">Japan and South Korea routes</a></li>
<li><a href="">European routes</a></li>
<li><a href="">Three Gorges Route</a></li>
<li><a href="">American routes</a></li>
				</ul>
			</li>
<li class="fl" onmouseover="showsubmenu(this)" onmouseout="hidesubmenu(this)"><a href="">Self-driving</a>
				<ul class="subMenu">
<li><a href="">Self-driving around the area</a></li>
<li><a href="">Domestic self-driving</a></li>
<li><a href="">Outbound self-driving</a></li>
				</ul>
			</li>
		</ul>
	</div>
```
