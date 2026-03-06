+++
date = "2016-06-05T22:05:46+08:00"
title = "Markdown Intro"
description = "Markdown study notes, use Markdown to write blogs"
keywords = ["Markdown", "blog"]
categories = ["tools"]
tags = ["Markdown"]
url ="/markdonw-notes.html"
+++

## Definition:

Introduction on [Wikipedia](https://zh.wikipedia.org/zh-cn/Markdown):

Markdown is a lightweight markup language founded by John Gruber. It allows people to "write documents in a plain text format that is easy to read and write, and then convert them into valid XHTML (or HTML) documents." This language incorporates many of the features of plain text markup already found in email.

Markdown is also a Perl script written by Gruber: Markdown.pl. It converts content written in markdown syntax into valid, well-structured XHTML or HTML content, replacing left angle brackets ('<') and ampersands with their respective character entity references. It can be used as a standalone script, as a plug-in for Blosxom and Movable Type or as a text filter for BBEdit.


##Use:

From the introduction in Wikipedia, markdown is a markup language. Its concise syntax replaces typesetting, allowing us to concentrate on coding, and uses "markup" syntax to replace common typesetting formats. For example, the content of my current blog is written directly in Markdown. There is no need to consider complicated typesetting, you only need to remember a few simple and commonly used syntaxes, and then you can easily convert it into an HTML file and turn it into a web page that can be parsed by the browser.
If you have your own independent blog and just want to code without writing complex HTML and CSS codes, Markdown is undoubtedly a good choice.

## The most basic syntax:

1. Title:

If a piece of text is defined as a title, just add a `#` sign before the text. One `#` represents a first-level heading; `##` represents a second-level heading; and so on, for a total of 6 levels of headings. Add a space after the `#` sign.


2. Quote code:

1) To quote the entire code, only a space or a Tab key is required to completely retain the code indentation format.
	2) Introduce the code snippet in one line. Surround the code with backticks (` `) above the tab key.

3. Link:

Use square brackets `[]` to enclose the text to be added as a hyperlink, and use round brackets `()` to enclose the url. It is written as follows:

`[Markdown Wikipedia English version](https://en.wikipedia.org/wiki/Markdown)`

The effect is shown on the right: [Markdown Wikipedia English version](https://en.wikipedia.org/wiki/Markdown)


4. Pictures:

The syntax for inserting a link is very similar to that of inserting a picture, the only difference is the `!` symbol. The picture is: `![Text description](url). `


5. Dividing line:

Use three or more `asterisks`, `minus signs`, and `underline` to create a dividing line, and there should be no other things in the line. You can insert spaces between asterisks or minus signs


6. List:

1) Unordered list Unordered list uses `asterisk`, `plus sign` or `minus sign` as list mark;
	2) For an ordered list, add `1.` `2.` `3.` directly before the text. A space of one character should be added between the symbol and the text.

7. Bold and italics:

Enclosing a block of text with two `*` is bold syntax, and using one `*` to enclose a block of text is italic syntax.

**This is bold text**

*This is italic style*

8. Spaces and line breaks:

`A single carriage return` is treated as a space; `continuous carriage returns` can be segmented.

9. Block quotes `Blockquotes`

Markdown markup block quotation uses a quotation method similar to `>` used in email. If you're familiar with introductions in email messages, you know how to create a block quote in a Markdown file. It will look like you break the lines yourself and then add `> at the beginning of each line:`

## Related links:

1. [Quick Start Guide](http://wowubuntu.com/markdown/basic.html)

2. [Markdown official website](http://daringfireball.net/projects/markdown/)
