+++
title = "Sublimetext Intro"
banner = "/images/20160513banner.jpg"
description = "Sublime Text study notes, Sublime Text beginner’s guide, front-end engineer’s editing tool"
keywords = ["Sublime Text", "An editing tool for front-end engineers"]
categories = ["tools"]
tags = ["Sublime Text"]
date = "2016-05-13T00:14:00+08:00"
url = "/sublimetext-notes.html"
+++

Since changing the main code editor to [Sublime Text](https://www.sublimetext.com/), the efficiency of writing code has been significantly higher. Recently, I started trying to recommend this editor to my friends.

## 1. Advantages of Sublime Text

1. Cross-platform;

2. Lightweight and scalable: There are a large number of plug-ins that users can choose to install (the `Emmet` plug-in is recommended first).

3. Support syntax highlighting for almost all mainstream programming languages;

4. Code automatic completion, supporting code snippets (Code Snippet);

5. `minimap` in the upper right corner: used to view annotations, quickly drag, and quickly locate;

6. Quickly jump to different files/methods/functions: supports fuzzy matching;

7. Quickly switch between `Tab` and `Space`;

8. Format code;

## 2. Install Sublime Text

1. Download the installation package:

Sublime Text official website address: [https://www.sublimetext.com/](https://www.sublimetext.com/) Select the corresponding installation package to download and install according to your system. The current stable version is `Sublime Text 3`;

2. Install Package Control:

Before downloading plug-ins, you need to install `Package Control`, which is a control component used to manage and download plug-ins. `Package Control` official website installation address: [https://packagecontrol.io/installation](https://packagecontrol.io/installation)

![](/images/2016051301.jpg)

1) Use the shortcut key `ctrl+`` or the `View` > `Show Console` menu to open the console, then press Enter to let it install.

![](/images/2016051302.jpg)

2) Select and copy the corresponding version code according to the version of Sublime Text;

![](/images/2016051303.jpg)

3) Paste it into the console input box and press the `Enter key`, and the plug-in management package will enter the downloading and installation state (it may take a while);

3. Customize the installation of various plug-ins:

At the Package Control official website address: [https://packagecontrol.io/](https://packagecontrol.io/) you can see various plug-ins and their download rankings. If you find the one you are interested in, download it and try it out.

The download and installation method is as follows: (windows platform)

1) Press `Ctrl+Shift+P` to bring up the command panel, enter `install`, bring up the `Install Package` option and press Enter, a screen like this will appear,

![](/images/2016051305.jpg)

2) Then enter the name of the plug-in you want to download, such as: `HTML Extended`

![](/images/2016051306.jpg)

3) After the download and installation is completed, a file similar to this will pop up, indicating that the plug-in has been successfully installed.

![](/images/2016051307.jpg)

Or a prompt for successful installation in the lower left corner:

![](/images/2016051308.jpg)


## 3. Recommend several useful plug-ins:

1. Emmet: Directly generate a large piece of code through simple commands.

2. ConvertToUTF8 (convert to utf-8 format): By default, Chinese in gbk encoding format will become garbled characters. This plug-in can implement automatic conversion.

3. JsFormat: Format js code. It can restore the js code that has been compressed and difficult to read on other people's websites.

4. HTMLBeautify: Format HTML.

5. Hasher: symbol escape.

6. TrailingSpaces: extra space mark.

7. SideBarEnhancementS: Sidebar enhancements.

8. ChineseLocalization: Chinese plug-in.

## 4. Commonly used shortcut keys (under Windows platform):

1. `Ctrl + Shift + N`Create a new window;`Ctrl + W`Close the window.

2. `Ctrl + N` creates a new label; `Ctrl + W` closes the current label; `Ctrl + Shift + T` restores the just-closed label.

3. `Alt + Shift + 2` split the screen left and right; `Alt + Shift + 8` split the screen up and down; `Alt + Shift + 5` split the screen up, down, left and right into four screens. `Ctrl + Numeric Keys` jumps to the specified screen; `Ctrl + Shift + Numeric Keys` moves the current screen to the specified screen.

`ctrl+1` changes back to one screen display.

4. `F11` switches to normal full screen; `Shift + F11` switches to interference-free full screen.

5. `Ctrl + P` will list all currently opened files, click on a file to jump quickly;

6. `Ctrl + R` For md files, the outline will be listed.

![](/images/2016051309.jpg)

7. `Ctrl + F` brings up the search box to search; `Ctrl + H` replaces

8. `Ctrl + J` merges the selected areas into one line; `Ctrl + Shift + L` can scatter the currently selected areas and edit them simultaneously:

9. Multi-line cursor (can edit multiple lines of code at the same time): `Ctrl + D` selects the word where the current cursor is located and highlights all occurrences of the word, and `Ctrl + D` again selects the next position where the word appears. In the process of multiple word selection, use `Ctrl + K` to skip, use `Ctrl + U` to go back, and use `Esc` to exit multiple editing.

10. `Ctrl + Enter` adds a new line below the current line and jumps to that line; `Ctrl + Shift + Enter` adds a new line above the current line and jumps to that line.

11. `Ctrl + E` automatically generates code snippets (after installing the Emmet plug-in).

12. `Ctrl + shift + D`Copy the contents of the current line to the next line and jump to that line.
