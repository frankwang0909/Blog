+++
categories = ["frontend"]
tags = ["JavaScript"]
title = "Safari Not Support"
keywords = ["iOS system", "Safari browser", "new Date() date conversion", "Event is not compatible"]
description = "The Safari browser on Apple mobile phones is not compatible with the new Date() date conversion format. Safari does not support dates in YYYY-MM-DD format on iOS5 and below, so the date needs to be converted to YYYY/MM/DD format. The Safari browser on Apple mobile phones does not support keydown, keypress, keyup, change and other events in Safari on iOS. Keydown, keypress, keyup, change and other events are invalid. Consider listening to input and propertychange events instead."
date = "2017-06-01T07:35:15+08:00"
url = "/safari-not-support.html"
+++


## 1. The Safari browser of Apple mobile phone is not compatible with the new Date() date conversion format.

When developing web projects, `countdown` is a very common requirement. My need is to make a countdown to the time when concert tickets are on sale.

### The idea is as follows:

Get the `on-sale time` and `current time on the server`, subtract the `current time` from the `on-sale time` to get a time in milliseconds, and then convert it into xx days xx hours xx minutes xx seconds.

After a brief communication with the backend technical guy, the backend will transmit the 'on sale time' and 'current time' to the page and put them in the 'hidden field', so that I can get the time using JavaScript. So easy! Then I started writing code.

At first I wrote like this:

```javascript
function preSellCount(){
    // If the sale time is not set, the performance time will be obtained. The obtained time format is 2017-06-01 10:00
    var preSt = $('#preSellTime').val() || $('#showTime').val();  

    var nowTime = $('#nowTime').val();

    // If there is no on-sale time or performance time set, the countdown will display "On-sale time to be determined"
    if (!preSt) {
        $('# preSellCount').text("On sale time to be determined");
    }else{

        // The obtained sales opening time is a string, first converted into milliseconds,
        var sellTime = new Date(preSt).getTime();

        // Current milliseconds
        var now = new Date(nowTime).getTime();

        var count, d, h, min, sec, timeStr, timer;

        count = now > sellTime ? 0 : Math.floor((sellTime-now)/1000);

        // The timer will only be executed when the time of the incoming page is not zero.
        if(count!==0){
            // timer
            timer = setInterval(function() {
                if (count === 0) {
                    clearInterval(timer);

                    // When the countdown reaches zero, automatically refresh the page
                    window.location.reload();
                }else{
                    
                    // days
                    d = Math.floor(count/86400); 

                    // hours
                    h = Math.floor(count%86400/3600); 

                    // minutes
                    min = Math.floor(count%86400%3600/60); 

                    // seconds
                    sec = Math.floor(count%86400%3600%60);

                    // When it is less than 10, add a ‘0’ in front.
                    if (min < 10) {
                        min = '0' + min;
                    }
                    if (sec < 10 ) {
                        sec = '0' + sec;
                    }

                    if (d == 0) {
timeStr = h + "hour" + min + "minute" + s + "second";
                    }else{
timeStr = d + "day" + h + "hour" + min + "minute" + s + "second";
                    }
                    // Get the countdown time string
timeStr = d + "day" + h + "hour" + min + "minute" + sec + "second";

                    // Display word countdown on page
                    $('#preSellCount').text(timeStr);

                    count -= 1;
                }
            }, 1000);
        }
    }
}

```

Everything is normal when using Chrome to simulate various mobile phone debugging. Publish it to the local test environment and then access it with your Android phone, and everything works fine. Then I tested it with a colleague’s iPhone, and the countdown was not displayed. WTF?

Think about where there might be compatibility issues?

Go through the code from the beginning. There is no problem in getting the sales opening time. The obtained sales opening time is a string date. Use `new Date(preSt).getTime()` to convert it into milliseconds. Is there any problem? Google `new Date() iOS`.
Sure enough, I found that there are many related articles mentioning the date conversion problem under iOS. Since Safari does not support dates in the `YYYY-MM-DD` format on iOS5 and below, the format needs to be converted.

The simplest is to use `regular expression` to convert the date into `YYYY/MM/DD` format.

```javascript

    preSt.replace(/-/g, "/")

```

The final code is this:

```javascript

function preSellCount(){
    // If the sale time is not set, the performance time will be obtained. The obtained time format is 2017-06-01 10:00
    var preSt = $('#preSellTime').val() || $('#showTime').val();  
    var nowTime = $('#nowTime').val();
    // If there is no on-sale time or performance time set, the countdown will display "On-sale time to be determined"
    if (!preSt) {
        $('# preSellCount').text("On sale time to be determined");
    }else{

        // The obtained sales opening time is a string, first converted into milliseconds,
        var sellTime = new Date(preSt.replace(/-/g, "/")).getTime();

        // Current milliseconds
        var now = new Date(nowTime.replace(/-/g, "/")).getTime();

        var count, d, h, min, sec, timeStr, timer;

        count = now > sellTime ? 0 : Math.floor((sellTime-now)/1000);

        // The timer will only be executed when the time of the incoming page is not zero.
        if(count!==0){
            // timer
            timer = setInterval(function() {
                if (count === 0) {
                    clearInterval(timer);

                    // When the countdown reaches zero, automatically refresh the page
                    window.location.reload();
                }else{
                    
                    // days
                    d = Math.floor(count/86400); 

                    // hours
                    h = Math.floor(count%86400/3600); 

                    // minutes
                    min = Math.floor(count%86400%3600/60); 

                    // seconds
                    sec = Math.floor(count%86400%3600%60);

                    // When it is less than 10, add a ‘0’ in front.
                    if (min < 10) {
                        min = '0' + min;
                    }
                    if (sec < 10 ) {
                        sec = '0' + sec;
                    }

                    if (d == 0) {
timeStr = h + "hour" + min + "minute" + s + "second";
                    }else{
timeStr = d + "day" + h + "hour" + min + "minute" + s + "second";
                    }
                    // Get the countdown time string
timeStr = d + "day" + h + "hour" + min + "minute" + sec + "second";

                    // Display word countdown on page
                    $('#preSellCount').text(timeStr);

                    count -= 1;
                }
            }, 1000);
        }
    }
}

```


## 2. The Safari browser on Apple phones does not support keydown, keypress, keyup, change and other events.

Requirement: When entering content in the input box, a clear button is displayed behind the input box. Click to clear all the content in the input box.

```javascript
var keyword = $("#search-keyword");
var clear = $('.clear');

keyword.on('keyup', function(event) {
    if($(this).val().length>0){

        // Displays a small icon for clearing the input box
        clear.show();

    }else{

        // Hide the small icon for clearing the input box
        clear.hide();
    }
});

```

However, in iOS Safari, keydown, keypress, keyup, change and other events are invalid. Consider listening to input and propertychange events instead.

```javascript
var keyword = $("#search-keyword");
var clear = $('.clear');

keyword.on('input propertychange', function(event) {
    if($(this).val().length>0){
        // Displays a small icon for clearing the input box
        clear.show();
    }else{
        // Hide the small icon for clearing the input box
        clear.hide();
    }
});

```
