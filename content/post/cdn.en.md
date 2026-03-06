+++
keywords = ["Front-end CDN public library","CDN acceleration"]
date = "2016-08-20T21:07:46+08:00"
title = "Cdn"
description = "Recommended several commonly used CDN public libraries, front-end CDN public libraries, CDN acceleration"
categories = ["frontend"]
tags = ["CDN"]
url= "/cdn.html"
+++

## CDN

The full name of CDN is Content Delivery Network, which is content distribution network. It refers to a computer network system that is connected to each other through the Internet. It uses the server closest to each user to send music, pictures, videos, applications and other files to users faster and more reliably to provide high performance, scalability and low-cost network content to users.

## CDN public library

CDN public library refers to placing commonly used js libraries on CDN nodes to facilitate direct calls by developers. Compared with being stored on a single server, the CDN public library is more stable and faster. The general CDN public library will contain all the most popular open source JavaScript libraries in the world and can be directly referenced.

### advantage:

1. Improve access speed:

Assuming that your website's jQuery references Sina's CDN, then when the user's browser submits a request, the browser will automatically download the latest available file on the network, and the download speed will be faster.

2. Better caching:

Many websites use several well-known CDN public libraries at home or abroad. It is very likely that many versions of jQuery have already been downloaded in the cache area of ​​the user's browser. When visiting your website, there is no need to download jQuery again. If you serve jQuery from your own server, your users will have to download it at least once.

## Recommend several commonly used front-end public libraries CDN

### Foreign

1. jQuery: https://code.jquery.com/

2. Google: https://developers.google.com/speed/libraries/

3. CDNJS: https://cdnjs.com/libraries


### Domestic

1. cdnjs: http://cdnjs.net/

2. Baidu: http://developer.baidu.com/wiki/index.php?title=docs/cplat/libs

3. 360: http://libs.useso.com/

4. Also shoot the cloud: http://upcdn.b0.upaiyun.com/

5. Sina: http://lib.sinaapp.com/


### Commonly used jQueryCDN at home and abroad:

1. jQuery official website: http://code.jquery.com/jquery-2.0.0.min.js

2. CDNJS: http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.0/jquery.min.js

3. Google Hosted Libraries: http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js

4. jsDeliver: http://cdn.jsdelivr.net/jquery/2.0.0/jquery-2.0.0.min.js

5. Qiniu: http://cdn.staticfile.org/jquery/2.0.0/jquery.min.js

6. Baidu: http://libs.baidu.com/jquery/2.0.0/jquery.min.js

7. Sina: http://lib.sinaapp.com/js/jquery/2.0/jquery.min.js

8. Also shoot the cloud: http://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.0.min.js

9. 360: http://libs.useso.com/js/jquery/2.0.0/jquery.min.js

Of course, after all, third-party services may not be completely reliable. If you refer to a foreign site, it may be blocked one day. So, we can add the following code, when
When the CDN fails to load, you can also load your own local jQuery file. [Code source link below](https://paulund.co.uk/fallback-on-local-jquery-if-cdn-fails)

	<script>
window.jQuery || document.write('<script src="js/libs/jquery-2.1.0.min.js"></script>');
	</script>
	
