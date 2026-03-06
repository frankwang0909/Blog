+++
categories = ["Node", "tools"]
tags = ["Node","nvm"]
date = "2017-07-20T07:54:41+08:00"
title = "NVM for Windows"
keywords = ["Node.js", "version manager", "nvm", "Windows"]
description = "nvm-windows is a Node.js version manager written in Go for Windows."
url = "/nvm_for_window.html"
+++




## Introduction

nvm-windows is a Node.js version manager written in Go for Windows. [GitHub repository](https://github.com/coreybutler/nvm-windows)

## Download and Install

[Download from releases](https://github.com/coreybutler/nvm-windows/releases)


## Common Commands

1. Install a specific Node.js version:

nvm install <version>

Example:

nvm install 6.2.0

You should see output indicating Node.js `6.2.0` and the matching `npm` version are being downloaded and installed.

Downloading node.js version 6.2.0 (64-bit)...
	Complete
	Creating C:\Users\Administrator\AppData\Roaming\nvm\temp

Downloading npm version 3.8.9...
	Complete
	Installing npm v3.8.9...
	Installation complete.
	If you want to use this version, type nvm use 6.2.0


2. Use a specific Node.js version:

nvm use <version>

Example:

nvm use 6.2.0

After switching versions, the output looks like:

Now using node v6.2.0 (64-bit)

Verify active versions:

node -v

npm -v

3. List all installed Node.js versions

nvm list

Example output (`*` indicates the active version):

8.1.4
    *6.2.0 (Currently using 64-bit executable)
	 6.1.0
	 4.6.0
	 4.4.7

With the `available` flag, you can list downloadable Node.js versions:

nvm list available

Example output:

| CURRENT | LTS | OLD STABLE | OLD UNSTABLE |
	|--------------|--------------|--------------|--------------|
	| 8.1.4 | 6.11.1 | 0.12.18 | 0.11.16 |
	| 8.1.3 | 6.11.0 | 0.12.17 | 0.11.15 |
	| 8.1.2 | 6.10.3 | 0.12.16 | 0.11.14 |
	| 8.1.1 | 6.10.2 | 0.12.15 | 0.11.13 |
	| 8.1.0 | 6.10.1 | 0.12.14 | 0.11.12 |
	| 8.0.0 | 6.10.0 | 0.12.13 | 0.11.11 |
	| 7.10.1 | 6.9.5 | 0.12.12 | 0.11.10 |
	| 7.10.0 | 6.9.4 | 0.12.11 | 0.11.9 |
	| 7.9.0 | 6.9.3 | 0.12.10 | 0.11.8 |
	| 7.8.0 | 6.9.2 | 0.12.9 | 0.11.7 |
	| 7.7.4 | 6.9.1 | 0.12.8 | 0.11.6 |
	| 7.7.3 | 6.9.0 | 0.12.7 | 0.11.5 |
	| 7.7.2 | 4.8.4 | 0.12.6 | 0.11.4 |
	| 7.7.1 | 4.8.3 | 0.12.5 | 0.11.3 |
	| 7.7.0 | 4.8.2 | 0.12.4 | 0.11.2 |
	| 7.6.0 | 4.8.1 | 0.12.3 | 0.11.1 |
	| 7.5.0 | 4.8.0 | 0.12.2 | 0.11.0 |
	| 7.4.0 | 4.7.3 | 0.12.1 | 0.9.12 |
	| 7.3.0 | 4.7.2 | 0.12.0 | 0.9.11 |
	| 7.2.1 | 4.7.1 | 0.10.48 | 0.9.10 |


4. Uninstall a specific Node.js version:

nvm uninstall <version>

Example:

nvm uninstall 6.1.0

Example output:

Uninstalling node v6.1.0... done

Run `nvm list` again to verify that `6.1.0` was removed.
	
8.1.4
    *6.2.0 (Currently using 64-bit executable)
	 4.6.0
	 4.4.7

What if you try to uninstall the currently active version?
	
nvm uninstall 6.2.0

You will get an error because the active version cannot be removed.

Uninstalling node v6.2.0...Error removing node v6.2.0
	Manually remove C:\Users\Administrator\AppData\Roaming\nvm\v6.2.0.

If you run `nvm list`, you will see that `6.2.0` is still present, but no version is currently active.
	
8.1.4
	6.2.0
	4.6.0
	4.4.7

Running `node -v` now fails with:

'node' is not recognized as an internal or external command, operable program or batch file.
