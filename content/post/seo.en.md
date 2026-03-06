+++
date = "2016-08-01T21:49:40+08:00"
title = "Seo"
description = "Basic SEO knowledge that front-end engineers should have, SEO Beginner’s Guide"
keywords = ["SEO basics", "SEO Beginner’s Guide"]
categories = ["frontend"]
tags = ["seo"]
url = "/seo.html"
+++

## What is SEO?

SEO is an acronym for Search Engine Optimization or Search Engine Optimizer. In layman's terms, SEO is to adjust and optimize the website internally and off-site to make the website meet the search engine ranking requirements and improve the keyword ranking in the search engine, thereby bringing accurate users to the website, obtaining free traffic, and generating direct sales or brand promotion.

Newbies can read [Google Search Engine Optimization (SEO) One-page Guide.pdf](https://support.google.com/webmasters/answer/35291?hl=zh-Hans).

If you want to learn more, you can refer to [Google Search Engine Optimization Starter Guide](http://static.googleusercontent.com/media/www.google.com/en/us/intl/zh-cn/webmasters/docs/search-engine-optimization-starter-guide-zh-cn.pdf) (Need to climb over the wall), [If you can’t climb over, you can click here](http://frankwang0909.github.io/posts/search-engine-optimization-starter-guide-zh-cn.pdf).

## SEO knowledge that front-end engineers should master

At present, many companies have full-time positions for SEO, and front-end engineers are not specialized in SEO optimization and promotion. They do not need to become SEO experts, but they should master the following basic SEO knowledge.

### 1. Optimization of structural layout

1. Flatten the structure.

The hierarchical structure of the website should not exceed three levels. In this way, search engines or users can reach any internal page in the website by clicking and jumping 3 times.

2. Optimize navigation.

Set the main navigation, secondary navigation, category navigation, breadcrumb navigation, pagination page number, etc. of the page to facilitate users to jump to the page they want to visit.


### 2. Semanticization of tags

Search engine crawlers will rely on tags to determine the context and weight of each keyword. Therefore, the correct use of semantic tags will help search engines crawl and include web content.

1. Anchor link `<a>` tag:

1) Add the attribute **title="text description of the link"** to add a description of the link, especially the link pointing to this site.

2) Add the attribute **rel="no follow"**. For links pointing to non-sites, adding this attribute tells the crawler that the page does not need to be tracked.

2. Use `<h1>` for the main text title and `<h2>` for the subtitle. Do not abuse titles.

3. Use `<p>` for the text content, and `<br>` for line breaks within the text. Do not abuse `<br>` for line breaks in other places, but set them through CSS styles.

4. Picture `<img> `Add attribute **alt="Text annotation of the picture"**.

5. Use `<table>` for tables and `<caption>` for table titles.

6. Use `<ol>` for ordered lists, `<ul>` for unordered lists, and `< dl>` for definition lists.

7. Emphasis tag: `<strong>` means emphasis. It can be used to highlight keywords and has greater weight. `<em>` also expresses emphasis and has a slightly lower weight than strong. Although the `<b>` tag also has a bold effect, it does not have an emphasis effect, so it does not increase the weight of the text within the tag.

8. Reduce the use of `<iframe>`. iframes block page loading and delay triggering the window.onload event, giving users the impression that the webpage is very slow.

9. Put the HTML code of important content at the front, and then control the position through CSS properties.
