+++
keywords = ["CSS preprocessor", "Less","CSS Preprocessors"]
description = "Less, CSS Preprocessors, CSS preprocessors provide convenience for writing CSS such as variables, mixins, functions, rule nesting, and color processing."
categories = ["frontend"]
tags = ["CSS"]
title = "Css Prep"
url ="/less.html"
date = "2017-04-23T16:28:38+08:00"

+++

## 1.CSS

`CSS` Cascading Style Sheets (Cascading Style Sheets) is a computer language used to express document styles such as HTML (an application of Standard Generalized Markup Language) or XML (a subset of Standard Generalized Markup Language).

Because `CSS` does not have its own programming syntax such as variables, constants, conditional statements, functions, etc. as ordinary programming languages, but only simple attribute descriptions line by line, it is quite troublesome to write, and the code is difficult to organize and maintain.

## 2.DRY

`DRY`, or Don't Repeat Yourself, is a programming philosophy familiar to programmers, and good programmers usually write code following this specification.
`DRY` can significantly improve the maintainability of the code. For example, when a parameter needs to be changed, only one or a few places need to be changed.

## 3.CSS preprocessor

Pure `CSS` code does not have concepts such as variables, nesting, conditions, etc., and it is difficult to achieve DRY, which causes programmers a headache. Therefore, some programmers try to add some programming features to `CSS`, making it possible to use variables, simple program logic, and functions in `CSS`.

Currently, there are three most commonly used CSS preprocessors: `Less`, `SASS`, and `Stylus`.
It can be seen from [GitHub](https://github.com/showcases/css-preprocessors) that `Less` is the most popular `CSS` preprocessor.
![](/images/2017042301.jpg)

## 3.Less

### 3.1 Installation
Because `Less` is written in `JavaScript` language, it can run in the `NodeJS` environment on the server side. Therefore, the simplest installation method is to use `npm install`.

npm install -g less # -g means global installation

### 3.2 Compilation
The suffix of `Less` files is `.less`. Browsers cannot directly recognize `.less` files and need to be compiled into `CSS` style files ending in `.css`.
Assuming you already have a `less` file `demo.less`, execute the following command on the command line to compile and generate `demo.css`.

lessc demo.less demo.css

`lessc` is the command of Less. The first parameter demo.less specifies the name of the source file that needs to be compiled. The second parameter demo.css is the name of the compiled CSS file.

If you need to compile it into a compressed CSS file, you can install and download a plug-in officially provided by Less globally [clean-css plugin](https://github.com/less/less-plugin-clean-css).

npm install -g less-plugin-clean-css

Then, enter the following command on the command line:

lessc --clean-css demo.less demo.min.css #One more parameter --clean-css

### 3.3 Basic syntax

#### 3.3.1 Variables

Less variable names start with the ` @ ` symbol, for example:

@nice-blue: #5B83AD;
	@light-blue: @nice-blue + #111;

#header {
	  color: @light-blue;
	}

After compilation, you get the following code:

#header {
	  color: #6c94be;
	}

Note: Less variables are essentially constants and can only be defined once.

#### 3.3.2 Mixins
A way to introduce ("mix") a series of properties from one ruleset into another.

For example, first define a rule

.bordered {
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}

If you want to use this rule elsewhere, you can do this:

#menu a {
	  color: #111;
	  .bordered;
	}

.post a {
	  color: red;
	  .bordered;
	}

The compilation results are as follows:

.bordered {
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}
	#menu a {
	  color: #111;
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}
	.post a {
	  color: red;
	  border-top: dotted 1px black;
	  border-bottom: solid 2px black;
	}


#### 3.3.3 Nesting
Nest style rules according to HTML structure.

#header {
	  color: black;
	  .navigation {
	    font-size: 12px;
	  }
	  .logo {
	    width: 300px;
	  }
	}

Compiled CSS style file:

#header {
	  color: black;
	}
	#header .navigation {
	  font-size: 12px;
	}
	#header .logo {
	  width: 300px;
	}

You can also combine pseudo-classes for nesting. For example, the "clear float" style can be written like this:

.clearfix {
	  display: block;
	  zoom: 1;

&:after {
	    content: " ";
	    display: block;
	    font-size: 0;
	    height: 0;
	    clear: both;
	    visibility: hidden;
	  }
	}

The symbol ` & ` in the above code represents the parent selector of the current selector.

The result after compilation is as follows:

.clearfix {
	  display: block;
	  zoom: 1;
	}
	.clearfix:after {
	  content: " ";
	  display: block;
	  font-size: 0;
	  height: 0;
	  clear: both;
	  visibility: hidden;
	}


#### 3.3.4 Media queries and nesting

Media query (Media query) can be nested in the selector. When compiling, the selector will be automatically copied into the media query body. Media queries can also be nested in media query rules.

.screen-color {
	  @media screen {
	    color: green;
	    @media (min-width: 768px) {
	      color: red;
	    }
	  }
	  @mediatv{
	    color: black;
	  }
	}

Compilation result:

@media screen {
	  .screen-color {
	    color: green;
	  }
	}
	@media screen and (min-width: 768px) {
	  .screen-color {
	    color: red;
	  }
	}
	@mediatv{
	  .screen-color {
	    color: black;
	  }
	}


#### 3.3.5 Operation
In Less, numerical values, colors, and variables can be added, subtracted, multiplied, and divided.

@color: #224488 / 2; //results in #112244
	background-color: #112244 + #111; // result is #223355

@base: 5%;
	@filler: @base * 2; // result is 10%
	@other: @base + @filler; // result is 15%

#### 3.3.6 Function

`Less` provides a number of functions for converting colors, manipulating strings, and performing arithmetic operations. For details, please refer to [Less Function Reference](http://lesscss.org/functions/)

These functions are very simple to use.

@base: #f04615;
	@width: 0.5;

.class {
	  width: percentage(@width);
	  color: saturate(@base, 5%);
	  background-color: spin(lighten(@base, 25%), 8);
	}

In the above code, we use the function `percentage()` to convert 0.5 to 50%, then use the function `saturate()` to increase the saturation of the base color value by 5%, then use the function lighten() to increase the brightness of the background color by 25%, and finally use the function spin() to increase the hue value by 8. After compilation:

.class {
	  width: 50%;
	  color: #f6430f;
	  background-color: #f8b38d;
	}

### 3.5 official website
For more content, you can visit [http://lesscss.org/](http://lesscss.org/)
