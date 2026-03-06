+++
date = "2017-07-16T21:43:35+08:00"
title = "TypeScript Introduction"
keywords = ["TypeScript", "JavaScript", "static typing", "type annotations", "classes", "interfaces"]
description = "TypeScript is a Microsoft language (released in 2012) and a superset of JavaScript. It compiles to JavaScript and adds static typing and class-based object-oriented features."
categories = ["frontend"]
tags = ["TypeScript"]
url = "/typescript_basic.html"
+++

## 1. Introduction

[TypeScript](http://www.typescriptlang.org/) is a Microsoft language released in 2012. It is a `superset` of JavaScript, compiles to JavaScript, and adds optional static typing plus class-based object-oriented capabilities.

TypeScript files have the extension `.ts`.

TypeScript cannot run directly in the browser environment. It needs to be compiled into JavaScript before running in the browser.

TypeScript is the officially recommended language for `Angular 2` development. It can also be used as a development language for projects using frameworks or class libraries such as React, Vue, and ReactNative.

A minimal TypeScript example (`demo.ts`):
```typescript
var book: string = "Angular 2";  // Defines a variable book of string type

var num: number = 123;  // Defines a variable num of type number

function log(msg: string): void {  // A function log is defined, and its parameter msg is of type string. `:void` means that this function has no return value.
	console.log(msg);
}
```

## 2. Install TypeScript
```shell
npm install -g typescript
```

## 3. Compile

3.1 Local compilation: run `tsc <file>.ts` to generate a JavaScript file with the same base name.
```shell
tsc demo.ts
```

After compiling `demo.ts`, you get `demo.js`:

```typescript	
var book = "Angular 2";
var num = 123;
function log(msg) {
	console.log(msg);
}
```

3.2 Online compilation: TypeScript provides an official [online playground](http://www.typescriptlang.org/play/index.html).

## 4. Editor: Visual Studio Code

Microsoft officially provides a lightweight but powerful editor for TypeScript - [VS Code](https://code.visualstudio.com/). Visual Studio Code is a lightweight editor, and with extensions it provides many of Visual Studio's advanced capabilities.

## 5. Language Feature: Type Annotations

Type annotations in TypeScript are a lightweight way to add constraints to functions or variables.

In the example code, we want the log function to receive a string parameter. Then try changing the call to log to pass in an array:
```typescript
function log(msg: string) {
	return "Hello, " + msg;
}

var msg = [0, 1, 2];

log(msg);
```

TypeScript provides static code analysis, which can analyze the code structure and provided type annotations. Therefore, the above code will prompt an error in VS Code:
	
Argument of type 'number[]' is not assignable to parameter of type string

## 6. Language Feature: Interfaces

One of the core principles of TypeScript is type checking the structure that a value has. It is sometimes called "duck typing" or "structural subtyping".

In TypeScript, the role of interfaces is to name these types and define contracts for your code or third-party code.

Simple example:
```typescript
function print(obj: { a: string }) {
	console.log(obj.a);
}

let myObj = { 
	size: 10, 
	a: "Size 10 Object" 
};

print(myObj);
```

The type checker looks at calls to the function print(). It has an object parameter, and this object parameter has a property named a, of type string. It should be noted that the object parameter we pass in will actually contain many properties, but the compiler will only check whether those required properties exist and whether their types match.

Use the `interface` keyword to define contracts. By convention, interface names are PascalCase.

Rewriting the example with an `interface`:
```typescript
interface MyValue {
	a: string;
}

function print(obj: MyValue) {
	console.log(obj.a);
}

let myObj = {
	size: 10, 
	a: "Size 10 Object"
};
print(myObj);
```

## 7. Language Feature: Classes

### 7.1 Defining a class

Before ES2015, JavaScript used prototype-based inheritance without `class` syntax. ES2015 introduced classes, and TypeScript builds on that model with stronger typing.


Sample code:
```typescript
class Greeter {
	
	// Defines properties of string type,
	greeting: string;

	// Defines the constructor of the class, whose parameters are of type string
	constructor(message: string) {

		this.greeting = message;
	}

	// defines a class method
	greet() {
		return "Hello, " + this.greeting;
	}
}
```

The above code declares a Greeter class. This class has 3 members: a property called greeting, a constructor, and a greet method.

We use `this` when referencing any class member, which indicates that we are accessing a member of the class.

### 7.2 Instantiation
```typescript
let greeter = new Greeter("world");
```

An instance of the Greeter class is created using `new`. It will call the previously defined constructor, create a new object of type Greeter, and execute the constructor to initialize it.

### 7.3 Inheritance

Sample code:
```typescript
class Animal {
	name:string;
	constructor(theName: string) { 
		this.name = theName; 
	}
	move(distanceInMeters: number = 0) {
		console.log(`${this.name} moved ${distanceInMeters}m.`);
	}
}

class Snake extends Animal {
	constructor(name: string) {
		super(name); // The super() method must be called to execute the constructor of the parent class
	}
	move(distanceInMeters = 5) {
		console.log("Slithering...");
		super.move(distanceInMeters); 
	}
}

class Horse extends Animal {
	constructor(name: string) { 
		super(name); 
	}
	move(distanceInMeters = 45) {
		console.log("Galloping...");
		super.move(distanceInMeters);
	}
}

let sam = new Snake("Sammy the Python");
let tom: Animal = new Horse("Tommy the Palomino");

sam.move();
tom.move(34);
```

Similar to other languages, TypeScript uses the keyword `extends` to create subclasses. You can see that both Horse and Snake are subclasses of Animal and have access to its properties and methods.

A derived class that contains a constructor must call `super()`, which will execute the parent class's constructor.

Methods of the parent class can be overridden in subclasses. In the above code, both Snake class and Horse class create move methods, which override the move method inherited from Animal, so that the move method has different functions according to different classes.

### 7.4 Access Modifiers

7.4.1 `public` (default)

If no `modifier` is used to modify the members (properties, methods) of the class, the default is `public`, which means that we can freely access this member of the class.

7.4.2 `private`

When a member is marked `private`, it cannot be accessed `outside` the class in which it is declared.
```typescript
class Animal {
	private name: string;
	constructor(theName: string) { 
		this.name = theName; 
	}
}

new Animal("Cat").name; // Error: 'name' is private;
```

7.4.3 `protected`

The `protected` modifier behaves very similarly to the `private` modifier, but with one difference, `protected` members are still accessible in `derived classes`.
```typescript
class Person {
	protected name: string;
	constructor(name: string) { 
		this.name = name; 
	}
}

class Employee extends Person {
	private department: string;

	constructor(name: string, department: string) {
		super(name)
		this.department = department;
	}

	public getElevatorPitch() {
		return `Hello, my name is ${this.name} and I work in ${this.department}.`;
	}
}

let howard = new Employee("Howard", "Sales");
console.log(howard.getElevatorPitch());
console.log(howard.name); // error
```

We cannot use name outside the Person class, but we can still access it through the instance methods of the Employee class because Employee is derived from Person.

7.4.4 `readonly`

You can use the `readonly` keyword to set a property to `read-only`. Read-only properties must be initialized at declaration time or in the constructor.
```typescript
class Octopus {
	readonly name: string;
	readonly numberOfLegs: number = 8;
	constructor (theName: string) {
		this.name = theName;
	}
}

let dad = new Octopus("Man with the 8 strong legs");

dad.name = "Man with the 3-piece suit"; // error! name is readonly.
```
