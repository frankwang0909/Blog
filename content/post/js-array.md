+++
tags = ["数组"]
keywords = ["JavaScript数组方法", "slice", "splice", "Array.isArray"]
description = "JavaScript数组常用方法总结，再也不会傻傻分不清slice()和splice()，不改变原数组的方法，改变原数组的方法，判断某个对象是否是数组的方法Array.isArray()"
date = "2017-04-06T22:31:32+08:00"
title = "JavaScript数组的常用方法总结"
categories = ["frontend"]
url ="/js-array.html"
+++

## 不改变原数组的方法：

1.`indexOf()` 和`lastIndexOf()`

1.1 `indexOf()` : 返回元素在数组的索引，从`0`开始。若数组不存在该元素，则返回`-1`。
```javascript
	var arr = [1, 2];
	arr.indexOf(1); //0
	arr.indexOf(10); //-1
```

1.2 `lastIndexOf()`:
返回元素在数组中最后一次出现的索引，如果没有出现则返回-1.
```javascript
	var arr = [1, 2, 3, 4, 2];
	arr.lastIndexOf(2); // 4
```

2.`slice()`: 与`字符串`的`substring()`方法一样，截取数组的一部分，返回一个新的数组。

2.1 通常，接受2个参数作为一个左闭右开区间，即包括开始索引位置的元素，但不包括结束索引位置的元素。
```javascript
	var arr = [1, 2, 3,4,5,6];
	arr.slice(0,2)    //[1, 2] 只返回索引0,1位置的元素
```

2.2 可以省略第二个参数，即截取到原数组的最后一个元素。
```javascript
	arr.slice(2,);    //[3, 4, 5, 6] 
```

2.3 如果没有传参数，则返回一个从头到尾截取所有元素的新数组。可以用来复制一个数组。
```javascript
	var copyArr = arr.slice();
	copyArr;   //[1, 2, 3, 4, 5, 6]
```

3.`concat()`: 合并数组。把当前的数组和另一个数组连接起来，并返回一个新的数组。

3.1 `concat()`方法的参数可以有多个，也可以任意任意类型，`数值`、`字符串`、`布尔值`、`数组`、`对象` 都可以，参数会被被添加到新的数组中。
```javascript
	var arr1 =  [1, 2, 3,4,5,6];
	var arr2 = ['a','b','c'];
	var arr3 = arr1.concat(arr2);
	arr3;   //[1, 2, 3, 4, 5, 6, "a", "b", "c"]
```

3.2 注意，如果参数是`数组`, 会被拉平一次，即数组会被拆开来，加入到新的数组中。具体看示例：
```javascript
	var arr1 = [1, 2, 3];
	var arr2 = arr1.concat(66,'abc',true,[10,20],[30,[31,32]],{x:100});
	arr2;  //[1, 2, 3, 66, "abc", true, 10, 20, 30, [31,32], {x:100}]
```

4.`join()`: 转成字符串。它会把当前Array的每个元素都用指定的字符串连接起来，然后返回连接后的字符串。

4.1 参数是用来指定连接的字符串。见示例代码：
```javascript
	var arr = [1, 2, 3];
	arr.join('*')   //"1*2*3"
```

4.2 如果没有指定参数，默认是用`,`连接。
```javascript
	var arr = [1, 2, 3];
	arr.join()   //"1,2,3"
```

5.`toString()`: 返回数组的字符串形式
```javascript
	var arr = [1, 2, 3];
	arr.toString() // "1,2,3"
```

6.`valueOf()`:返回数组本身
```javascript
	var arr = [1, 2, 3];
	arr.valueOf() // [1, 2, 3]
```


7.`map()`: 

7.1 对数组的所有成员`依次调用一个函数`，返回值是一个新数组。
```javascript
	var arr = [1, 2, 3];
	arr.map(function(elem){
		return elem*2;
	});
	//[2, 4, 6, 8]
	arr; //[1, 2, 3]
```

7.2 `map`方法接受一个函数作为参数,该函数调用时，map方法会将其传入3个参数，分别是当前成员、当前位置和数组本身(后2个参数可选)。
```javascript
	arr.map(function(elem, index, arr) {
		return elem * index;
	}); 
	//[0, 2, 6]
```

7.3 `map`方法还可以接受第2个参数，表示回调函数执行时`this`所指向的对象。

8.`forEach()`: 与map方法很相似，也是遍历数组的所有成员，执行某种操作。**注意**：`forEach`方法一般没有返回值
```javascript
	var arr = [1, 2, 3];
	function log(element, index, array) {
		console.log('[' + index + '] = ' + element);
	}
	arr.forEach(log);
	// [0] = 1
	// [1] = 2
	// [2] = 3
```

**注意**: `forEach`方法无法中断执行，总是会将所有成员遍历完。如果希望符合某种条件时，就中断遍历，要使用`for循环`。

9.`filter()`: 

9.1 筛选数组的元素，返回值是符合筛选条件元素组成的一个新数组。
```javascript	
	var arr = [1, 2, 3, 4, 5];
	arr.filter(function (elem) {
	  return (elem > 3);
	});
	//[4, 5]
```

9.2 `filter`方法接受一个函数作为参数,该函数调用时，`fitler`方法会将其传入3个参数，分别是当前成员、当前位置和数组本身(后2个参数可选)。
```javascript
	var arr = [1, 2, 3, 4, 5];
	arr.filter(function (elem, index, arr) {
	  return index % 2 === 1;
	});
	//[2, 4]
```

