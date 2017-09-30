+++
date = "2017-07-09T11:37:11+08:00"
categories = ["tools"]
tags = ["Shadowsocks"]
title = "撸了Google Cloud，自建了个梯子"
keywords = ["Google Cloud Platform", "Shadowsocks", "科学上网"]
description = "为了更方便地科学上网，使用 Google Cloud Platform 免费试用服务，搭建一个 Shadowsocks 梯子"
url = "/ss.html"

+++

鉴于最近科学上网变得越来越不方便了，不少之前坚挺的 VPN 都被迫停止服务了，只好自己动手，搭个梯子。网上找找资料，意外发现了[谷歌的云服务 (Google Cloud Platform)](https://cloud.google.com/)有免费试用服务（其实亚马逊云也有一年的免费试用）。 新用户注册赠送300刀，一年有效期，完全可以用来搭建个梯子玩玩。

目前撸这个的人应该不多，因为至少有两个门槛。第一，谷歌的服务在国内基本被墙了，所以必须得先能翻墙，注册了 Google 账号，才能登录 Google Cloud。第二，国内用户必须得有双币或者多币种的信用卡才能通过验证。

以下是我搭建梯子的流程：

### 1.注册登录：

先用免费的蓝灯翻墙上[谷歌云](https://cloud.google.com/)，点击那个蓝色的 "TRY IT FREE"  按钮，需要用谷歌账号登录，然后填写一些个人信息，过程中需要绑定真实的信用卡。还有可能会发邮件给你，让你上传证件以及信用卡的照片用于身份认证。验证成功后会预扣费1美元用于验证卡的有效性，稍后它会自动返回。

### 2.创建项目：

项目名称什么的可以随便填。

### 3.创建VM实例： 计算引擎 --> VM实例。 

1）地区：可以选择亚洲的节点；

2）机器类型：选择了最低配的，微型。

3）启动磁盘：我选了CentOS7的操作系统

4）网络：记得要新建静态IP地址，后面需要绑定到实例。

### 4.绑定外部IP地址：

网络 --> 绑定外部IP地址 --> 保留静态地址 （未附加到实例或负载平衡器的静态 IP 地址将按小时计费!!!）

### 5.防火墙设置：

由于默认的防火墙限制太多，SS等可能用不了，所以我们把防火墙相应端口开一下。

网络 --> 防火墙规则--> 新建防火墙规则 --> 来源过滤选择 “允许任意来源的流量” -->设置协议和端口：“tcp:你的端口号” 

### 6.在服务器上安装、配置SS: 

1)用 Google Cloud 有自带的SSH工具, 链接上服务器。

2)输入命令：`sudo -i` 获取`root`权限;

3)然后输入 `yum install -y emacs python python-pip` 安装 Emacs 编辑器和 Python (编辑器用于编辑SS的配置文件，Python用于运行SS)。

4)等待一会儿后安装完毕，这时输入命令`pip install shadowsocks` 安装SS;

5)输入命令`emacs /etc/ss.json` 打开编辑器，并打开一个名为`ss.json`的配置文件保存在`/etc/`目录下。以下是SS官方的默认配置：
```json
	{
	    "server":"你的服务器静态IP地址",
	    "server_port":端口号, //端口号需要与步骤5设置的一致
	    "password":"你的密码",
	    "timeout":600,
	    "method":"rc4-md5", 
	    "auth": true
	}
```

6)配置完成后, 按`ctrl + x` 然后 `ctrl + s` 保存文件，再按 `ctrl + x `然后 `ctrl + c`退出编辑器。

7)最后输入命令`ssserver -c /etc/ss.json -d start`即可启动 Shadowsocks 服务器。

要停止SS服务器（例如需要更改配置文件），输入`ssserver -d stop`即可。

要让SS服务能在后台运行，输入`ssserver -p 你的端口号 -k 你的密码 -m rc4-md5 --user nobody -d start`。到此为止，服务器端的配置已经搞定。


### 6.Win7在配置客户端SS:

1)下载并解压[ss客户端](https://github.com/shadowsocks/shadowsocks-windows/releases);

2)运行`Shadowsocks.exe`，图标会出现在桌面右下方。

3)右击图标--> 点击“系统代理” -->“系统代理模式”选择“PAC模式” -->选择“服务器” --> “编辑服务器”--> 填写服务器地址、端口号、密码、加密方式等信息-->确定。

到此为止，你就可以畅游真正的互联网了。

### 7.安卓手机SS客户端配置：

1）下载 “影梭”

2）填写相应的服务器地址、端口号、密码、加密方式等信息。

