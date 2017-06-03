+++
categories = ["frontend"]
tags = ["RegExp"]
date = "2016-12-18T21:56:37+08:00"
title = "JavaScript的正则表达式"
banner = "/images/2016-12-18banner.jpg"
description = "JavaScript的正则表达式学习笔记"
keywords = "JavaScript, 正则表达式"
url = "js-reg"
+++

## 1.基本概念

正则表达式(`Regular Expression`)是一个字符串，定义了某个规则，按照这种规则来描述、匹配一系列符合条件的字符串。

## 2.通配符

当前目录下查找文件(linux 命令行)

	find ./ -name *.txt

## 3.在线图形工具：

[https://regexper.com/](https://regexper.com/) 是一款非常实用的正则表达式图形化工具。你也可以[下载](https://regexper.com/)到本地，运行速度更快


## 4.IDE中可以支持正则表达式：

我用的是编辑器是`Sublime Text 3`。快捷键`Ctrl+F`查找字符串，`Ctrl+H `替换字符串，在底部唤出的面板左上角有开启正则表达式（快捷键`Alt+R`）
	
	http://www.wangxingfeng.com
	http://m.wangxingfeng.com
	http://cosmic.wangxingfeng.com
	http://blog.wangxingfeng.com
	http://img.wangxingfeng.com/1234.jpg
	http://img.wangxingfeng.com/158.png
	https://img.wangxingfeng.com/128744.jpg
	http://img.wangxingfeng.com/1285.jpg
	http://img.wangxingfeng.com/7884.png

`Sublime`中找出上面的`url`中`http`协议的`jpg`文件，去掉其协议头

	Find What: http:\/\/(.+\.jpg)
	replace with: $1

## 5.JavaScript中实例化`RegExp`对象

5.1.字面量: 

	var reg = /\d/; 
	var reg2 = /[a-zA-Z0-9]/g;

5.2.构造函数:  

	var reg = new RegExp(\d); 
	var reg = new RegExp('[a-zA-Z0-9]', 'g');


## 6.修饰符：

6.1.`g`(global):表示全局匹配，不添加则默认匹配到第一个字符串。

6.2.`i`(ignore case):表示忽略大小写,不添加则默认大小写敏感。

6.3.`m`(multiple lines):表示多行匹配。


## 7.原意文本字符 和元字符：

7.1.原意文本字符：表示字符的原本含义，如`a`表示小写字母a，`1`表示数字1。

7.2.元字符：在正则表达式中有特殊含义的非字母字符，如星号`*`，问号`？`等。

7.3.常用元字符及其含义：

	1）[]:构建字符类，范围类等；
	2）{}:量词，表示字符的个数；
	3）():构建分组；
	4）*：表示任意个字符；可理解为{0,}；
	5）？：表示最多有一个该字符{0,1}；
	6）+：表示至少有一个该字符{1,}；
	7）^: 取反；
	8）\n: 换行符；
	9）\r: 回车符；
	10）\0: 空字符；
	11）\t: 水平制表符；
	12）\v:  垂直制表符；
	13）\f: 换页符。

## 8.字符类：

8.1.通常，正则表达式一个字符对应字符串一个字符，如`/a/`对应字母a。元字符`[]`构建一个字符类，如`[abc]`可以匹配字符a或b或c中的任意一个。在浏览器调试界面控制台输入：
	
	'a1b2c3d4a'.match(/[abc]/g);

会得到匹配的字符串：
	
	["a", "b", "c", "a"]

8.2字符类取反：

在`[]`内使用元字符^创建反向类，即匹配不属于某个字符类的字符串。如`[^abc]`匹配不是字符a、b、c的内容。
在浏览器调试界面控制台输入：
	
	'a1b2c3d4a'.match(/[^abc]/g);

会得到匹配的字符串：
	
	["1", "2", "3", "d", "4"]


8.3范围类：

1)`[a-z]`表示：a到z的任意一个字符；

在浏览器调试界面控制台输入：
	
	'a1b2c3d4a'.match(/[a-z]/g);

会得到匹配的字符串：
	
	["a", "b", "c", "d", "a"]

2)`[a-zA-Z]`表示：a到z以及A到Z的任意一个字符。

在浏览器调试界面控制台输入：
	
	'a1B2Zc3d4'.match(/[a-zA-Z]/g);

会得到匹配的字符串：
	
	["a", "B", "Z", "c", "d"]

8.4 预定义类（简写）

	1) /./ => /[^\r\n]/  除了回车符和换行符之外的任何字符
	2) /\d/ => [0-9]  数字字符
	3) /\D/ => [^0-9] 非数字字符
	4) /\s/ => 空白字符
	5) /\S/ => 非空白字符
	6) /\w/ => [a-zA-Z0-9_]单词字符（字母，数字，下划线. 
	7) /\W/ => [^a-zA-Z0-9_]非单词字符
	8) \b: 单词边界
	9) \B：非单词边界；


