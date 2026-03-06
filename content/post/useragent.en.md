+++
description = "Identify mobile devices through navigator.userAgent and jump to mobile sites. The wonderful use of userAgent. The purpose of userAgent: identify mobile phones and tablet devices; the specific meaning of the string returned by userAgent"
keywords = ["userAgent", "mobile device", "Purpose of userAgent"]
categories = ["frontend"]
tags = ["userAgent"]
date = "2017-04-04T21:02:50+08:00"
title = "Useragent"
url = "/useragent.html"
+++

The websites of many Internet companies are divided into PC and mobile terminals. If a user uses a mobile phone to access a PC site, the web page may be loaded slowly due to the limitations of the mobile phone network.
Therefore, how to identify the device used by users to access the website and automatically jump to the corresponding site?

## navigator.userAgent

Navigator is an independent object in JavaScript, used to provide information such as the browser and operating system used by the user, in the form of navigator object attributes. This object is supported by all browsers.

The navigator object has a userAgent attribute that returns information about the user's device operating system and browser.

1. Use `Google Chrome` to open a web page, `F12` to open the Chrome debugging tool, enter `navigator.userAgent`, the following string will be returned:

"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"

This string can be divided into four main parts. Let me explain the meaning of each part:

1) Mozilla/5.0: Indicates compatibility with Mozilla, almost all browsers have this character;
	2) (Windows NT 6.1; Win64; x64): Indicates the operating system version of the device and CPU information;
	3) AppleWebKit/537.36 (KHTML, like Gecko): represents the browser’s core;
	4) Chrome/57.0.2987.98 Safari/537.36: Indicates the browser version number.

2. Use `Firefox` to open a web page, `F12` to open the debugging tool, and similarly enter `navigator.userAgent` in the console to return the following string:

"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0"

Differences from previous results:

1) The browser kernel is Gecko kernel,
	2) The browser version is Firefox/52.0. From here we can see that Firefox is based on the Gecko kernel.

3. Use `Google Chrome` to simulate `mobile phone` access, select `iPhone6s`, and also enter `navigator.userAgent` in the debugging tool console, the following string will be returned:

"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"

Notice that `iPhone` appears.

4. Use `Google Chrome` to simulate `tablet device` access, select `iPad`, and also enter `navigator.userAgent` in the debugging tool console, the following string will be returned:

"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"

Notice that `iPad` appears.

5. Use `Google Chrome` to simulate an `Android device`, for example, select `Galaxy S5`, and also enter `navigator.userAgent` in the debugging tool console, the following string will be returned:

"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36"

Notice that `Android` appears.

6. Use `Google Chrome` to simulate `winPhone device`, for example, select `Microsoft Lumia 950`, and also enter `navigator.userAgent` in the debugging tool console, the following string will be returned:

"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263"

Notice that `Windows Phone` appears.

Through the above small test, we can also find a rule: when accessed by mobile phones and tablet devices, the string returned by `navigator.userAgent` will contain `Mobile`.

##Use of userAgent: Identify mobile phones and tablet devices

We have just seen that when accessed by mobile phones and tablet devices, the string returned by `navigator.userAgent` will contain `Mobile`. This can be used to achieve the requirements raised at the beginning of the article, automatically identify the user's access device and jump to the corresponding site.

The PC site can add the following code to automatically jump to the mobile site
```javascript
    var ua = navigator.userAgent.toLowerCase();
    if (/mobile|android|iphone|ipad|phone/i.test(ua)) {
       window.location.href = "http://m.example.com";
    }
```

If the webpage opened in `WeChat` and the webpage opened in `mobile browser` execute different scripts, you can also use `userAgent` to determine whether it was opened in `WeChat`.
```javascript
	var ua = navigator.userAgent.toLowerCase();
	if(/micromessenger/i.test(ua){
		//to do
	}
```
