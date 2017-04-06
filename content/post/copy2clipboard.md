+++
images = []
banner = "/images/20170405banner.jpg"
menu = ""
description = "不用Flash实现剪贴板功能，纯JavaScript实现复制内容到剪切板的功能，Clipboard.js轻量集的JavaScript库"
categories = ["frontend"]
tags = ["Clipboard"]
date = "2017-04-05T20:29:51+08:00"
title = "JavaScript实现复制内容到剪贴板的功能"
url = "copy2clipboard"
+++


## 1.ZeroClipboard.js

点击按钮实现复制链接或者一段文本到剪贴板，这个小功能想必不少人都见过。GitHub上就有这么一个点击按钮复制仓库地址的功能。如下图所示：

![](/images/2017040501.jpg)

`Github`用的是[ZeroClipboard](http://zeroclipboard.org/)来实现这一功能。这个库是用一个不可见的Flash来完成剪贴操作的。即将 Flash 做成透明的，以便于我们放在诸如链接、按钮等需要放置的任何地方。这样，用户界面看起来没有变化，当点击链接或按钮时，实际上点击是却是 Flash，从而实现复制操作。具体实现方法，可以参考官方文档http://zeroclipboard.org。

我们知道`Flash`正走向没落，不少功能被越来越强大的`HTML5`所替代。而且，出于安全方面的考虑，不少浏览器都默认禁用了Flash。那么有没有不是Flash的实现方式呢？


## 2.clipboard.js

[clipboard.js](https://clipboardjs.com/)是个更加轻量的JavaScript库，没有使用Flash，而是依赖于[Selection](https://developer.mozilla.org/en-US/docs/Web/API/Selection)和[execCommand](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand)这两个API，并且使用了HTML5的特性，比如自定义数据的`data-* 属性`。因此，clipboard.js在兼容性方面比ZeroClipboard.js差，但现代浏览器(IE9+)基本能够兼容。

使用方法非常简单：

1)[下载代码](https://github.com/zenorocha/clipboard.js/archive/master.zip)，并引入到文件中。

	<script src="dist/clipboard.min.js"></script>

2)实例化一个Clipboard对象，参数可以是`CSS选择器`、`HTML节点`、NodeList对象

参数为`CSS选择器`：

	new Clipboard('.btn'); // btn为DOM元素的class名, 跟jQuery的用法一样。

参数为`HTML节点`：

	var btn = document.getElementById('btn');
    var clipboard = new Clipboard(btn);

参数为`NodeList对象`：

	var btns = document.querySelectorAll('button');
    var clipboard = new Clipboard(btns);

3)实例化对象的时候，可以同时设置复制的内容：

	var clipboard = new Clipboard('.btn', {
        text: function() {
            return 'to be or not to be'; //剪贴板上的文本
        }
    });

4)也可以通过data-*属性来设置要复制的内容

	<!-- Target -->
	<input id="foo" value="https://github.com/zenorocha/clipboard.js.git">

	<!-- Trigger -->
	<button class="btn" data-clipboard-target="#foo">点击复制</button>

	<script>
	    var clipboard = new Clipboard('.btn');
	</script>

点击一下，看看是否成功复制到剪贴板：

<input id="foo" value="https://github.com/zenorocha/clipboard.js.git" style="width:300px;">
<button class="btn" data-clipboard-target="#foo">点击复制</button>
<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.6.0/clipboard.min.js"></script>

<script type="text/javascript" >
    var clipboard = new Clipboard('.btn');
</script>

`data-clipboard-target`属性的值`#foo`对应的是目标节点的CSS选择器。

5）更多的配置信息和使用方法，请查阅[clipboard.js官网](https://clipboardjs.com/)，有兴趣的朋友，应该看看它的源码。


注意我说的看源码，指的是`src目录`的代码。

![](/images/2017040502.jpg)

![](/images/2017040505.jpg)

代码是长这样的。没错，这是ES6的写法。

![](/images/2017040504.jpg)

千万不要去看`dist`下的`clipboard.js` ，那个是编译之后的代码。

![](/images/2017040503.jpg)

