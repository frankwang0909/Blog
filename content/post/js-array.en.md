+++
tags = ["array"]
keywords = ["JavaScript array methods", "slice", "splice", "Array.isArray"]
description = "Summary of commonly used JavaScript array methods. You will no longer be confused between slice() and splice(). Methods that do not change the original array, methods that change the original array, and methods that determine whether an object is an array Array.isArray()"
date = "2017-04-06T22:31:32+08:00"
title = "Js Array"
categories = ["frontend"]
url ="/js-array.html"
+++

## Method without changing the original array:

1. `indexOf()` and `lastIndexOf()`

1. 1 `indexOf()`: Returns the index of the element in the array, starting from `0`. If the element does not exist in the array, `-1` is returned.
```javascript
	var arr = [1, 2];
	arr.indexOf(1); //0
	arr.indexOf(10); //-1
```

1. 2 `lastIndexOf()`:
Returns the index of the last occurrence of an element in the array, or -1 if it does not appear.
```javascript
	var arr = [1, 2, 3, 4, 2];
	arr.lastIndexOf(2); // 4
```

2. `slice()`: Like the `substring()` method of `string`, it intercepts a part of the array and returns a new array.

2. 1 Usually, it accepts 2 parameters as a left-closed and right-open interval, that is, it includes the element at the starting index position, but does not include the element at the ending index position.
```javascript
	var arr = [1, 2, 3,4,5,6];
	arr.slice(0,2)    // [1, 2] only returns elements at index 0,1
```

2. 2 You can omit the second parameter, that is, intercept the last element of the original array.
```javascript
	arr.slice(2,);    //[3, 4, 5, 6] 
```

2. 3 If no parameters are passed, a new array intercepting all elements from beginning to end will be returned. Can be used to copy an array.
```javascript
	var copyArr = arr.slice();
	copyArr;   //[1, 2, 3, 4, 5, 6]
```

3. `concat()`: merge arrays. Concatenates the current array with another array and returns a new array.

3. 1 The parameters of the `concat()` method can have multiple parameters, or any type, such as `numeric`, `string`, `Boolean`, `array`, and `object`. The parameters will be added to the new array.
```javascript
	var arr1 =  [1, 2, 3,4,5,6];
	var arr2 = ['a','b','c'];
	var arr3 = arr1.concat(arr2);
	arr3;   //[1, 2, 3, 4, 5, 6, "a", "b", "c"]
```

3. 2 Note that if the parameter is an `array`, it will be flattened once, that is, the array will be split and added to a new array. See specific examples:
```javascript
	var arr1 = [1, 2, 3];
	var arr2 = arr1.concat(66,'abc',true,[10,20],[30,[31,32]],{x:100});
	arr2;  //[1, 2, 3, 66, "abc", true, 10, 20, 30, [31,32], {x:100}]
```

4. `join()`: Convert to string. It will concatenate each element of the current Array with the specified string, and then return the concatenated string.

4. 1 The parameter is a string used to specify the connection. See sample code:
```javascript
	var arr = [1, 2, 3];
	arr.join('*')   //"1*2*3"
```

4. 2 If no parameters are specified, the default is to use `,` to connect.
```javascript
	var arr = [1, 2, 3];
	arr.join()   //"1,2,3"
```

5. `toString()`: Returns the string form of the array
```javascript
	var arr = [1, 2, 3];
	arr.toString() // "1,2,3"
```

6. `valueOf()`: Returns the array itself
```javascript
	var arr = [1, 2, 3];
	arr.valueOf() // [1, 2, 3]
```


7. `map()`:

7. 1 Call a function on all members of the array in sequence, and the return value is a new array.
```javascript
	var arr = [1, 2, 3];
	arr.map(function(elem){
		return elem*2;
	});
	//[2, 4, 6, 8]
	arr; //[1, 2, 3]
```

7. 2 The `map` method accepts a function as a parameter. When the function is called, the map method will pass in 3 parameters, namely the current member, the current position and the array itself (the last 2 parameters are optional).
```javascript
	arr.map(function(elem, index, arr) {
		return elem * index;
	}); 
	//[0, 2, 6]
```

7. 3 The `map` method can also accept a second parameter, which represents the object pointed to by `this` when the callback function is executed.

8. `forEach()`: Very similar to the map method, it also traverses all members of the array and performs some operation. **Note**: The `forEach` method generally has no return value
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

**Note**: The `forEach` method cannot interrupt execution and will always traverse all members. If you want to interrupt the traversal when certain conditions are met, use a `for loop`.

9. `filter()`:

9. 1 Filter the elements of the array, and the return value is a new array composed of elements that meet the filter conditions.
```javascript	
	var arr = [1, 2, 3, 4, 5];
	arr.filter(function (elem) {
	  return (elem > 3);
	});
	//[4, 5]
```

9. 2 The `filter` method accepts a function as a parameter. When the function is called, the `fitler` method will pass in 3 parameters, namely the current member, the current position and the array itself (the last two parameters are optional).
```javascript
	var arr = [1, 2, 3, 4, 5];
	arr.filter(function (elem, index, arr) {
	  return index % 2 === 1;
	});
	//[2, 4]
```

9. 3 The `filter` method can also accept the second parameter, which specifies the `context object` (ie `this object`) where the test function is located.

