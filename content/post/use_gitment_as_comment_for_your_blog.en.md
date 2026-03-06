+++
categories = ["tools"]
tags = ["Gitment"]
date = "2017-06-24T17:04:42+08:00"
title = "Use Gitment As Comment For Your Blog"
keywords = ["Gitment", "Blog comment system", "GitHub Issues"]
description = "Gitment is a comment system built using GitHub Issues. This article teaches you how to use Gitment as a comment system for your own blog"
url = "/use_gitment_as_comment_system_for_your_blog.html"
+++

[Gitment](https://github.com/imsun/gitment) is a comment system built using GitHub Issues. This article teaches you how to use Gitment as a comment system for your own blog.

## Let’s briefly introduce the advantages and disadvantages:

### 1. Advantages:

Gitment supports direct introduction on the front end without any back-end code. You can log in, view, comment, like and other operations on the page. It also has complete Markdown / GFM and code highlighting support, which is especially suitable for various static blogs or project pages based on GitHub Pages.

### 2. Disadvantages:

Comments can only be made using a GitHub account. Each article needs to be manually logged in and initialized with a GitHub account so that other users can comment.



## Usage:

### Step 1: Register OAuth Application

Register a new [OAuth Application](https://github.com/settings/applications/new) on GitHub. You can fill in the first three items as you like, but make sure the last `Authorization callback URL` is your website domain name (such as http://www.wangxingfeng.com).

After successful registration, you will get a client ID and a client secret, which will be used to instantiate Gitment later.


### Step 2: Introduce Gitment’s static resource files into the page

```html
<link rel="stylesheet" href="https://imsun.github.io/gitment/style/default.css">
<script src="https://imsun.github.io/gitment/dist/gitment.browser.js"></script>
```
Of course, you can also choose to download these two static resource files locally, and then put them in the corresponding static resource directory of your site.


### Step 3: Instantiate Gitment

1. Add a DOM node to the page where you need to use the comment system (generally, find the template page of your article) to place the content of the comment box area.

```html
<div id="comment"></div>
```

2. Add the following configuration script to this page:

```javascript

var gitment = new Gitment({
id: 'Page ID',
owner: 'your GitHub ID',
repo: 'repo where comments are stored',
  oauth: {
client_id: 'your client ID',
client_secret: 'your client secret',
  },
})
gitment.render('comment')

```

Notice:

1. The parameter of `gitment.render()` is the id name of your comment area div;

2. If the page ID is not written, it defaults to location.href.


### Step 4: Initialize the comment function

After the third step, you need to deploy your website online. If nothing went wrong in the previous three steps, you should be able to see the comment box. It is not possible to comment at this time.

Click `Login with GitHub` on the right side of the comment box, log in with your GitHub, and then click the blue `Initialize Comments` button in the middle to initialize the comment function of the page.

Now, visitors to your page can log in using their GitHub account to comment. The only drawback is that the comment box on each page needs to be initialized manually.
