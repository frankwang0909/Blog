+++
date = "2017-07-09T21:45:51+08:00"
categories = ["frontend"]
tags = ["JavaScript"]
title = "Js Number"
keywords = ["NaN", "Infinity", "parseInt()", "parseFloat()", "Number()", "JavaScript"]
description = "JavaScript's Number has some features that warrant attention. For example: NaN and Infinity are two special values. Methods for converting to numeric values: parseInt(), parseFloat(), Number()."
url = "/js-number.html"
+++

## 1. NaN:

1. Definition: `NaN` is a special value in JavaScript, which means "Not a Number". It mainly occurs when there is an error in parsing a string into a number.

2. `NaN` is not an independent data type, but a special value. Its data type still belongs to `number`, which can be seen clearly using the `typeof` operator.

typeof NaN // 'number'

3. NaN is not equal to any value, including itself.

NaN === NaN // false

4. isNaN(): can be used to determine whether a value is NaN.

`Note:` If a non-numeric value (such as a string) is passed in, type conversion will be performed first and converted to NaN, so this method is not reliable! Before using isNaN(), you need to determine whether the data type is number.

function isRealNaN(x){
		return typeof x === "number" && isNaN(x);
	}

Or make use of the fact that NaN is the only value in JavaScript that is not equal to itself to make a judgment.

function isTrueNaN(x){
		return x !== x;
	}

## 2. Infinity and isFinite()

1. `Infinity`: means "infinity" and is a special value used to represent two scenarios. One is that a positive value is too large, or a negative value is too small to be represented; the other is that a non-0 value is divided by 0 to get `Infinity`.

2. `isFinite()`: Returns a `Boolean value` to check whether a certain value is a `normal value`.

If the `isFinite` function is used on `NaN`, it also returns `false`, indicating that `NaN` is not a normal value.

isFinite(Infinity) // false
	isFinite(NaN) // false
	isFinite("abc") // false
	isFinite(undefined) //false
	isFinite({}) //false


Note that `true` is returned when the parameters are `true`, `false`, `null`, `[]`, `""`.

isFinite(true) // true
	isFinite(false)// true
	isFinite(null) //true
	isFinite([]) //true
	isFinite("") //true
	isFinite(-1) // true


## 3. parseInt() and parseFloat()

1. `parseInt()` is used to convert `string` to `integer`; `parseFloat()` is used to convert `string` to `floating point number`.

parseInt('123') // 123
	parseFloat('3.14') // 3.14

2. When a string is converted to an integer or floating point number, it is converted one character at a time. If it encounters a character that cannot be converted into a number, it will not continue and the converted part will be returned.

parseInt('15px') // 15
	parseFloat('3.14abcd ') // 3.14

3. If there are spaces before and after the string, the spaces will be automatically removed.

parseInt(' 81') // 81
	parseFloat('\t\v\r12.34\n ') // 12.34

4. If the first character of the string cannot be converted into a number (except for the sign followed by a number), `NaN` is returned.

parseInt('abc') // NaN
	parseInt('.3') // NaN
	parseInt('') // NaN
	parseInt('+') // NaN
	parseInt('+1') // 1

5. For those numbers that will be automatically converted to `scientific notation`, parseInt() will treat the scientific notation representation as a string, thus leading to some strange results. If the string conforms to scientific notation, parseFloat()) will perform the corresponding conversion.

parseInt(1000000000000000000000.5) // 1
	// Equivalent to
	parseInt('1e+21') // 1

parseFloat('314e-2') // 3.14
	parseFloat('0.0314E+2') // 3.14


6. `parseInt()` can also accept a second parameter (between 2 and 36), indicating the base of the parsed value, and returns the decimal number corresponding to the value. By default, the second parameter of `parseInt` is 10, that is, the default is decimal to decimal.

parseInt('1000') // 1000
	// Equivalent to
	parseInt('1000', 10) // 1000
	parseInt('1000', 2) // 8
	parseInt('1000', 6) // 216
	parseInt('1000', 8) // 512

7. If the string contains meaningless characters for the specified base, starting from the highest bit, only values ​​that can be converted will be returned. If the highest bit cannot be converted, `NaN` is returned directly.

parseInt('1546', 2) // 1
	parseInt('546', 2) // NaN

8. If the first parameter of `parseInt()` is not a string, it will be converted to a string first. This can lead to some surprising results.

parseInt(0x11, 36) // 43
	// Equivalent to
	parseInt('17', 36)
	parseInt(String(0x11), 36)

9. If the parameter is not a string, or the first character of the string cannot be converted to a floating point number, `parseFloat()` returns `NaN`.

parseFloat([]) // NaN
	parseFloat('FF2') // NaN
	parseFloat('') // NaN


## 4. Forced type conversion function: Number()

1. Number(): can convert any type of value into a numerical value.

2. `Number()` converts a string into a numerical value, which is much stricter than `parseInt()`. Basically, as long as one character cannot be converted to a numeric value, the entire `string` will be converted to `NaN`.

parseFloat('123.45#') // 123.45
	Number('123.45#') // NaN

2. If the parameter of `Number()` is `null`, `false`, `''`, `[]`, the result is `0`; if it is `true`, the result is `1`. If the parameters of `parseInt()`/`parseFloat()` are these special values, they will always be `NaN`.

Number(null) //0
	Number("") //0
	Number(false) //0
	Number([]) //0
	Number(true) // 1

parseInt(null) // NaN
	parseFloat(null) // NaN
	parseInt("") // NaN
	parseFloat("") // NaN
	parseInt(false) // NaN
	parseFloat(false) // NaN
	parseInt([]) // NaN
	parseFloat([]) // NaN
	parseInt(true) // NaN
	parseFloat(true) // NaN

3. `Number()`, like `parseInt()` and `parseFloat()`, will automatically filter the `spaces` before and after the string.

Number('\t\v\r12.34\n') // 12.34

4. If the parameter is an object, NaN will be returned unless it is an array containing a single value.

Number({a: 1}) // NaN
	Number([1, 2, 3]) // NaN
	Number([5]) // 5