10. `some()` and `every()`: similar to "assert", used to determine whether array members meet certain conditions.

10. 1 Accepts a function as a parameter, all array members execute the function in sequence, and return a `Boolean value`. This function accepts three parameters, which are the member of the current position, the sequence number of the current position and the entire array.

10. 2 The `some` method is that as long as the return value of one array member is true, the return value of the entire some method is true, otherwise it is false.
```javascript	
	var arr = [1, 2, 3, 4];
	arr.some(function (elem, index, arr) {
	  return elem >= 3;
	});
	// true
```

10. 3 The `every` method returns true only if the return values ​​of all array members are true, otherwise false.
```javascript	
	var arr = [1, 2, 3, 4];
	arr.every(function (elem, index, arr) {
	  return elem >= 3;
	});
	// false
```

10. 4 Note that for `empty array`, the `some` method returns false and the `every` method returns true

10. 5 The `some` and `every` methods can also accept a second parameter, which is used to bind the `this keyword` in the function.

11. `reduce()` and `reduceRight()`: Process each member of the array in turn, and finally accumulate a value.

11. 1 `reduce` is processed from `left to right` (from the first member to the last member)
```javascript
	arr.reduce(function(x, y){
	  console.log(x, y)
	  return x + y;
	});
	// 1 2
	// 3 3
	// 6
```

11. 2 `reduceRight` is processed from `right to left` (from the last member to the first member)
```javascript
	arr.reduceRight(function(x, y){
	  console.log(x, y)
	  return x + y;
	});
	// 3 2
	// 5 1
	// 6
```

## Method to change the original array:

1. `push()`: Add several elements to the end of the array. The return value is the changed array length.
```javascript	
	var arr = [1, 2];
	arr.push(3) ;// 3
	arr; //  [1, 2, 3]
	arr.push('b','c'); //5
	arr; //[1, 2, 3, "b", "c"]
	arr.push([10,20]); //6
	arr; //[1, 2, 3, "b", "c", [10,20]]
```


2. `pop()`: Delete the last element of the array. The return value is the deleted element.
```javascript
	var arr =[1, 2, 3, "b", "c", [10,20]];
	arr.pop(); //[10, 20]
	arr;  // [1, 2, 3, "b", "c"]
```

3. `unshift()`: Add several elements to the head of the array. The return value is the changed array length.
```javascript
	var arr = [1, 2];
	arr.unshift(3,4 );  //4
	arr;  // [3, 4, 1, 2]
```

4. `shift()`: Delete the last element of the array. The return value is the deleted element.
```javascript
	var arr = ['a', 'b', 1, 2];
	arr.shift(); //'a'
	arr;  //['b', 1, 2]
```

5. `sort()`: Array sorting.

5. 1 **Note**: The default is to convert all elements into `string` and then sort by `string Unicode code point`. The return value is the new array.
```javascript
	var arr = [1, 2, 12, 'a', 'b', 'ab', 'A', 'B']
	arr.sort();  // [1, 12, 2, "A", "B", "a", "ab", "b"] Note: 12 comes before 2
```


5. 2 If the elements are all numbers and they need to be sorted from small to large, you can pass in a callback function as a parameter.
```javascript
	var arr = [1, 2, 12, 100]

	arr.sort(function(a,b){
		return a-b;
	});
    // [1, 2, 12, 100]
```

5. 3 If you want to sort from large to small:
```javascript
	arr.sort(function(a,b){
		return b-a;
	});
	//[100, 12, 2, 1]
```

6. `reverse()`: Reverse the position of elements in the array
```javascript
	var arr = [1, 2, 12, 'a', 'b', 'ab', 'A', 'B'];
	arr.reverse();
	//["B", "A", "ab", "b", "a", 12, 2, 1]
```

7. `splice()`: Modify array elements (add, delete, replace). Delete `several` elements starting from `specified index`, and then add `several elements` from that position. The return value is an array of deleted elements. Parameter 1 is the starting index of the element to be deleted, parameter 2 is the number of elements to be deleted, and the subsequent parameters are the elements to be added.

7. 1 Only delete, not add. You can pass in 2 parameters:
```javascript
	var arr = ['Alibaba', 'Tencent', 'Baidu', 'XiaoMi', '360'];

	// Delete 3 elements starting from index 2
	arr.splice(2, 3); // Return deleted elements ['Baidu', 'XiaoMi', '360']
	arr; // ['Alibaba', 'Tencent']
```

7. 2 Only add, not delete. The second parameter is set to `0`, which means the element will not be deleted.
```javascript
	arr.splice(2, 0, 'Toutiao', 'Meituan', 'Didi'); // Returns [] because no elements were deleted
	arr; //["Alibaba", "Tencent", "Toutiao", "Meituan", "Didi"]
```

7. 3 First delete several elements, and then add several elements at the deleted positions.
```javascript
	var  arr =["Alibaba", "Tencent", "Toutiao", "Meituan", "Didi"]
	arr.splice(2,2,'Apple','Google');  //["Toutiao", "Meituan"]
	arr; //["Alibaba", "Tencent", "Apple", "Google", "Didi"]
```

## Array.isArray()

Used to determine whether a value is an array. If the parameter is an array, return true, otherwise, return false.
```javascript
	var arr = [1,2]
	Array.isArray(arr);  //true;

	Array.isArray('a'); //false
```
