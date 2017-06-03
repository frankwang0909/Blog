+++
images = []
banner = ""
menu = ""
description = "通过navigator.userAgent识别移动设备，跳转移动端站点，userAgent的妙用，userAgent的用途：识别手机、平板设备；userAgent返回字符串的具体含义"
keywords = "userAgent， 移动设备，userAgent的妙用，userAgent的用途"
categories = ["frontend"]
tags = ["userAgent"]
date = "2017-04-04T21:02:50+08:00"
title = "通过userAgent识别移动设备，自动跳转移动端站点"
url = "useragent"
+++

不少互联网公司的网站都分为PC端和手机端。如果用户用手机访问PC站点，受限于手机网络，很可能会出现加载网页缓慢的情况。
因此，如何识别用户访问网站的设备，并且自动跳转到对应的站点呢？

## navigator.userAgent

navigator是JavaScript中的一个独立的对象，用于提供用户所使用的浏览器以及操作系统等信息，以navigator对象属性的形式来提供。所有浏览器都支持该对象。

navigator对象有一个userAgent属性，会返回用户的设备操作系统和浏览器的信息。

1.用`谷歌浏览器`，随便打开一个网页，`F12`打开Chrome调试工具，输入`navigator.userAgent`, 会返回如下的字符串：

	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"

这个字符串可以分成四个主要的部分，我来解释一下各个部分的含义：

	1）Mozilla/5.0 ：表示兼容Mozilla, 几乎所有的浏览器都有这个字符;
	2) (Windows NT 6.1; Win64; x64): 表示设备的操作系统版本，以及CPU信息；
	3）AppleWebKit/537.36 (KHTML, like Gecko)：表示浏览器的内核；
	4) Chrome/57.0.2987.98 Safari/537.36: 表示浏览器的版本号。

2.用`火狐浏览器`，随便打开一个网页，`F12`打开调试工具，同样地在控制台输入`navigator.userAgent`, 返回如下的字符串：

	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0"

与之前的结果区别：

	1)浏览器内核是Gecko内核，
	2)浏览器版本是火狐的Firefox/52.0。从这里我们可以看出火狐浏览器是基于Gecko内核。

3.用`谷歌浏览器`模拟`手机`访问，选择`iPhone6s`，同样在调试工具控制台输入`navigator.userAgent`, 会返回如下的字符串：

	"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"

注意看出现了`iPhone`。

4.用`谷歌浏览器`模拟`平板设备`访问，选择`iPad`，同样在调试工具控制台输入`navigator.userAgent`, 会返回如下的字符串：	

	"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"

注意看出现了`iPad`。

5.用`谷歌浏览器`模拟`安卓设备`，比如选择`Galaxy S5`，同样在调试工具控制台输入`navigator.userAgent`, 会返回如下的字符串：

	"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36"

注意看出现了`Android`。

6.用`谷歌浏览器`模拟`winPhone设备`，比如选择`Microsoft Lumia 950`，同样在调试工具控制台输入`navigator.userAgent`, 会返回如下的字符串：

	"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263"

注意看出现了`Windows Phone`。

通过以上的小测试，我们还可以能够发现一个规律：手机和平板设备访问时，`navigator.userAgent`返回的字符串都会包含`Mobile`。

## userAgent的用途：识别手机、平板设备

刚才我们已经看到了手机和平板设备访问时，`navigator.userAgent`返回的字符串都会包含`Mobile`，可以利用这一点，来实现文章开头提出的需求，自动识别用户访问设备从而跳转对应的站点。

PC端站点可以加上如下代码，自动跳转到移动端站点

    var ua = navigator.userAgent.toLowerCase();
    if (/mobile|android|iphone|ipad|phone/i.test(ua)) {
       window.location.href = "http://m.example.com";
    }

如果在`微信`中打开和在`手机浏览器`打开网页执行的是不同的脚本的话，还可以通过`userAgent`来判断是否是在`微信`中打开的。

	var ua = navigator.userAgent.toLowerCase();
	if(/micromessenger/i.test(ua){
		//to do
	}

本文首发于[Frank Wang的个人博客](http://www.wangxingfeng.com/), 转载时请附上原文链接。