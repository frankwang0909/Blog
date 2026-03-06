+++
title = "Git Intro"
categories = ["tools"]
tags = ["Git"]
keywords = ["Git study notes", "Git learning guide for newbies", "Git workflow", "How to use Git to manage code in win7 system"]
description = "Git study notes, Git newbie study guide, Git workflow, how to use Git to manage code in win7 system"
date = "2016-04-03T22:43:39+08:00"
url = "/git-intro.html"
+++

`Git` is a distributed code management tool that facilitates code management when multiple people collaborate. There are two main ways to use Git to manage code in `win7` system.

## Method 1: msysgit

### Step 1: Download and install msysgit

[msysgit](https://git-for-windows.github.io) is the Windows version of Git. Download and install according to the default options. After the installation is complete, find "Git" -> "Git Bash" in the start menu. Clicking it will pop up a command line window, indicating that Git is installed successfully.


### Step 2: Set username

Enter the following command at the command line
```shell
	$ git config --global user.name "Your Name"
	$ git config --global user.email "email@example.com"
```

**Note**: Using this parameter in the `--global` parameter of the `git config`g command means that all Git repositories on your computer will use this configuration. Of course, you can also specify different user names and email addresses for a certain repository.

### Step 3: Create a repository

Choose a suitable place and create an empty directory:
```shell
	$ mkdir  gitskills  // Create a directory named gitskills
	$ cd   gitskills    // Switch gitskills directory
	$ pwd           // pwd command is used to display the current directory
    $ git init      // Initialize the Git repository, and there will be an additional .git directory in the current directory (hidden by default)
```

**Note**: To avoid inexplicable errors, please ensure that the directory name (including the parent directory) does not contain **Chinese**.

### Step 4: Add files to the repository

Create a new file in the directory you just created (such as gitskills), or copy files from other places to this directory.
```shell
	$ git add readme.md  // Add a readme.md file
$ git commit -m "Additional information when submitting" // Submit the file to the warehouse and attach relevant description text (enclosed in quotation marks)
```

**Note**: Every time you modify a file, you need to `git add` to the staging area first, and then `git commit` to the warehouse. You can `add` one file and then `commit`, or you can `add` multiple files and then `commit` together.

### Commonly used Git commands:

1. Check status: `git status`

2. Push to the remote library: `git remote add origin git@github.com: the name of the specific remote library`

3. View difference: `git diff readme.md`

4. View the history: `git log` or `git log --pretty=oneline`.

You will see a large string of hexadecimal strings similar to `commit: 8a56b4...ba53c1e50`, which is the version number `commit id`, which will be used when rolling back.

5. Version rollback: To only roll back to the previous version, you can use the command `git reset --hard HEAD^`; if there are many versions, you can first use `git log` to find the corresponding version number commit_id, and then use the command `git reset --hard commit_id` (you don’t need to write the complete version number, git will automatically find the matching one)

6. Check the command history: `git reflog`. If you regret it after rolling back and have closed Git, then use `git reflog` to find the corresponding commit so that you can go back to a future version.

7. Update the local library: Use `git pull` to update the local library before pushing, so as to avoid the remote library having changed and causing the push to fail and report an error.

8. Common errors and solutions:

Common error 1:
```shell
	fatal: remote origin already exists. 
```

Solution: Delete the remote git repository first, then add it
```shell
	git remote rm origin

git remote add origin git@github.com: the remote git repository of the project
```

## Method 2: Use GitHub for Windows provided by GiHub

The easiest way to use Git on the window platform is to use [GitHub for Windows](https://desktop.github.com/) provided by the GitHub website. The advantage is the direct graphical operation interface, no need to remember the commands at all.