9.量词：在字符后跟一个{}表示重复前面字符的次数。

	1.) /\d{1,20}/: 1~20个数字；
	2.) /\d*/ => /\d{0,}/: 任意个数字;
	3.) /\d+/ => /\d{1,}/  :至少一个数字；
	4.) /\d?/ => /\d{0,1}/ :之多一个数字；
	5.) /\d{3}/ : 3个数字


## 10.贪婪模式与非贪婪模式：

10.1.贪婪模式：正则表达式会尽可能多地去匹配字符。

例如，下面的正则表达式，匹配3到6个数字的字符串，默认会尽可能多地去匹配。

	'b12345678A5879e123'.match(/\d{3,6}/g)

	>>>["123456", "5879", "123"]

10.2.非贪婪模式：在量词后加一个问号, 尽可能少地去匹配字符串。

	'b12345678A5879e123'.match(/\d{3,6}?/g)

	>>>["123", "456", "587", "123"]


## 11.分组：

11.1.括号“()”把字符串变成分组，使量词作用于分组。

示例代码：

	'abcabcabccc'.match(/abc{3}/g); 
	>>>["abccc"]

	'abcabcabccc'.match(/(abc){3}/g);
	>>>["abcabcabc"]

11.2.逻辑或：竖线 “|” 作用于分组, 可以表示选择多个分支中的一个。

	'whatwhaowho'.match(/wh(at|o)/g)；
	>>>["what", "who"]

	'whatwhaowhowhy'.match(/wh(at|o|y)/g)
	>>>["what", "who", "why"]

11.3.捕获分组，反向引用

想要把如下日期格式化：`2016-01-20` => `01/20/2016`；可以这样写

	'2016-01-20'.replace(/(\d{4})-(\d{2})-(\d{2})/g, "$2/$3/$1")
	>>>"01/20/2016"


`$`加上一个数字，数字对应的是分组的序号，第一个分组的内容用`$1`来捕获，第二分组的内容用`$2`来捕获，以此类推。

11.4.忽略分组：分组内加上`?:`表示忽略该分组，而捕获该组的内容。

	'2016-01-20'.replace(/(?:\d{4})-(\d{2})-(\d{2})/g, "$1/$2")
	>>>"01/20"


## 12.断言：

12.1.正则表达式从文本头部向文本尾部开始解析，文本尾部方向称为“前”，反之，为“后”。

12.2.前瞻与后顾：正则表达式匹配到规则的时候，向前检查是否符合断言，称为"前瞻"。向后检查是否符合断言则称为"后顾"。JavaScript不支持后顾。

12.3.正向/肯定前瞻：向前符合断言。exp(?=assert)

		'5a68cz7'.match(/\d(?=[a-z])/g);
		>>>["5", "8"]

12.4.负向/否定前瞻：向前不符合断言。exp(?!assert)

	'5a68cz7'.match(/\d(?=[a-z])/g);
	>>>["6", "7"]


### 13.RegExp对象属性

13.1.`global`: 是否全文搜索（只读属性）;

13.2.`ignoreCase`：是否大小写敏感（只读属性）;

13.3.`multline`: 是否多行（只读属性）;

13.4.`source`：正则表达式文本内容；（只读属性）;

13.5.`lastIndex`: 当前表达式匹配内容的最后一个字符的下一个位置。   

	var reg1 = /\d{3,5}-\w{6}/, reg2 = /\d{3,5}-\w{6}/gim;
	reg1.global
	>>>false
	reg1.ignoreCase
	>>>false
	reg1.multiline
	>>>false
	reg2.global
	>>>true
	reg2.multiline
	>>>true
	reg2.ignoreCase
	>>>true
	reg1.source
	>>>"\d{3,5}-\w{6}"
	reg2.source
	>>>"\d{3,5}-\w{6}"
	reg1.source == reg2.source
	>>>true

## 14.RegExp的方法：`test()`, `exec()`;

14.1.`RegExp.test(string)`: 测试某个字符串是否能够匹配该正则表达式。参数为字符串；返回值为布尔值。

	var reg1 = /\d/, reg2 = /\d/g;
	reg1.test('a12ab');
	>>>true

	reg2.test('a12ab');
	>>>true

	reg2.test('a12ab');
	>>>true

	reg2.test('a12ab'); //注意这里变成`false`了就是因为每执行一次，`lastIndex`属性变了一次导致的。所以用`test`方法的RegExp不要用全局匹配模式。
	>>>false

	reg2.test('a12ab');
	>>>true

	reg2.test('a12ab');
	>>>true

	while(reg2.test('a12ab')){
		console.log('reg2.lastIndex:' +reg2.lastIndex);
	}
	>>> reg2.lastIndex:2
	>>> reg2.lastIndex:3

