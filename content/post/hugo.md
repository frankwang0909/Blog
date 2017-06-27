+++
banner = "/images/2017-04-03banner.jpg"
keywords = "Hugo, 建站, 静态博客, GitHub"
description = "用Hugo快速搭建个人静态博客，并托管到GitHub"
categories = ["tools"]
tags = ["Hugo", "GitHub"]
date = "2017-04-03T20:49:23+08:00"
title = "用Hugo快速搭建个人静态博客"
images = ["/images/2017-04-03sm.jpg"]
url = "build-blog-with-hugo"

+++

最近心血来潮，想要重新折腾一番自己的博客。于是，发现了Hugo比之前使用的Jekyll更好用。本文是个人参照[Hugo官网](https://gohugo.io/overview/quickstart/) 搭建个人博客的记录。

## Step 1. Install Hugo 下载、安装Hugo
下载地址：[https://github.com/spf13/hugo/releases](https://github.com/spf13/hugo/releases)。
根据自己的操作系统，下载对应的安装包。我的操作系统是`Win7 64bit`， 选择了`hugo_0.19_Windows-64bit.zip`。

下载完成之后，解压的文件夹包含以下3个文件：

	hugo_0.19_windows_amd64.exe
	LICENSE.md
	README.md

将 `hugo_0.19_windows_amd64.exe` 重命名为`hugo.exe`。在你的软件安装盘新增名为`hugo`的文件目录，在里面在新建一个`bin`子目录。然后将`hugo.exe`放到`hugo\bin`目录下。再将这个`bin`目录的路径添加到`系统环境变量`中。

完成以上步骤后，打开命令行输入

	hugo help

如果得到如下信息，说明安装成功。

	hugo is the main command, used to build your Hugo site.

	Hugo is a Fast and Flexible Static Site Generator
	built with love by spf13 and friends in Go.

	Complete documentation is available at http://gohugo.io/.


## Step 2. 创建一个名为blog的Hugo站点
我希望在E盘下创建站点，所以我先切换目录

	cd e:
	e:

然后输入命令：

	hugo new site blog 

得到如下提示创建成功的信息：

	Congratulations! Your new Hugo site is created in E:\blog.

	Just a few more steps and you're ready to go:

	1. Download a theme into the same-named folder.
	Choose a theme from https://themes.gohugo.io/, or
	create your own with the "hugo new theme <THEMENAME>" command.
	2. Perhaps you want to add some content. You can add single files
	with "hugo new <SECTIONNAME>\<FILENAME>.<FORMAT>".
	3. Start the built-in live server via "hugo server".

	Visit https://gohugo.io/ for quickstart guide and full documentation.

进入该目录，可以看到自动生成了5个目录和一个配置文件config.toml

	|-- archetypes
	|-- content   #存放内容的目录
	|-- data      
	|-- layouts   
	|-- static    #存放静态资源（图片,css,js）
	|-- themes    #存放主题
	|-- config.toml  #配置文件

## Step 3. 添加内容
切换到该目录下，然后输入如下命令，会在`content`的目录下创建`post`目录，在`post`目录下创建名为`test.md`的文件。

	cd blog
	hugo new post/test.md

提示文件创建成功：

	E:\blog\content\post\test.md created

用文本编辑器打开文件`test.md`文件
可以看到如下内容：

	+++
	date = "2017-01-02T17:45:06+08:00"  #创建文件的时间
	title = "test"                      #文件的标题
	draft = true                        # 是否为草稿

	+++

上述内容为自动创建的与文章有关的内容。自己也可以在两个`+++`之间添加如下内容：

	image = "hugo.png"            #指定图片。
	category = "test"             #文章的类别
	tags = ["Hugo", "intro"]      #文章的标签分类。
	url = "new_start"             #该文章访问时的相对的url地址，默认为文件名。

更多的设置，可以参考[官方文档](https://gohugo.io/content/front-matter/)。

以后写博客文章就是这样创建`markdown`文件, 之后通过`Hugo`编译成静态的html文件。

## Step 4. 添加主题
官方提供了多种主题可供选择，具体在 [https://themes.gohugo.io/](https://themes.gohugo.io/) 可以找到。

找到想要的主题后，切换到`themes`目录（该目录可以存放多个不同的主题）。

	cd themes

由于需要使用到Git下载主题，以及版本管理和代码推送。需要事先下载安装好[Git](https://git-for-windows.github.io/)，关于如何安装和使用Git，可以参考我之前的一篇文章：[Git学习笔记](http://www.wangxingfeng.com/git-intro/)。

把选定的主题下载到`themes`目录下。

	git clone https://github.com/dim0627/hugo-icarus-theme.git


## Step 5. 启动服务，本地预览
先从`themes`目录下退回到`blog`目录, 然后启动服务。

	cd ..
    hugo server --theme=hugo-icarus-theme --buildDrafts

在浏览器中打开 http://localhost:1313/


## Step 6. 修改配置文件`config.toml`

	languageCode = "zh-cn"
	title = "Frank Wang's Coding World"
	baseurl = "http://www.wangxingfeng.com/"  

	[Params]
		Author ="Frank Wang"


## Step 7.  生成网站

### 1.改变文章`draft`（草稿）状态：

	hugo undraft content/post/*.md

### 2. 启动`hugo`, 生成发布文件到`public`目录下。

	hugo --theme=hugo-icarus-theme


## Step 8. 托管到`GitHub Pages`

### 1. 使用`Git`来进行版本管理

	git init
	echo "/public/" >> .gitignore
	echo "/themes/" >> .gitignore
	git add --all
	git commit -m "Initial commit"

### 2. 创建`Git` 远程仓库：
登录你的`GitHub`. 创建一个新的仓库，仓库名为`Github用户.github.io`, 比如我的是`frankwang0909.github.io `.

### 3. 添加`Git` 远程仓库，并提交代码。

	cd public
	git init
	git remote add origin git@github.com:frankwang0909/frankwang0909.github.io.git

	git add --all
	git commit -m "blog added"
	git push -u origin master


### 4.以后有内容改动，提交代码.

	(cd ..; hugo --theme=hugo_theme_robust)
	git add --all
	git commit -m "<some change message>"
	git push -u origin master
