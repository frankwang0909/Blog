+++
menu = ""
date = "2016-08-01T21:49:40+08:00"
title = "前端工程师应该具备的SEO基础知识"
description = "前端工程师应该具备的SEO基础知识, SEO新手指南"
keywords = ["SEO基础知识", "SEO新手指南"]
categories = ["frontend"]
tags = ["seo"]
url = "/seo.html"
+++

## SEO 是什么？

SEO 是“Search Engine Optimization”（搜索引擎优化）或“Search Engine Optimizer”（搜索引擎优化服务商）的首字母缩略词。通俗地说，SEO就是通过对网站内部调整优化及站外优化，使网站满足搜索引擎收录排名需求，在搜索引擎中提高关键词排名，从而把精准用户带到网站，获得免费流量，产生直接销售或品牌推广。

新手入门可以阅读[Google 搜索引擎优化 (SEO) 单页指南.pdf](https://support.google.com/webmasters/answer/35291?hl=zh-Hans). 

如果想要进一步学习，可以参考[Google搜索引擎优化入门指南](http://static.googleusercontent.com/media/www.google.com/en/us/intl/zh-cn/webmasters/docs/search-engine-optimization-starter-guide-zh-cn.pdf) （需翻墙），[如果翻不了，可以点击这里](http://www.wangxingfeng.com/posts/search-engine-optimization-starter-guide-zh-cn.pdf)。

## 前端工程师应该掌握的SEO知识

目前不少公司设有SEO的专职岗位，而前端工程师不是专业做SEO优化推广的，并不需要变成SEO专家，但应掌握以下SEO基础知识。

###  一、结构布局的优化

1.结构扁平化。

网站的层次结构尽量不超过三层。这样搜索引擎或者用户点击跳转3次可以到达网站内任何一个内页。

2.优化导航。

设置页面的主导航、副导航、分类导航、面包屑导航、分页页码等，方便用户跳转到想访问的页面。


###  二、标签的语义化

搜索引擎的爬虫会依赖于标记来确定上下文和各个关键字的权重.因此，正确使用语义化的标签有利于搜索引擎抓取和收录网页内容。

1.锚链接 `<a>` 标签：

1）添加属性 **title="链接的文字说明"**，增加对该链接的说明，尤其是指向本站的链接。 

2）添加属性 **rel="no follow"**。 对于指向非本站的链接，增加这个属性是告诉爬虫该页面无需追踪。

2.正文标题用`<h1>`,副标题用`<h2>`, 不要滥用标题。

3.正文内容用`<p>`，正文内的换行用`<br>`， 其他地方不要滥用`<br>`来换行，而是通过CSS样式来设置。

4.图片`<img> `添加属性 **alt="图片的文字注释"**.

5.表格用`<table>` ，表格的标题使用 `<caption>`

6.有序列表用`<ol>`， 无序列表用`<ul>`， 定义列表用`< dl>`、

7.强调标签： `<strong>` 表示强调， 可以用于突出关键词，有较大的权重。`<em> `也表示强调，权重比strong稍低。`<b>`标签虽然也有加粗效果，但没有强调的作用，因此不会增加标签内的文本权重。

8.减少`<iframe>`的使用。iframes 阻塞页面加载, 延迟触发window.onload事件，给用户的感觉就是这个网页非常慢。

9.重要内容HTML代码放在最前面，然后通过CSS属性控制位置。