14.2.`RegExp.exec(string)`: 返回匹配信息的数组。

如果没有匹配的文本，则返回`null`，否则返回一个结果数组。非全局匹配模式，`lastIndex`为0，不会变。全局模式下，每次执行，`lastIndex`都会跟着改变。
	
	var reg1 = /\d+(\w)\d/, reg2 = /\d+(\w)\d/g, str="1a2ce58g79ht";
	var result = reg1.exec(str);
	console.log(reg1.lastIndex + '\t' + result.index+ '\t' + result.toString());
	>>> 0	0	1a2,a
	while(result=reg2.exec(str)){
		console.log('reg2.lastIndex:'+ reg2.lastIndex + '\t' + 'result.index:'+ result.index+ '\t' + result.toString());	
	}
	>>>reg2.lastIndex:3	result.index:0	1a2,a
	>>>reg2.lastIndex:9	result.index:5	58g7,g


## 15.`String`的一些正则操作(查找、替换、切分等)方法：`match()`、`search()`、`replace()`、`split()`;

15.1. `string.match(RegExp)`： 

1)非全局模式下，返回第一个匹配结果及其`index`以及原字符串的引用(见示例代码)；

2)全局模式下，返回所有匹配结果为元素的数组；

3)匹配失败则返回`null`。

	var reg1 = /\d{4}-\d{2}-\d{2}/;
	var reg2 = /\d{4}-\d{2}-\d{2}/g;
	var str = "2016-10-01 2017-10-01 20181001";
	var matchArray1 = str.match(reg1);
	var matchArray2 = str.match(reg2);
	console.log(matchArray1);
	>>>["2016-10-01", index: 0, input: "2016-10-01 2017-10-01 20181001"]

	console.log(matchArray2);
	>>>["2016-10-01", "2017-10-01"]

15.2.`string.search(RegExp)`:

参数可以是`子字符串`也可以是`正则表达式`。这个方法用来寻找某个子字符串或者正则表达式在该字符串中第一次匹配成功的位置，如果不成功，则返回`-1`.

15.3.`string.replace(RegExp, replacement)`：

1)这个方法用来进行正则表达式替换，将`RegExp`能匹配的文本替换成第二个参数`replacement`。默认只进行一次匹配。如果设定为全局模式，则所有能匹配的文本都会替换。
	
	"2016-10-01 2017-10-01 20181001".replace(/\d{4}-\d{2}-\d{2}/, "Date");
	>>>"Date 2017-10-01 20181001"

	"2016-10-01 2017-10-01 20181001".replace(/\d{4}-\d{2}-\d{2}/g, "Date");
	>>>"Date Date 20181001"

2)如果第二个参数字符串中引用分组，可以使用`$1`表示第一个分组，`$2`表示第二个分组，以此类推。
	
	"2016-10-01 2017-10-01 20181001".replace(/(\d{4})-(\d{2})-(\d{2})/, "$2/$3/$1");
	>>>"10/01/2016 2017-10-01 20181001"

	"2016-10-01 2017-10-01 20181001".replace(/(\d{4})-(\d{2})-(\d{2})/g, "$2/$3/$1");
	>>>"10/01/2016 10/01/2017 20181001"

	"2016-10-01 2017-10-01 20181001".replace(/(\d{4})-?(\d{2})-?(\d{2})/g, "$2/$3/$1");
	>>>"10/01/2016 10/01/2017 10/01/2018"

3)如果要在第二个参数中表示`$`字符，则必须使用`$$`转义。
	
	"the price is 12.99".replace(/([\d+\.\d{0,2}|\d+])/, "$$$1");
	>>>"the price is $12.99"

	"the price is 12".replace(/([\d+\.\d{0,2}|\d+])/, "$$$1");
	"the price is $12"

	"the price is 12.99".replace(/(\d+\.\d{0,2})/, "￥$1");
	>>>"the price is ￥12.99"

	"the price is 12".replace(/([\d+\.\d{0,2}|\d+])/, "$");
	"the price is $12"

4)第二个参数还可以是函数。

下面的例子展示了如何将t开头的单词转换为大写。
	
	"one two three".replace(/\bt[a-zA-Z]+\b/g, function(m){
		return m.toUpperCase();
	});
	>>>"one TWO THREE"

15.4. `string.split(RegExp)`:

这个方法使用一个正则表达式切分字符串，正则表达式是否使用了全局模式对结果没有影响。
	
	"one two three".split(/s+/);
	>>>["one two three"]

