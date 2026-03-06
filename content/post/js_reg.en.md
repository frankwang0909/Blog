+++
categories = ["frontend"]
tags = ["RegExp"]
date = "2016-12-18T21:56:37+08:00"
title = "Js Reg"
banner = "/images/2016-12-18banner.jpg"
description = "JavaScript regular expression study notes"
keywords = ["JavaScript", "regular expression"]
url = "/js-reg.html"
+++

## 1.Basic concepts

A regular expression (`Regular Expression`) is a string that defines a rule according to which a series of strings that meet conditions are described and matched.

## 2. Wildcard

Find files in the current directory (linux command line)

find ./ -name *.txt

## 3. Online graphics tools:

[https://regexper.com/](https://regexper.com/) is a very practical regular expression graphical tool. You can also [download](https://regexper.com/) to your local computer to run faster


## 4. Regular expressions can be supported in IDE:

The editor I use is `Sublime Text 3`. Use the shortcut key `Ctrl+F` to search for a string, `Ctrl+H` to replace a string, and open regular expressions in the upper left corner of the panel called up at the bottom (shortcut key `Alt+R`)
	
http://www.wangxingfeng.com
	http://m.wangxingfeng.com
	http://cosmic.wangxingfeng.com
	http://blog.wangxingfeng.com
	http://img.wangxingfeng.com/1234.jpg
	http://img.wangxingfeng.com/158.png
	https://img.wangxingfeng.com/128744.jpg
	http://img.wangxingfeng.com/1285.jpg
	http://img.wangxingfeng.com/7884.png

In `Sublime`, find the `jpg` file of the `http` protocol in the `url` above and remove its protocol header.

Find What: http:\/\/(.+\.jpg)
	replace with: $1

## 5. Instantiate `RegExp` object in JavaScript

5. 1. Literal:
```javascript
	var reg = /\d/; 
	var reg2 = /[a-zA-Z0-9]/g;
```

5. 2.Constructor:
```javascript
	var reg = new RegExp(\d); 
	var reg = new RegExp('[a-zA-Z0-9]', 'g');
```

## 6. Modifier:

6. 1.`g`(global): indicates global matching. If not added, the first string will be matched by default.

6. 2.`i`(ignore case): Indicates ignoring case. If not added, the case will be case-sensitive by default.

6. 3.`m`(multiple lines): indicates multiple lines matching.


## 7. Original text characters and metacharacters:

7. 1. Original text character: represents the original meaning of the character, such as `a` represents the lowercase letter a, and `1` represents the number 1.

7. 2. Metacharacters: non-alphabetic characters with special meanings in regular expressions, such as asterisk `*`, question mark `? `Wait.

7. 3. Commonly used metacharacters and their meanings:

1) []: Construct character classes, range classes, etc.;
	2) {}: quantifier, indicating the number of characters;
	3) (): Construct a group;
	4) *: represents any number of characters; can be understood as {0,};
	5)? : Indicates that there is at most one character {0,1};
	6) +: Indicates that there is at least one character {1,};
	7) ^: negation;
	8)\n: newline character;
	9) \r: carriage return character;
	10)\0: null character;
	11) \t: horizontal tab character;
	12) \v: vertical tab character;
	13) \f: form feed character.

## 8. Character class:

8. 1. Usually, one character in a regular expression corresponds to one character in a string, such as `/a/` corresponding to the letter a. The metacharacter `[]` constructs a character class, such as `[abc]` which can match any one of the characters a, b or c. Enter in the browser debugging interface console:
```javascript
	'a1b2c3d4a'.match(/[abc]/g);
```

Will get the matching string:
```javascript
	["a", "b", "c", "a"]
```

8. 2 Character class negation:

Use the metacharacter ^ within `[]` to create a reverse class, that is, match strings that do not belong to a certain character class. For example, `[^abc]` matches content that is not the characters a, b, or c.
Enter in the browser debugging interface console:
```javascript	
	'a1b2c3d4a'.match(/[^abc]/g);
```

Will get the matching string:
```javascript	
	["1", "2", "3", "d", "4"]
```


8. 3 Scope class:

1)`[a-z]` means: any character from a to z;

Enter in the browser debugging interface console:
```javascript	
	'a1b2c3d4a'.match(/[a-z]/g);
```

Will get the matching string:
```javascript	
	["a", "b", "c", "d", "a"]
```

2)`[a-zA-Z]` means: any character from a to z and A to Z.

Enter in the browser debugging interface console:
```javascript	
	'a1B2Zc3d4'.match(/[a-zA-Z]/g);
```

Will get the matching string:
```javascript	
	["a", "B", "Z", "c", "d"]
```

8. 4 Predefined classes (abbreviation)

