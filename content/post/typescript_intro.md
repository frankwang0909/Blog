+++
date = "2017-07-16T21:43:35+08:00"
title = "TypeScript 入门"
keywords = ["TypeScript", "JavaScript", "静态类型","类型注解", "类 Class", "接口 Interface"]
description = "TypeScript 是微软2012年推出的一种编程语言，属于 JavaScript 的超集，可以编译为 JavaScript 执行。它拓展了 JavaScript 的语法，给 JavaScript 添加可选的静态类型和基于类的面向对象编程。"
categories = ["frontend"]
tags = ["TypeScript"]
url = "/typescript_basic.html"
+++

## 1.简介：

[TypeScript](http://www.typescriptlang.org/) 是微软2012年推出的一种编程语言，属于 JavaScript 的`超集`，可以编译为 JavaScript 执行。它拓展了 JavaScript 的语法，给 JavaScript 添加可选的`静态类型`和`基于类`的面向对象编程。

TypeScript文件拓展名为 `.ts`。

TypeScript 不能直接运行在浏览器环境中，运行前需要编译成 JavaScript 才能在浏览器运行。

TypeScript 是`Angular2`官方推荐的开发语言，同时也可以作为使用 React、Vue、ReactNative 等框架或者类库的项目的开发语言。

一个简单的 TypeScript 文件 demo.ts, 如下代码所示：
```typescript
var book: string = "Angular 2";  // 定义了一个 string 类型的变量 book

var num: number = 123;  // 定义了一个 number 类型的变量 num

function log(msg: string): void {  // 定义了一个 函数 log, 它的参数 msg 是 string 类型的， `：void`表示这个函数没有返回值 
	console.log(msg);
}
```

## 2.安装 TypeScript:
```shell
npm install -g typescript
```

## 3.编译:

3.1 本地编译：命令行输入`tsc 文件名.ts` 既可编译成`同名`的 JavaScript 文件。
```shell
tsc demo.ts
```

demo.ts 编译后得到 demo.js 文件，如下代码所示：

```typescript	
var book = "Angular 2";
var num = 123;
function log(msg) {
	console.log(msg);
}
```

3.2 在线编译：TypeScript 官方提供[在线的实时编译](http://www.typescriptlang.org/play/index.html)。

## 4.编辑器: Visual Studio Code

微软官方为 TypeScript 提供了一款轻量级但功能强大的编辑器 —— [VS Code](https://code.visualstudio.com/)。Visual Studio Code本身就是一个`文本编辑器`，非常轻量级，搭配各种插件的话，就可以重现 Visual Studio的强大功能。

## 5.语法特性之一：类型注解

TypeScript里的`类型注解`是一种轻量级的为函数或变量添加约束的方式。 

在示例代码中里，我们希望 log 函数接收一个字符串参数。 然后尝试把 log 的调用改成传入一个数组：
```typescript
function log(msg: string) {
	return "Hello, " + msg;
}

var msg = [0, 1, 2];

log(msg);
```

TypeScript提供了静态的代码分析，它可以分析代码结构和提供的类型注解。所以上述代码在 VS Code 中会出现提示错误：
	
	Argument of type 'number[]' is not assignable to parameter of type string

## 6.语法特性之二：接口 Interface:

TypeScript的核心原则之一是对值所具有的结构进行类型检查。 它有时被称做“鸭式辨型法”或“结构性子类型化”。 

在TypeScript里，接口的作用就是为这些类型命名和为你的代码或第三方代码定义契约。

简单示例来观察接口是如何工作的：
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

类型检查器会查看函数 print()的调用。 它有一个对象参数，并且这个对象参数有一个名为a, 类型为 string 的属性。 需要注意的是，我们传入的对象参数实际上会包含很多属性，但是编译器只会检查那些必需的属性是否存在，并且其类型是否匹配。

关键字`interface`用来定义`接口`, 接口名`首字母大写`。

下面我们重写上面的例子，这次使用`接口`来描述：必须包含一个类型为 string 的属性 a。
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

## 7.语法特性之三：类 Class

### 7.1 类的定义：关键字`class`用来定义一个类，类名`首字母大写`。

传统的 JavaScript 程序没有`类(Class)`的概念, 通过基于`原型链`的继承来实现面向对象的编程。从ECMAScript 2015(ES6) 开始，JavaScript 引入了类的概念，而 TypeScript 早就实现了类的继承。


示例代码：
```typescript
class Greeter {
	
	// 定义了 string 类型的属性, 
	greeting: string;

	// 定义了类的构造函数，它参数为 string 类型
	constructor(message: string) {

		this.greeting = message;
	}

	// 定义了一个类的方法 
	greet() {
		return "Hello, " + this.greeting;
	}
}
```

上述代码声明了一个 Greeter类。这个类有3个成员：一个叫做 greeting 的属性，一个构造函数和一个 greet 方法。

我们在引用任何一个类成员的时候都用了`this`, 它表示我们访问的是类的成员。

### 7.2 实例化：关键字`new`用来创建类的一个实例对象。
```typescript
let greeter = new Greeter("world");
```

使用`new` 创建了Greeter类的一个实例。 它会调用之前定义的构造函数，创建一个 Greeter类型的新对象，并执行构造函数初始化它。

### 7.3 类的继承： 关键字`extends`表示类的继承关系

示例代码：
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
		super(name); //必须调用super()方法来执行父类的构造方法
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

与其它语言类似，TypeScript 使用 关键字`extends`来创建子类。你可以看到 Horse 和 Snake 都是 Animal 的子类，并且可以访问其属性和方法。

包含构造函数的派生类必须调用`super()`，它会执行父类的构造方法。

在子类里可以重写父类的方法。上述代码中，Snake 类 和 Horse 类都创建了 move 方法，它们重写了从 Animal 继承来的 move 方法，使得 move 方法根据不同的类而具有不同的功能。

### 7.4 类的修饰符：

7.4.1  public：默认修饰符

如果没有使用`修饰符`来修饰类的成员（属性、方法），则默认为`public`，表示我们可以自由地访问到类的这个成员。

7.4.2 private：修饰私有成员用

当成员被标记成`private`时，它就不能在声明它的类的`外部`访问。
```typescript
class Animal {
	private name: string;
	constructor(theName: string) { 
		this.name = theName; 
	}
}

new Animal("Cat").name; // Error: 'name' is private;
```

7.4.3 protected：

`protected`修饰符与`private`修饰符的行为很相似，但有一点不同，`protected`成员在`派生类`中仍然可以访问。
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

我们不能在 Person 类外使用 name ，但是我们仍然可以通过 Employee 类的实例方法访问，因为 Employee 是由 Person 派生而来的。

7.4.4 readonly：只读修饰符

你可以使用`readonly`关键字将属性设置为`只读`的。 只读属性必须在`声明`时或`构造函数`里被初始化。
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
