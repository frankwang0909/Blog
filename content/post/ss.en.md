+++
date = "2017-07-09T11:37:11+08:00"
categories = ["tools"]
tags = ["Shadowsocks"]
title = "Ss"
keywords = ["Google Cloud Platform", "Shadowsocks", "Scientific Internet"]
description = "In order to surf the Internet more conveniently and scientifically, use Google Cloud Platform free trial service to build a Shadowsocks ladder"
url = "/ss.html"

+++

In view of the fact that scientific Internet access has become more and more inconvenient recently, many previously strong VPNs have been forced to stop their services, so they have to do it themselves and build a ladder. After searching for information online, I accidentally discovered that [Google Cloud Platform](https://cloud.google.com/) has a free trial service (in fact, Amazon Cloud also has a one-year free trial). New users will be given $300 for registration, which is valid for one year and can be used to build a ladder for fun.

There probably aren't many people doing this right now, because there are at least two thresholds. First, Google's services are basically blocked in China, so you must first be able to circumvent the wall and register a Google account before you can log in to Google Cloud. Second, domestic users must have a dual-currency or multi-currency credit card to pass verification.

Here is my process for building a ladder:

### 1. Register and log in:

First use the free blue light to go over the wall [Google Cloud](https://cloud.google.com/), click the blue "TRY IT FREE" button, you need to log in with a Google account, and then fill in some personal information. During the process, you need to bind a real credit card. They may also send you an email asking you to upload photos of your ID and credit card for identity verification. After successful verification, a fee of US$1 will be withheld to verify the validity of the card, and it will be automatically returned later.

### 2. Create project:

You can fill in the project name as you like.

### 3. Create a VM instance: Computing Engine --> VM instance.

1) Region: You can select nodes in Asia;

2) Machine type: I chose the lowest configuration, micro.

3) Boot disk: I chose CentOS7 operating system

4) Network: Remember to create a new static IP address, which needs to be bound to the instance later.

### 4. Bind external IP address:

Network --> Bind External IP Address --> Reserve Static Address (Static IP addresses not attached to an instance or load balancer will be billed hourly!!!)

### 5. Firewall settings:

Since the default firewall has too many restrictions, SS, etc. may not be able to be used, so we open the corresponding ports in the firewall.

Network --> Firewall Rules --> New Firewall Rule --> Source filtering selection "Allow traffic from any source" --> Set protocol and port: "tcp: your port number"

### 6. Install and configure SS on the server:

1) Use Google Cloud’s built-in SSH tool to connect to the server.

2) Enter the command: `sudo -i` to obtain `root` permissions;

3) Then enter `yum install -y emacs python python-pip` to install the Emacs editor and Python (the editor is used to edit the SS configuration file, and Python is used to run SS).

4) Wait for a while and then the installation is completed. Then enter the command `pip install shadowsocks` to install SS;

5) Enter the command `emacs /etc/ss.json` to open the editor, and open a configuration file named `ss.json` and save it in the `/etc/` directory. The following is the official default configuration of SS:
```json
	{
"server":"Your server static IP address",
"server_port": port number, // The port number needs to be consistent with the one set in step 5
"password":"your password",
	    "timeout":600,
	    "method":"rc4-md5", 
	    "auth": true
	}
```

6) After the configuration is completed, press `ctrl + x` and then `ctrl + s` to save the file, then press `ctrl + x` and then `ctrl + c` to exit the editor.

7) Finally enter the command `ssserver -c /etc/ss.json -d start` to start the Shadowsocks server.

To stop the SS server (for example, if you need to change the configuration file), enter `ssserver -d stop`.

To enable the SS service to run in the background, enter `ssserver -p your port number -k your password -m rc4-md5 --user nobody -d start`. So far, the server-side configuration has been completed.


### 6.Win7 is configuring client SS:

1) Download and unzip [ss client](https://github.com/shadowsocks/shadowsocks-windows/releases);

2) Run `Shadowsocks.exe`, the icon will appear in the lower right corner of the desktop.

3) Right-click the icon --> Click "System Proxy" --> Select "PAC Mode" for "System Proxy Mode" --> Select "Server" --> "Edit Server" --> Fill in the server address, port number, password, encryption method and other information --> OK.

At this point, you can enjoy the real Internet.

### 7. Android mobile SS client configuration:

1) Download “Shadow Shuttle”

2) Fill in the corresponding server address, port number, password, encryption method and other information.
