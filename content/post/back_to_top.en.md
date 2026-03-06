+++
keywords = ["Back to top"]
description = "3 ways to achieve the return to top effect"
categories = ["frontend"]
tags = ["Back to top"]
date = "2016-04-22T22:56:30+08:00"
title = "Back To Top"
url = "/back-to-top.html"
+++


Today's web pages contain a lot of content, and it is basically impossible to display them all on one screen. At this time, the user needs to move the scroll bar (slide the mouse wheel) to view the entire content. If he wants to return to the top, he also needs to move the scroll bar. If the page is too long, the experience is obviously not good enough. Therefore, the `Back to Top` button came into being.

There are mainly three ways to implement returning to the top.

## Implementation method one: Set anchor link

The simplest and fastest way is to set an anchor link `<a href="#">`. `Jingdong` uses this method.

Advantages: Simple and fast, no browser compatibility issues.

The reference code is as follows:

HTML code

		<div id="go-top">
<a href="#" id="gotop-btn"></a><!-- Use anchor links directly to return to the top -->
		</div>


## Implementation method two: Use jQuery to achieve

The reference code is as follows:

HTML code

	<div id="go-top">
<a href="javascript:;" id="gotop-btn"></a>
	</div>

JavaScript code

	<script type="text/javascript">
$(function() {
			$(window).scroll(function(){
				// When the scroll bar is more than 100 pixels from the top, the back to top button appears, otherwise it disappears
		if ($(window).scrollTop()>=100){
			$("#gotop-btn").fadeIn(500);
		}
		else{
			$("#gotop-btn").fadeOut(500);
		}
		});
		//When clicking the jump link, return to the top of the page
		$("#gotop-btn").click(function(){
			$('body,html').animate({scrollTop:0},300);
		});
	});
	</script>


## Implementation method three: dynamic operation through native JavaScript.

The following knowledge is required

### DOM operations:

1. Get elements based on ID: `document.getElementById`

2. The value of the scroll bar, which can be read and written: `document.documentElment.scrollTop`

### Event application:

1. Trigger `window.onload` after the page is loaded.

2. Trigger `onclick` after clicking

3. Trigger `window.onscroll` when the scroll bar scrolls


### Timer:

1. `setInterval()`: To set the timer, two parameters need to be passed.

2. `clearInterval()`: To turn off the timer, two parameters need to be passed.

Reference code:

HTML code
	<div id="go-top">
<a href="javascript:;" id="gotop-btn"></a>
	</div>

js code
	<script  type="text/javascript" >
//Trigger event after loading
		window.onload = function() {
			var obtn = document.getElementById('gotop-btn');
			// Get the height of the visible area of the page
			var clientHeight = document.documentElement.clientHeight;
			var timer = null;
			var isTop = true;
			// Trigger the event when the scroll bar scrolls, clear the timer, and stop at the current position.
			window.onscroll = function() {
				// Get the value of the scroll bar from the top
				var osTop = document.documentElement.scrollTop || document.body.scrollTop;

if(osTop >= clientHeight){
					//Show return button
					obtn.style.display = "block";
				}
				else{
					//Hide the back button
					obtn.style.display = "none";
				}
				if(!isTop){
					clearInterval(timer);
				}
				isTop = false;
			}
			obtn.onclick = function() {
				//Set timer
				timer = setInterval(function() {
					var osTop = document.documentElement.scrollTop || document.body.scrollTop;
					// Chrome uses document.body.scrollTop to get the distance from the scroll bar to the top.
					// The scroll bar scrolls from fast to slow, that is, the reduced distance is from large to small.
					var ispeed = Math.floor(-osTop /6);
					// Math.floor() rounds down. If ispeed is rounded to a positive number, osTop will not be equal to 0 in the end, so the timer cannot be eliminated.
					document.documentElement.scrollTop = document.body.scrollTop = osTop + ispeed;
					//After the scroll bar reaches the top, clear the timer, otherwise it will keep returning to the top and cannot pull down the scroll bar to see the web content below.
					isTop = true;
					// console.log(osTop-ispeed);
					if(osTop == 0){
						clearInterval(timer);
					}
				},50)
			}
		}
	</script>
