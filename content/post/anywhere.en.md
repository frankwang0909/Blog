+++
title = "Anywhere"
keywords = ["Node server", "anywhere", "npm", "Mobile device debugging"]
description = "Quickly start the Node server, how to test static files on mobile devices, front-end engineers must have the skills to turn your current directory into the root directory of a static file server anytime, anywhere, Running static file server anywhere."
categories = ["node"]
tags = ["server"]
date = "2017-04-04T17:41:35+08:00"
url = "/anywhere-npm.html"
+++

## How to test static files on mobile devices?

Now that mobile is given priority, after front-end engineers write static pages, they usually need to test the effects on different devices to see if there are any compatibility issues. Google Chrome has a debugging function that simulates a mobile phone. Generally, we use Google to debug it first. But after all, it is a simulation. To be on the safe side, it still needs to be tested with a real machine.

But how to put static html files on mobile phones for debugging? Is it possible to copy the file and put it on a different phone? Apparently not.

A `npm` module `anywhere` of NodeJS can quickly turn your current directory into the root directory of a static file server.


## Installation and use of `anywhere`

First, install Node. For specific operations, please see [Node’s official website](https://nodejs.org). Install the easy way.

Second, install `anywhere`. Enter at the command line

npm install anywhere -g

`npm install + module name` is a fixed way of downloading third-party packages written by others from the NPM server.

`-g` means global installation, and the anywhere module can be used in any department of the computer.

Start the service:

Switch to the root directory of the project on the command line and enter `anywhere`. After the service is started, your default browser will automatically open, http://192.168.31.192:8000/.

At this time, if you want to test the index.html page on your mobile phone, you only need to visit `http://192.168.31.192:8000/index.html` on your mobile phone to see the effect.

Of course, there is a premise here, that is, your mobile phone and computer are in the same LAN.
 