1) /./ => /[^\r\n]/ Any character except carriage return and line feed characters
	2) /\d/ => [0-9] numeric characters
	3) /\D/ => [^0-9] non-numeric characters
	4) /\s/ => whitespace character
	5) /\S/ => non-whitespace characters
	6) /\w/ => [a-zA-Z0-9_] word characters (letters, numbers, underscore.
	7) /\W/ => [^a-zA-Z0-9_] non-word characters
	8) \b: word boundary
	9) \B: non-word boundary;


9. Quantifier: A {} followed by a character indicates the number of times the previous character is repeated.

1. ) /\d{1,20}/: 1~20 numbers;
	2.) /\d*/ => /\d{0,}/: any number;
	3.) /\d+/ => /\d{1,}/ : at least one number;
	4.) /\d?/ => /\d{0,1}/: one more number;
	5.) /\d{3}/ : 3 numbers


## 10. Greedy mode and non-greedy mode:

10. 1. Greedy mode: Regular expressions will match as many characters as possible.

For example, the following regular expression matches a string of 3 to 6 digits, and by default will match as many as possible.
```javascript
	'b12345678A5879e123'.match(/\d{3,6}/g)
	// ["123456", "5879", "123"]
```

10. 2. Non-greedy mode: Add a question mark after the quantifier to match as few strings as possible.
```javascript
	'b12345678A5879e123'.match(/\d{3,6}?/g)
	// ["123", "456", "587", "123"]
```

## 11. Grouping:

11. 1. The brackets "()" turn the string into a group, allowing the quantifier to act on the group.

Sample code:
```javascript
	'abcabcabccc'.match(/abc{3}/g); 
	// ["abccc"]

	'abcabcabccc'.match(/(abc){3}/g);
	// ["abcabcabc"]
```

11. 2. Logical OR: The vertical bar "|" acts on grouping and can represent selecting one of multiple branches.
```javascript
	'whatwhaowho'.match(/wh(at|o)/g)；
	// ["what", "who"]

	'whatwhaowhowhy'.match(/wh(at|o|y)/g)
	// ["what", "who", "why"]
```

11. 3. Capture grouping, back reference

If you want to format the following date: `2016-01-20` => `01/20/2016`; you can write it like this
```javascript
	'2016-01-20'.replace(/(\d{4})-(\d{2})-(\d{2})/g, "$2/$3/$1")
	// "01/20/2016"
```

`$` plus a number, the number corresponds to the sequence number of the group, the content of the first group is captured with `$1`, the content of the second group is captured with `$2`, and so on.

11. 4. Ignore the group: Adding `?:` in the group means ignoring the group and capturing the contents of the group.
```javascript
	'2016-01-20'.replace(/(?:\d{4})-(\d{2})-(\d{2})/g, "$1/$2")
	// "01/20"
```

## 12. Assertion:

12. 1. Regular expressions are parsed from the beginning of the text to the end of the text. The direction of the end of the text is called "front", and vice versa is called "back".

12. 2. Look-ahead and look-ahead: When a regular expression matches a rule, it checks forward to see if it conforms to the assertion, which is called "look-ahead". Checking backward to see if an assertion is met is called "look-behind". JavaScript does not support lookbehinds.

12. 3. Positive/positive lookahead: forward conformity assertion. exp(?=assert)
```javascript
	'5a68cz7'.match(/\d(?=[a-z])/g);
	//["5", "8"]
```

12. 4. Negative/negative lookahead: Forward does not conform to the assertion. exp(?!assert)
```javascript
	'5a68cz7'.match(/\d(?=[a-z])/g);
	// ["6", "7"]
```

### 13.RegExp object properties

13. 1.`global`: Whether to search in full text (read-only attribute);

13. 2.`ignoreCase`: whether it is case sensitive (read-only attribute);

13. 3.`multline`: whether it is multi-line (read-only attribute);

13. 4.`source`: regular expression text content; (read-only attribute);

13. 5.`lastIndex`: The position next to the last character of the current expression matching content.
```javascript
	var reg1 = /\d{3,5}-\w{6}/, reg2 = /\d{3,5}-\w{6}/gim;
	reg1.global
	// false
	reg1.ignoreCase
	// false
	reg1.multiline
	// false
	reg2.global
	// true
	reg2.multiline
	// true
	reg2.ignoreCase
	// true
	reg1.source
	// "\d{3,5}-\w{6}"
	reg2.source
	// "\d{3,5}-\w{6}"
	reg1.source == reg2.source
	// true
```

## 14.RegExp methods: test(), exec()

