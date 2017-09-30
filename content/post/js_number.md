+++
date = "2017-07-09T21:45:51+08:00"
categories = ["frontend"]
tags = ["JavaScript"]
title = "JavaScript 的 Number 需要注意的一些特性"
keywords = ["NaN", "Infinity", "parseInt()", "parseFloat()", "Number()", "JavaScript"]
description = "JavaScript 的 Number 有一些特性需要引起注意。比如： NaN 和 Infinity 这两个特殊的值。转换成数值的方法： parseInt(), parseFloat(), Number()。"
url = "/js-number.html"
+++

## 一、NaN：

1.定义：`NaN` 是 JavaScript 的一个特殊值，表示“非数字”（Not a Number），主要出现在将字符串解析成数字出错的场合。

2.`NaN` 不是一种独立的数据类型，而是一种特殊数值，它的数据类型依然属于 `number` ，使用 `typeof` 运算符可以看得很清楚。

	typeof NaN // 'number'

3.NaN不等于任何值，包括它本身。

	NaN === NaN // false

4.isNaN()：可以用来判断一个值是否为 NaN 。

`注意:` 如果传入的非数值(如字符串），会先进行类型转换, 转成 NaN, 所以这个方法并不可靠！用 isNaN() 之前需要判断一下数据类型是否为 number 。

	function isRealNaN(x){
		return typeof x === "number" && isNaN(x);
	}

或者利用 只有 NaN 是JavaScript之中唯一不等于自身的值这个特点，进行判断。

	function isTrueNaN(x){
		return x !== x;
	}

## 二、Infinity 与 isFinite()

1.`Infinity`：表示“无穷”，是一个特殊的数值，用来表示两种场景。一种是一个正的数值太大，或一个负的数值太小，无法表示；另一种是非0数值除以0，得到 `Infinity`。

2.`isFinite()`：返回一个`布尔值`，检查某个值是不是`正常数值`。

如果对 `NaN` 使用 `isFinite` 函数，也返回 `false`，表示 `NaN` 不是一个正常值。

	isFinite(Infinity) // false
	isFinite(NaN) // false
	isFinite("abc") // false
	isFinite(undefined) //false
	isFinite({}) //false


注意参数为 `true`, `false`, `null`, `[]`, `""` 时返回 `true`。

	isFinite(true) // true
	isFinite(false)// true
	isFinite(null) //true
	isFinite([]) //true
	isFinite("") //true
	isFinite(-1) // true


## 三、 parseInt() 和parseFloat()

1.`parseInt()` 用于将`字符串`转为`整数`; `parseFloat()`用于将`字符串`转为`浮点数`。

	parseInt('123') // 123
	parseFloat('3.14') // 3.14

2.字符串转为整数或浮点数的时候，是`一个个字符依次转换`，如果遇到不能转为数字的字符，就不再进行下去，返回已经转好的部分。

	parseInt('15px') // 15
	parseFloat('3.14abcd ') // 3.14

3.如果字符串前后有`空格`，空格会被自动去除。

	parseInt('   81') // 81
	parseFloat('\t\v\r12.34\n ') // 12.34

4.如果字符串的第一个字符不能转化为数字（后面跟着数字的正负号除外），返回`NaN`。

	parseInt('abc') // NaN
	parseInt('.3') // NaN
	parseInt('') // NaN
	parseInt('+') // NaN
	parseInt('+1') // 1

5.对于那些会自动转为`科学计数法`的数字，parseInt()会将科学计数法的表示方法视为字符串，因此导致一些奇怪的结果。如果字符串符合科学计数法，parseFloat())则会进行相应的转换。

	parseInt(1000000000000000000000.5) // 1
	// 等同于
	parseInt('1e+21') // 1

	parseFloat('314e-2') // 3.14
	parseFloat('0.0314E+2') // 3.14


6.`parseInt()`还可以接受第二个参数（2到36之间），表示被解析的值的进制，返回该值对应的十进制数。默认情况下，`parseInt`的第二个参数为10，即默认是十进制转十进制。

	parseInt('1000') // 1000
	// 等同于
	parseInt('1000', 10) // 1000
	parseInt('1000', 2) // 8
	parseInt('1000', 6) // 216
	parseInt('1000', 8) // 512

7.如果字符串包含对于指定进制无意义的字符，则从最高位开始，只返回可以转换的数值。如果最高位无法转换，则直接返回`NaN`。

	parseInt('1546', 2) // 1
	parseInt('546', 2) // NaN

8.如果`parseInt()`的第一个参数不是字符串，会被先转为字符串。这会导致一些令人意外的结果。

	parseInt(0x11, 36) // 43
	// 等同于
	parseInt('17', 36)
	parseInt(String(0x11), 36)

9.如果参数不是字符串，或者字符串的第一个字符不能转化为浮点数，则`parseFloat()`返回`NaN`。

	parseFloat([]) // NaN
	parseFloat('FF2') // NaN
	parseFloat('') // NaN


## 四、强制类型转换的函数：Number()

1.Number(): 可以将任意类型的值转化成数值。

2.`Number()`将字符串转为数值，要比`parseInt()`严格很多。基本上，只要有一个字符无法转成数值，整个`字符串`就会被转为`NaN`。

	parseFloat('123.45#') // 123.45
	Number('123.45#') // NaN

2.如果`Number()`的参数是`null`, `false`, `''`, `[]` 则结果为`0`；如果为 `true`，则结果为 `1`。`parseInt()`/`parseFloat()`的参数如果是这些特殊值时，一律为 `NaN`。

	Number(null)  //0
	Number("")   //0
	Number(false)   //0
	Number([])   //0
	Number(true) // 1

	parseInt(null) // NaN
	parseFloat(null) // NaN
	parseInt("") // NaN
	parseFloat("") // NaN
	parseInt(false) // NaN
	parseFloat(false) // NaN
	parseInt([]) // NaN
	parseFloat([]) // NaN
	parseInt(true)  // NaN
	parseFloat(true)  // NaN

3.`Number()`跟`parseInt()`、`parseFloat()`一样，会自动过滤字符串前后的`空格`。

	Number('\t\v\r12.34\n') // 12.34

4.如果参数是`对象`时，将返回`NaN`，除非是包含`单个数值的数组`。

	Number({a: 1}) // NaN
	Number([1, 2, 3]) // NaN
	Number([5]) // 5
