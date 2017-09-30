+++

categories = ["tools"]
tags = ["Gitment"]
date = "2017-06-24T17:04:42+08:00"
title = "一个Geek的评论系统Gitment"
keywords = "Gitment, 博客评论系统, GitHub Issues"
description = "Gitment是一个使用GitHub Issues 搭建的评论系统。本文教你如何使用Gitment作为自己博客的评论系统"
url = "/use_gitment_as_comment_system_for_your_blog.html"

+++

[Gitment](https://github.com/imsun/gitment)是一个使用GitHub Issues 搭建的评论系统。本文教你如何使用Gitment作为自己博客的评论系统。

## 先简单介绍下优缺点：

### 1.优点：

Gitment支持在前端直接引入，不需要任何后端代码，可以在页面进行登录、查看、评论、点赞等操作，同时有完整的 Markdown / GFM 和代码高亮支持，尤为适合各种基于 GitHub Pages 的静态博客或项目页面。

### 2.缺点：

只能使用 GitHub 账号进行评论。每篇文章需要自己手动用GitHub账号登录并初始化，其他用户才能评论。



## 使用方法：

### 第一步: 注册 OAuth Application

在 GitHub 上注册一个新的 [OAuth Application](https://github.com/settings/applications/new)。前面3项内容都可以随意填写，但要确保最后一个 `Authorization callback URL` 是你的网站域名(比如http://www.wangxingfeng.com)。

成功注册之后，你将会得到一个 client ID 和一个 client secret，这个将被用于之后的实例化 Gitment。


### 第二步: 页面引入 Gitment 的静态资源文件

```html
<link rel="stylesheet" href="https://imsun.github.io/gitment/style/default.css">
<script src="https://imsun.github.io/gitment/dist/gitment.browser.js"></script>
```
当然你也可以选择把这两个静态资源文件下载到本地，然后放到你的站点对应静态资源目录下。


### 第三步: 实例化 Gitment

1.在需要使用评论系统的页面（一般情况下，找到你的文章的模板页）新增一个DOM节点用于放置评论框区域的内容。

```html
<div id="comment"></div>
```

2.在该页面加入如下的配置脚本：

```javascript

var gitment = new Gitment({
  id: '页面 ID', 
  owner: '你的 GitHub ID',
  repo: '存储评论的 repo',
  oauth: {
    client_id: '你的 client ID',
    client_secret: '你的 client secret',
  },
})
gitment.render('comment')

```

注意：

1.`gitment.render()`这个方法的参数就是你的评论区域 div 的 id 名;

2.页面 ID 如果不写，默认为 location.href。


### 第四步：初始化评论功能

第三步之后，你需要把你的网站部署到线上。如果前面三步没出错的话，应该能够看到评论框了。这个时候是不能够评论的。

点击在评论框的右侧`Login with GitHub`, 用你的 GitHub 登录， 然后点击中间那个蓝色的 `Initialize Comments`按钮，对该页面的评论功能进行初始化。

现在，你的这个页面的访客就可以使用 GitHub 账号登录进行评论了。唯一不足的是，每个页面的评论框都需要手动地初始化。
