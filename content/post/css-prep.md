+++
keywords = ["CSS预处理器", "Less","CSS Preprocessors"]
description = "CSS预处理器之Less, CSS Preprocessors, CSS预处理器为CSS的编写提供变量、mixin、函数、规则嵌套、颜色处理等便利"
categories = ["frontend"]
tags = ["CSS"]
title = "CSS预处理器之Less"
url ="less.html"
date = "2017-04-23T16:28:38+08:00"

+++

## 1.CSS

`CSS`层叠样式表(Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。

由于`CSS`不想普通的编程语言有自己的变量、常量、条件语句、函数等编程语法，而只是一行行单纯的属性描述，所以写起来相当的费事，代码难以组织和维护。

## 2.DRY

`DRY`, 即 Don't Repeat Yourself， 是一种为程序员所熟悉的编程理念，优秀的程序员通常遵循这种规范编写代码。
`DRY`可以显著地提升代码的可维护性，比如在需要改变某个参数的时候，只需要改动一处或者少数几处地方。

## 3.CSS预处理器

纯粹的`CSS`代码并没有变量、嵌套、条件等概念，难以做到DRY, 这令程序员们头痛不已。因此，有程序员尝试为 `CSS` 增加一些编程的的特性，使得在 `CSS` 中使用变量、简单的程序逻辑、函数成为可能。

目前，最常用的CSS预处理器，主要有3个：`Less`、`SASS`、`Stylus`。
从[GitHub](https://github.com/showcases/css-preprocessors)上可以看出`Less`是最受欢迎的`CSS`预处理器。
![](/images/2017042301.jpg)

## 3.Less

### 3.1 安装
因为`Less`是使用`JavaScript`语言写的，它可以运行在服务端的`NodeJS`环境中，因此，最简单的安装方式是用 `npm install`。

	npm install -g less # -g表示全局安装

### 3.2 编译
`Less`文件的后缀名为`.less`. 浏览器并不能直接识别`.less`的文件，需要编译成`.css`结尾的`CSS`样式文件。
假设你已经有一个`less`文件`demo.less`，在命令行执行以下命令，即可编译生成`demo.css`。

	lessc demo.less demo.css  

`lessc`是Less的命令，第一个参数demo.less为指定需要编译的源文件名， 第二个参数demo.css为编译后的CSS文件名。

如果需要编译成压缩的CSS文件，可以全局安装下载一个Less官方提供的插件 [clean-css plugin](https://github.com/less/less-plugin-clean-css)。

	npm install -g less-plugin-clean-css

然后，在命令行输入如下命令：

	lessc --clean-css demo.less demo.min.css #多了一个参数 --clean-css

### 3.3 基本语法

#### 3.3.1 变量

Less 的变量名使用` @ `符号开始, 比如：

	@nice-blue: #5B83AD;
	@light-blue: @nice-blue + #111;

	#header {
	  color: @light-blue;
	}

编译之后，得到如下代码：

	#header {
	  color: #6c94be;
	}

注意：Less的变量本质上是常量，只能定义 一次。

#### 3.3.2 Mixins
将一系列属性从一个规则集引入(“混合”)到另一个规则集的方式。

比如，先定义了一个规则

	.bordered {
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}

想要在其他的地方使用到这个规则，可以这样：

	#menu a {
	  color: #111;
	  .bordered;
	}

	.post a {
	  color: red;
	  .bordered;
	}

编译结果如下：

	.bordered {
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}
	#menu a {
	  color: #111;
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}
	.post a {
	  color: red;
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}


#### 3.3.3 嵌套
根据HTML结构来嵌套样式规则。

	#header {
	  color: black;
	  .navigation {
	    font-size: 12px;
	  }
	  .logo {
	    width: 300px;
	  }
	}

编译之后的CSS样式文件：

	#header {
	  color: black;
	}
	#header .navigation {
	  font-size: 12px;
	}
	#header .logo {
	  width: 300px;
	}

还可以结合伪类来嵌套，比如“清除浮动”的样式可以这样写：

	.clearfix {
	  display: block;
	  zoom: 1;

	  &:after {
	    content: " ";
	    display: block;
	    font-size: 0;
	    height: 0;
	    clear: both;
	    visibility: hidden;
	  }
	}

上述代码里的符号` & `表示当前选择器的父选择器。

编译之后的结果如下：

	.clearfix {
	  display: block;
	  zoom: 1;
	}
	.clearfix:after {
	  content: " ";
	  display: block;
	  font-size: 0;
	  height: 0;
	  clear: both;
	  visibility: hidden;
	}


#### 3.3.4 媒体查询及嵌套

媒体查询（Media query ）可以嵌套在选择器中，编译时，会自动把选择器复制到媒体查询体内。媒体查询规则里还可以嵌套媒体查询。

	.screen-color {
	  @media screen {
	    color: green;
	    @media (min-width: 768px) {
	      color: red;
	    }
	  }
	  @media tv {
	    color: black;
	  }
	}

编译结果：

	@media screen {
	  .screen-color {
	    color: green;
	  }
	}
	@media screen and (min-width: 768px) {
	  .screen-color {
	    color: red;
	  }
	}
	@media tv {
	  .screen-color {
	    color: black;
	  }
	}


#### 3.3.5 运算
在Less中，数值、颜色、变量可以进行加、减、乘、除的运算。

	@color: #224488 / 2; //results in #112244
	background-color: #112244 + #111; // result is #223355

	@base: 5%;
	@filler: @base * 2; // result is 10%
	@other: @base + @filler; // result is 15%

#### 3.3.6 函数

`Less`提供了许多用于转换颜色、处理字符串 以及进行算术运算的函数。具体可以参考[Less Function Reference](http://lesscss.org/functions/)

这些函数使用起来非常简单。

	@base: #f04615;
	@width: 0.5;

	.class {
	  width: percentage(@width); 
	  color: saturate(@base, 5%);
	  background-color: spin(lighten(@base, 25%), 8);
	}

在上述代码中我们使用 函数`percentage()` 将 0.5 转换为 50%，然后用 函数`saturate()`将基础颜色值的饱和度增加了 5%，再使用 函数lighten() 将背景颜色的亮度增加了 25%，最后通过函数spin()又将色相值增加 8。编译之后：

	.class {
	  width: 50%;
	  color: #f6430f;
	  background-color: #f8b38d;
	}

### 3.5 官网
更多内容，可以访问[http://lesscss.org/](http://lesscss.org/)
