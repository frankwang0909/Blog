+++
images = []
banner = ""
menu = ""
date = "2016-08-20T21:07:46+08:00"
title = "推荐几个常用的CDN公共库"
description = "推荐几个常用的CDN公共库,前端CDN公共库，CDN加速"
categories = ["frontend"]
tags = ["CDN公共库"]
url= "cdn"
+++

## CDN

CDN的全称是Content Delivery Network，即内容分发网络。是指一种通过互联网互相连接的电脑网络系统，利用最靠近每位用户的服务器，更快、更可靠地将音乐、图片、视频、应用程序及其他文件发送给用户，来提供高性能、可扩展性及低成本的网络内容传递给用户。

## CDN公共库

CDN公共库指将常用的js库存放在CDN节点，以方便广大开发者直接调用。与存放在服务器单机上相比，CDN公共库更加稳定、高速。一般的CDN公共库都会包含全球所有最流行的开源JavaScript库，可以直接引用。

### 优点：

1.提高访问速度：

假设你网站的jQuery引用了新浪的CDN，那么当用户的浏览器提交请求时，浏览器自动下载网络上最近的可用的文件，下载速度会更快。

2.更好的缓存:

许多网站都使用了国内或者是国外的几个知名的CDN公共库。很可能用户浏览器的缓存区里早就已经下载了许多版本的jQuery，访问你的网站时，不需要重复下载jQuery。如果你用自己的服务器提供jQuery，那么你的用户至少要下载一次它。

## 推荐几个常用前端公共库CDN

### 国外的

1.jQuery: https://code.jquery.com/

2.Google: https://developers.google.com/speed/libraries/

3.CDNJS: https://cdnjs.com/libraries


### 国内的

1.cdnjs: http://cdnjs.net/

2.百度：http://developer.baidu.com/wiki/index.php?title=docs/cplat/libs

3.360：http://libs.useso.com/

4.又拍云：http://upcdn.b0.upaiyun.com/

5.新浪：http://lib.sinaapp.com/


### 国内外常用的jQueryCDN：

1.jQuery官网： http://code.jquery.com/jquery-2.0.0.min.js

2.CDNJS： http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.0/jquery.min.js

3.Google Hosted Libraries： http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js

4.jsDeliver： http://cdn.jsdelivr.net/jquery/2.0.0/jquery-2.0.0.min.js

5.七牛: http://cdn.staticfile.org/jquery/2.0.0/jquery.min.js

6.百度: http://libs.baidu.com/jquery/2.0.0/jquery.min.js

7.新浪: http://lib.sinaapp.com/js/jquery/2.0/jquery.min.js

8.又拍云: http://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.0.min.js

9.360: http://libs.useso.com/js/jquery/2.0.0/jquery.min.js

当然，毕竟第三方的服务也不一定完全靠谱，如果引用的是国外的站点的话，哪天被墙了也有可能。所以，我们可以加入以下代码，当
CDN加载失败时，还可以加载自己本地的jQuery文件。[以下代码来源链接](https://paulund.co.uk/fallback-on-local-jquery-if-cdn-fails)

	<script>
		window.jQuery || document.write('<script src="js/libs/jquery-2.1.0.min.js"></script>');
	</script>
	
