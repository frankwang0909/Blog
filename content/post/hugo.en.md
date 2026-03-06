+++
keywords = ["Hugo", "Build a website", "static blog", "GitHub"]
description = "Use Hugo to quickly build a personal static blog and host it on GitHub"
categories = ["tools"]
tags = ["Hugo", "GitHub"]
date = "2017-04-03T20:49:23+08:00"
title = "Hugo"
url = "/build-blog-with-hugo.html"

+++

Recently, I had a sudden impulse to start my blog again. So, I found that Hugo is more useful than the Jekyll I used before. This article is a personal record of building a personal blog with reference to [Hugo official website](https://gohugo.io/overview/quickstart/).

## Step 1. Install Hugo Download and install Hugo

Download address: [https://github.com/spf13/hugo/releases](https://github.com/spf13/hugo/releases).
According to your operating system, download the corresponding installation package. My operating system is `Win7 64bit`, and I selected `hugo_0.19_Windows-64bit.zip`.

After the download is complete, the unzipped folder contains the following 3 files:

hugo_0.19_windows_amd64.exe
	LICENSE.md
	README.md

Rename `hugo_0.19_windows_amd64.exe` to `hugo.exe`. Add a new file directory named `hugo` to your software installation disk, and create a `bin` subdirectory in it. Then put `hugo.exe` in the `hugo\bin` directory. Then add the path to the `bin` directory to the `system environment variables`.

After completing the above steps, open the command line input
```shell
	hugo help
```
If you get the following information, the installation is successful.
```shell
	hugo is the main command, used to build your Hugo site.

	Hugo is a Fast and Flexible Static Site Generator
	built with love by spf13 and friends in Go.

	Complete documentation is available at http://gohugo.io/.
```

## Step 2. Create a Hugo site named blog

I want to create the site under the E drive, so I first change the directory
```shell
	cd e:
	e:
```

Then enter the command:
```shell
	hugo new site blog 
```

You will get the following message indicating that the creation was successful:


Congratulations! Your new Hugo site is created in E:\blog.
	Just a few more steps and you're ready to go:
	1. Download a theme into the same-named folder.
	Choose a theme from https://themes.gohugo.io/, or
	create your own with the "hugo new theme <THEMENAME>" command.
	2. Perhaps you want to add some content. You can add single files
	with "hugo new <SECTIONNAME>\<FILENAME>.<FORMAT>".
	3. Start the built-in live server via "hugo server".
	Visit https://gohugo.io/ for quickstart guide and full documentation.


Entering this directory, you can see that 5 directories and a configuration file config.toml are automatically generated.

|-- archetypes
	|-- content #Directory to store content
	|-- data
	|-- layouts
	|-- static #Storage static resources (pictures, css, js)
	|-- themes #Storage themes
	|-- config.toml #Configuration file

## Step 3. Add content

Switch to this directory and enter the following command. The `post` directory will be created in the `content` directory, and a file named `test.md` will be created in the `post` directory.

```shell
	cd blog
	hugo new post/test.md
```

Prompt file created successfully:

```shell
	E:\blog\content\post\test.md created
```

Open the file `test.md` with a text editor
You can see the following:
```markdown
	+++
	date = "2017-01-02T17:45:06+08:00"  # The time the file was created
	title = "test"                      # file title
	draft = true                        # Is it a draft?
	+++
```

The above content is automatically created content related to the article. You can also add the following content between the two `+++`:
```markdown
	image = "hugo.png"            # Specify picture.
	category = "test"             # Article category
	tags = ["Hugo", "intro"]      # Tag categories for articles.
	url = "new_start"             # The relative url address when accessing the article, which defaults to the file name.
```

For more settings, please refer to [Official Documentation](https://gohugo.io/content/front-matter/).

In the future, this is how you create a `markdown` file when writing blog posts, and then compile it into a static html file through `Hugo`.

## Step 4. Add theme

The official website provides a variety of themes to choose from, which can be found at [https://themes.gohugo.io/](https://themes.gohugo.io/).

After you find the theme you want, switch to the `themes` directory (this directory can store multiple different themes).

```shell
	cd themes
```

Because you need to use Git to download themes, as well as version management and code push. You need to download and install [Git](https://git-for-windows.github.io/) in advance. For how to install and use Git, you can refer to my previous article: [Git Learning Notes](http://frankwang0909.github.io/git-intro/).

Download the selected theme to the `themes` directory.
```shell
	git clone https://github.com/dim0627/hugo-icarus-theme.git
```


## Step 5. Start the service and preview locally

First, return to the `blog` directory from the `themes` directory, and then start the service.
```shell
	cd ..
    hugo server --theme=hugo-icarus-theme --buildDrafts
```

Open http://localhost:1313/ in your browser


## Step 6. Modify the configuration file config.toml

```markdown
	languageCode = "zh-cn"
	title = "Frank Wang's Coding World"
	baseurl = "http://frankwang0909.github.io/"  

	[Params]
		Author ="Frank Wang"
```

## Step 7. Generate website

7. 1 Change article `draft` (draft) status:

hugo undraft content/post/*.md

7. 2 Start `hugo` and generate the release file in the `public` directory.

```shell
	hugo --theme=even
```

## Step 8. Host to GitHub Pages

8. 1 Use `Git` for version management
```shell
	git init
	echo "/public/" >> .gitignore
	echo "/themes/" >> .gitignore
	git add --all
	git commit -m "Initial commit"
```

8. 2 Create a `Git` remote repository:

Log in to your `GitHub`. Create a new repository named `Github user.github.io`, for example, mine is `frankwang0909.github.io`.

8. 3. Add the `Git` remote repository and submit the code.
```shell
	cd public
	git init
	git remote add origin git@github.com:frankwang0909/frankwang0909.github.io.git

	git add --all
	git commit -m "blog added"
	git push -u origin master
```

8. 4 If there are any content changes in the future, please submit the code.

```shell
	(cd ..; hugo --theme=hugo_theme_robust)
	git add --all
	git commit -m "<some change message>"
	git push -u origin master
```