9.3 `filter`方法还可以接受第2个参数，指定测试函数所在的`上下文对象`（即`this对象`）。

10.`some()`和`every()`: 类似“断言”（assert），用来判断数组成员是否符合某种条件。

10.1 接受一个函数作为参数，所有数组成员依次执行该函数，返回一个`布尔值`。该函数接受三个参数，依次是当前位置的成员、当前位置的序号和整个数组。

10.2 `some`方法是只要有一个数组成员的返回值是true，则整个some方法的返回值就是true，否则false。
```javascript	
	var arr = [1, 2, 3, 4];
	arr.some(function (elem, index, arr) {
	  return elem >= 3;
	});
	// true
```

10.3 `every`方法则是所有数组成员的返回值都是true，才返回true，否则false。
```javascript	
	var arr = [1, 2, 3, 4];
	arr.every(function (elem, index, arr) {
	  return elem >= 3;
	});
	// false
```

10.4 注意，对于`空数组`，`some`方法返回false，`every`方法返回true

10.5 `some`和`every`方法还可以接受第2个参数，用来绑定函数中的`this关键字`。

11.`reduce()`和`reduceRight()`: 依次处理数组的每个成员，最终累计为一个值。

11.1`reduce`是`从左到右`处理（从第一个成员到最后一个成员）
```javascript
	arr.reduce(function(x, y){
	  console.log(x, y)
	  return x + y;
	});
	// 1 2
	// 3 3
	// 6
```

11.2`reduceRight`则是`从右到左`处理（从最后一个成员到第一个成员）
```javascript
	arr.reduceRight(function(x, y){
	  console.log(x, y)
	  return x + y;
	});
	// 3 2
	// 5 1
	// 6
```

## 改变原数组的方法：

1.`push()`: 向数组的末尾添加若干元素。返回值是改变后的数组长度。
```javascript	
	var arr = [1, 2];
	arr.push(3) ;// 3
	arr; //  [1, 2, 3]
	arr.push('b','c'); //5
	arr; //[1, 2, 3, "b", "c"]
	arr.push([10,20]); //6
	arr; //[1, 2, 3, "b", "c", [10,20]]
```


2.`pop()`: 删除数组最后一个元素。返回值是删除的元素。
```javascript
	var arr =[1, 2, 3, "b", "c", [10,20]];
	arr.pop(); //[10, 20]
	arr;  // [1, 2, 3, "b", "c"]
```

3.`unshift()`: 向数组头部添加若干元素。返回值是改变后的数组长度。
```javascript
	var arr = [1, 2];
	arr.unshift(3,4 );  //4
	arr;  // [3, 4, 1, 2]
```

4.`shift()`: 删除数组最后一个元素。返回值是删除的元素。
```javascript
	var arr = ['a', 'b', 1, 2];
	arr.shift(); //'a'
	arr;  //['b', 1, 2]
```

5.`sort()`: 数组排序。

5.1 **注意**：默认是将所有元素转换成`字符串`，再按`字符串Unicode码点`排序。返回值是新的数组。
```javascript
	var arr = [1, 2, 12, 'a', 'b', 'ab', 'A', 'B']
	arr.sort();  //[1, 12, 2, "A", "B", "a", "ab", "b"] 注意：12排在了2的前面
```


5.2 如果元素都是`数字`，要按`从小到大`排序，可以传入一个回调函数作为参数。
```javascript
	var arr = [1, 2, 12, 100]

	arr.sort(function(a,b){
		return a-b;
	});
    // [1, 2, 12, 100]
```

5.3 如果想要`从大到小`排序：
```javascript
	arr.sort(function(a,b){
		return b-a;
	});
	//[100, 12, 2, 1]
```

6.`reverse()`: 颠倒数组中元素的位置
```javascript
	var arr = [1, 2, 12, 'a', 'b', 'ab', 'A', 'B'];
	arr.reverse();
	//["B", "A", "ab", "b", "a", 12, 2, 1]
```

7.`splice()`: 修改数组元素（新增、删减、替换）。从`指定的索引`开始删除`若干个`元素，然后再从该位置添加`若干个元素`。返回值是删除的元素组成的数组。参数1是删除元素的起始索引，参数2是删除的元素个数，之后的参数为待添加的元素。

7.1 只删除,不添加。可以传入2个参数：
```javascript
	var arr = ['Alibaba', 'Tencent', 'Baidu', 'XiaoMi', '360'];

	// 从索引2开始删除3个元素
	arr.splice(2, 3); // 返回删除的元素 ['Baidu', 'XiaoMi', '360']
	arr; // ['Alibaba', 'Tencent']
```

7.2 只添加,不删除。第2个参数设为`0`，即不删除元素。
```javascript
	arr.splice(2, 0, 'Toutiao', 'Meituan', 'Didi'); // 返回[],因为没有删除任何元素
	arr; //["Alibaba", "Tencent", "Toutiao", "Meituan", "Didi"]
```

7.3 先删除若干元素，然后在删除的位置上在添加若干个元素。
```javascript
	var  arr =["Alibaba", "Tencent", "Toutiao", "Meituan", "Didi"]
	arr.splice(2,2,'Apple','Google');  //["Toutiao", "Meituan"]
	arr; //["Alibaba", "Tencent", "Apple", "Google", "Didi"]
```

## Array.isArray()

用来判断一个值是否为数组, 如果参数为数组，返回true，否则，返回false.
```javascript
	var arr = [1,2]
	Array.isArray(arr);  //true;

	Array.isArray('a'); //false
```