14. 1.`RegExp.test(string)`: Test whether a string can match the regular expression. Parameters are strings; return value is Boolean.
```javascript
	var reg1 = /\d/, reg2 = /\d/g;
	reg1.test('a12ab');
	// true

	reg2.test('a12ab');
	// true

	reg2.test('a12ab');
	// true

	reg2.test('a12ab'); // Note that it becomes `false` here because the `lastIndex` property changes every time it is executed. Therefore, do not use the global matching mode when using RegExp with the `test` method.
	// false

	reg2.test('a12ab');
	// true

	reg2.test('a12ab');
	// true

	while(reg2.test('a12ab')){
		console.log('reg2.lastIndex:' +reg2.lastIndex);
	}
	//  reg2.lastIndex:2
	//  reg2.lastIndex:3
```

14. 2.`RegExp.exec(string)`: Returns an array of matching information.

Returns `null` if there is no matching text, otherwise returns a result array. Non-global matching mode, `lastIndex` is 0 and will not change. In global mode, `lastIndex` will change every time it is executed.
	
var reg1 = /\d+(\w)\d/, reg2 = /\d+(\w)\d/g, str="1a2ce58g79ht";
	var result = reg1.exec(str);
	console.log(reg1.lastIndex + '\t' + result.index+ '\t' + result.toString());
	>>> 0 0 1a2,a
	while(result=reg2.exec(str)){
		console.log('reg2.lastIndex:'+ reg2.lastIndex + '\t' + 'result.index:'+ result.index+ '\t' + result.toString());
	}
	>>>reg2.lastIndex:3 result.index:0 1a2,a
	>>>reg2.lastIndex:9 result.index:5 58g7,g


## 15. Some regular operations (search, replace, split, etc.) methods of String: match(), search(), replace(), split();

15. 1. `string.match(RegExp)`:

1) In non-global mode, return the first matching result and its `index` and the reference to the original string (see sample code);

2) In global mode, return all arrays whose matching results are elements;

3) Return `null` if the match fails.
```javascript
	var reg1 = /\d{4}-\d{2}-\d{2}/;
	var reg2 = /\d{4}-\d{2}-\d{2}/g;
	var str = "2016-10-01 2017-10-01 20181001";
	var matchArray1 = str.match(reg1);
	var matchArray2 = str.match(reg2);
	console.log(matchArray1);
	// ["2016-10-01", index: 0, input: "2016-10-01 2017-10-01 20181001"]

	console.log(matchArray2);
	// ["2016-10-01", "2017-10-01"]
```

15. 2.`string.search(RegExp)`:

The parameter can be a `substring` or a `regular expression`. This method is used to find the first successful match of a substring or regular expression in the string. If it is unsuccessful, it returns `-1`.

15. 3.`string.replace(RegExp, replacement)`：

1) This method is used to perform regular expression replacement, replacing the text that `RegExp` can match with the second parameter `replacement`. By default, only one match is performed. If set to global mode, all matching text will be replaced.
```javascript	
	"2016-10-01 2017-10-01 20181001".replace(/\d{4}-\d{2}-\d{2}/, "Date");
	// "Date 2017-10-01 20181001"

	"2016-10-01 2017-10-01 20181001".replace(/\d{4}-\d{2}-\d{2}/g, "Date");
	// "Date Date 20181001"
```

2) If the second parameter string refers to groups, you can use `$1` to represent the first group, `$2` to represent the second group, and so on.
```javascript	
	"2016-10-01 2017-10-01 20181001".replace(/(\d{4})-(\d{2})-(\d{2})/, "$2/$3/$1");
	// "10/01/2016 2017-10-01 20181001"

	"2016-10-01 2017-10-01 20181001".replace(/(\d{4})-(\d{2})-(\d{2})/g, "$2/$3/$1");
	// "10/01/2016 10/01/2017 20181001"

	"2016-10-01 2017-10-01 20181001".replace(/(\d{4})-?(\d{2})-?(\d{2})/g, "$2/$3/$1");
	// "10/01/2016 10/01/2017 10/01/2018"
```

3) If you want to represent the `$` character in the second parameter, you must use `$$` to escape.
```javascript	
	"the price is 12.99".replace(/([\d+\.\d{0,2}|\d+])/, "$$$1");
	// "the price is $12.99"

	"the price is 12".replace(/([\d+\.\d{0,2}|\d+])/, "$$$1");
	"the price is $12"

	"the price is 12.99".replace(/(\d+\.\d{0,2})/, "￥$1");
	// "the price is ￥12.99"

	"the price is 12".replace(/([\d+\.\d{0,2}|\d+])/, "$");
	"the price is $12"
```
4) The second parameter can also be a function.

The example below shows how to convert words starting with t to uppercase.
```javascript	
	"one two three".replace(/\bt[a-zA-Z]+\b/g, function(m){
		return m.toUpperCase();
	});
	// "one TWO THREE"
```

15. 4. `string.split(RegExp)`:

This method uses a regular expression to split the string. Whether the regular expression uses a global pattern has no effect on the result.
```javascript
	"one two three".split(/s+/);
	// ["one two three"]
```
