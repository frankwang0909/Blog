+++
keywords = ["Block-level scoping in ES6", "let declare variables", "temporary dead zone", "const declaration constant"]
description = "ES6 introduces the concept of block-level scope. Use let to declare variables and const to declare constants."
categories = ["frontend"]
tags = ["block scope"]
date = "2017-04-07T20:18:56+08:00"
title = "Es6 Let Const"
url = "/es6-let-const.html"
+++

## 1. Block-level scope

`ES5` only has `global scope` and `function scope`, but no `block-level scope`.

Variables declared outside the function are global variables, which can easily lead to variable conflicts. Therefore, we have to use `execute function immediately` to avoid conflicts with global variables. In addition, variables used for counting within the loop will also be leaked into global variables.

To this end, `ES6` introduces the concept of `block-level scope`.


## 2. let declare variables

2. 1 Variables declared with `let` are only valid within the code block in which they are located (block-level scope).
```javascript
	{
	    var a = 1;
		let b = 2;
	}
	a //1 
	b // Uncaught ReferenceError: b is not defined
```

2. 2 The counter of the `for loop` is declared using the `let` command.
```javascript
	for (let i = 0; i < 10; i++) {
		//
	}
	console.log(i);  //ReferenceError: i is not defined
```

2. 3 There is no `variable promotion`. Variables should follow the `declare first and then use' principle.

Variables declared with `var` are hoisted to the top of the scope and can be used before the variable is declared, with the value `undefined`. The variable declared by `let` does not have `variable promotion`. If it is used before the declaration, an error will be reported.

2. 4 Temporary dead zone (TDZ):

Once a variable is declared with `let` inside a block scope, that binding only exists in that scope and is not affected by outer scopes. The variable cannot be accessed before the `let` declaration within that scope, even if a variable with the same name exists outside it.
```javascript
	let a = 1;
	if (true) {
		// TDZ starts
		console.log(a); //Uncaught ReferenceError: a is not defined

		let a;  // TDZ ends
	}

	let b = 1;
	if (true) {
		let b = 100; 
		console.log(b);  //100
	} 
```

You can understand the `temporary dead zone` this way: as soon as you enter the current block-level scope, all the variables to be used already exist, but they are not yet available. You can only obtain and use the variable after it is declared.

2. 5 Variables cannot be declared repeatedly

Within the same scope, the `let` command cannot declare the same variable repeatedly.
```javascript
	function () {
		let x = 10;
		var x = 20;
	}
	// Uncaught SyntaxError: Identifier 'x' has already been declared
```

## 3. const declares constants

3. 1 `ES6` introduces the concept of `constants`. The `const command` is used to declare `constants`, usually using `uppercase letters` to represent constants. Once declared, the value of a constant cannot be changed.
```javascript
	const PI = 3.1415;
	PI = 3; //Uncaught TypeError: Assignment to constant variable.
```

3. 2 When declaring a variable, it must be assigned a value immediately. Otherwise, an error will be reported.
```javascript
	const SIN //Uncaught SyntaxError: Missing initializer in const declaration
```

3. 3 The scope of `const` is the same as the `let` command: a constant is only valid within the `block-level scope` in which it is declared.
```javascript	
	if (true) {
	  const A = 5;
	}
	A // Uncaught ReferenceError: A is not defined
```

3. 4 The constants declared by the `const` command are not promoted. There is also a `temporary dead zone` and can only be used after the declared position. At the same time, repeated statements cannot be made.
