+++
menu = ""
keywords = "ES6的块级作用域, let声明变量, 暂时性死区, const声明常量 "
description = "ES6引入了块级作用域的概念。用let声明变量,用const声明常量 "
categories = ["frontend"]
tags = ["块级作用域"]
date = "2017-04-07T20:18:56+08:00"
title = "ES6的块级作用域以及let、const命令"
url = "es6-let-const"

+++



## 1.块级作用域

`ES5` 只有`全局作用域`和`函数作用域`，没有`块级作用域`。 

在函数外部声明的变量，都是全局变量，容易导致变量冲突。因此，我们不得不使用`立即执行函数`来避免全局变量的冲突。另外，在循环内用来计数的变量也会泄露成全局变量。

为此，`ES6` 引入了`块级作用域`的概念。


## 	2.`let` 声明变量 

2.1 `let`声明的变量，只在它所在的代码块（块级作用域）内有效。

	{
	    var a = 1;
		let b = 2;
	}
	a //1 
	b // Uncaught ReferenceError: b is not defined

2.2 `for循环`的计数器使用`let`命令来声明。

	for (let i = 0; i < 10; i++) {
		//
	}
	console.log(i);  //ReferenceError: i is not defined

2.3 不存在`变量提升`。变量应该遵循`先声明后使用`的原则。

`var`声明的变量会提升到作用域的顶部,在变量可以在声明之前可以使用，值为`undefined`。`let`声明的变量不存在`变量提升`, 声明之前使用，会报错。

2.4 暂时性死区(temporal dead zone，简称 TDZ):

只要`块级作用域`内存在`let命令`，它所声明的变量就“绑定”（binding）这个区域，不再受外部的影响。在let命令声明该变量之前的区域内，该变量不能使用，即使外部声明了该变量。

	let a = 1;
	if (true) {
		// TDZ开始
		console.log(a); //Uncaught ReferenceError: a is not defined

		let a;  //TDZ结束
	}

	let b = 1;
	if (true) {
		let b = 100; 
		console.log(b);  //100
	} 

可以这么理解暂时性死区：只要一进入当前的块级作用域，所有将要使用的变量就已经存在了，但是还暂时无法获取，只有等到声明变量之后，才可以获取和使用该变量。

2.5 不能重复声明变量

在同一个作用域内，`let`命令不能重复声明同一个变量。

	function () {
		let x = 10;
		var x = 20;
	}
	// Uncaught SyntaxError: Identifier 'x' has already been declared


## 3.`const` 声明常量

3.1 `ES6` 引入了`常量`的概念。`const 命令`是用来声明`常量`的, 通常用`大写字母`表示常量。一旦声明，常量的值就不能改变。

	const PI = 3.1415;
	PI = 3; //Uncaught TypeError: Assignment to constant variable.

3.2 `声明变量时，必须立即赋值。否则会报错。

	const SIN //Uncaught SyntaxError: Missing initializer in const declaration

3.3 `const`的作用域与`let`命令相同：常量只在它声明时所在的`块级作用域`内有效。
	
	if (true) {
	  const A = 5;
	}
	A // Uncaught ReferenceError: A is not defined

3.4 `const`命令声明的常量也是不提升，同样存在`暂时性死区`，只能在声明的位置后面使用。同时，也不能重复声明。
