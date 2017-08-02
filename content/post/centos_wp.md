+++
categories = ["tools"]
tags = ["WordPress"]
date = "2017-08-02T21:23:27+08:00"
title = "在 CentOS 上搭建 WordPress 博客"
keywords = ["CentOS", "WordPress", "建站", "LNMP"]
description = "CentOS 系统上搭建 WordPress 博客。首先需要准备 WordPress 博客系统依赖的基础运行环境。 "
url = "centos_wordpress.html"

+++

在资金预算或人力资源有限的情况下， `WordPress` 仍然是快速地搭建博客或者企业网站的不二选择。

最近，边学边干地使用 `WordPres`s 给兄弟公司搭建一个简单的官网。代码在本地调试好了。今天学习了如何学在服务器上发布这个程序。

备注：服务器是腾讯上的云主机， 操作系统是 `CentOS` 6.8 64 位的。 

## 一、准备 `LNMP` 环境

`LNMP` 是 `Linux、Nginx、MySQL 和 PHP` 的缩写，是 `WordPress `博客系统依赖的基础运行环境。我们先来准备 LNMP 环境。

### 1. 安装 `Nginx`

使用 `yum` 安装 `Nginx`：

	yum install nginx -y

修改 `/etc/nginx/conf.d/default.conf`，去除对 `IPv6` 地址的监听（`CentOS 6` 不支持 IPv6，需要取消对 IPv6 地址的监听，否则 `Nginx` 不能成功启动），可参考下面的示例：

	server {
	    listen       80 default_server;
	    # listen       [::]:80 default_server;
	    server_name  _;
	    root         /usr/share/nginx/html;

	    # Load configuration files for the default server block.
	    include /etc/nginx/default.d/*.conf;

	    location / {
	    }

	    error_page 404 /404.html;
	        location = /40x.html {
	    }

	    error_page 500 502 503 504 /50x.html;
	        location = /50x.html {
	    }

	}

修改完成后，启动 `Nginx`：

	nginx

此时，可访问云主机的外网 HTTP 服务来确认是否已经安装成功。

将 `Nginx` 设置为`开机自动启动`：

	chkconfig nginx on


### 2.安装 `MySQL`

使用 `yum` 安装 `MySQL`：

	yum install mysql-server -y


安装完成后，启动 `MySQL` 服务：

	service mysqld restart

设置 `MySQL` 账户 `root` 密码：

	 /usr/bin/mysqladmin -u root password 'yourPassword4WordPress'


将 `MySQ`L 设置为`开机自动启动`：

	chkconfig mysqld on


### 3.安装 `PHP`

使用 `yum` 安装 `PHP`：

	yum install php-fpm php-mysql -y

（CentOs 6 默认已经安装了 PHP-FPM 及 PHP-MYSQL，上述命令执行的可能会提示已经安装。）

安装之后，启动 `PHP-FPM` 进程：

	service php-fpm start


启动之后，可以使用下面的命令查看 `PHP-FPM` 进程监听哪个端口 （PHP-FPM 默认监听 9000 端口）

	netstat -nlpt | grep php-fpm


把 `PHP-FPM` 也设置成`开机自动启动`：

	chkconfig php-fpm on


## 二、安装并配置 `WordPress`

### 2.1安装 `WordPres`s

配置好 `LNMP` 环境后，继续使用 `yum` 来安装 `WordPress`：

	yum install wordpress -y

安装完成后，就可以在 `/usr/share/wordpress` 看到 `WordPress` 的源代码了。



### 2.2配置`数据库`

配进入 `MySQL`：

	mysql -uroot --password='yourPassword4WordPress'

为 `WordPress` 创建一个数据库：

	CREATE DATABASE wordpress;


`MySQL` 部分设置完了，我们退出 `MySQL` 环境：

	exit

把上述的 `DB` 配置同步到 `WordPress` 的`配置文件`中，可参考下面的配置：

	<?php
	/**
	 * The base configuration for WordPress
	 *
	 * The wp-config.php creation script uses this file during the
	 * installation. You don't have to use the web site, you can
	 * copy this file to "wp-config.php" and fill in the values.
	 *
	 * This file contains the following configurations:
	 *
	 * * MySQL settings
	 * * Secret keys
	 * * Database table prefix
	 * * ABSPATH
	 *
	 * @link https://codex.wordpress.org/Editing_wp-config.php
	 *
	 * @package WordPress
	 */

	// ** MySQL settings - You can get this info from your web host ** //
	/** The name of the database for WordPress */
	define('DB_NAME', 'wordpress');

	/** MySQL database username */
	define('DB_USER', 'root');

	/** MySQL database password */
	define('DB_PASSWORD', 'yourPassword4WordPress');

	/** MySQL hostname */
	define('DB_HOST', 'localhost');

	/** Database Charset to use in creating database tables. */
	define('DB_CHARSET', 'utf8');

	/** The Database Collate type. Don't change this if in doubt. */
	define('DB_COLLATE', '');

	/**#@+
	 * Authentication Unique Keys and Salts.
	 *
	 * Change these to different unique phrases!
	 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
	 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
	 *
	 * @since 2.6.0
	 */
	define('AUTH_KEY',         'put your unique phrase here');
	define('SECURE_AUTH_KEY',  'put your unique phrase here');
	define('LOGGED_IN_KEY',    'put your unique phrase here');
	define('NONCE_KEY',        'put your unique phrase here');
	define('AUTH_SALT',        'put your unique phrase here');
	define('SECURE_AUTH_SALT', 'put your unique phrase here');
	define('LOGGED_IN_SALT',   'put your unique phrase here');
	define('NONCE_SALT',       'put your unique phrase here');

	/**#@-*/

	/**
	 * WordPress Database Table prefix.
	 *
	 * You can have multiple installations in one database if you give each
	 * a unique prefix. Only numbers, letters, and underscores please!
	 */
	$table_prefix  = 'wp_';

	/**
	 * See http://make.wordpress.org/core/2013/10/25/the-definitive-guide-to-disabling-auto-updates-in-wordpress-3-7
	 */

	/* Disable all file change, as RPM base installation are read-only */
	define('DISALLOW_FILE_MODS', true);

	/* Disable automatic updater, in case you want to allow
	   above FILE_MODS for plugins, themes, ... */
	define('AUTOMATIC_UPDATER_DISABLED', true);

	/* Core update is always disabled, WP_AUTO_UPDATE_CORE value is ignore */

	/**
	 * For developers: WordPress debugging mode.
	 *
	 * Change this to true to enable the display of notices during development.
	 * It is strongly recommended that plugin and theme developers use WP_DEBUG
	 * in their development environments.
	 *
	 * For information on other constants that can be used for debugging,
	 * visit the Codex.
	 *
	 * @link https://codex.wordpress.org/Debugging_in_WordPress
	 */
	define('WP_DEBUG', false);

	/* That's all, stop editing! Happy blogging. */

	/** Absolute path to the WordPress directory. */
	if ( !defined('ABSPATH') )
	    define('ABSPATH', '/usr/share/wordpress');

	/** Sets up WordPress vars and included files. */
	require_once(ABSPATH . 'wp-settings.php');


### 2.3配置 `Nginx`

`WordPress` 已经安装完毕，我们配置`Nginx` 把请求转发给 `PHP-FPM` 来处理。

首先，重命名默认的配置文件（因为默认的 Server 监听 80 端口，与 WordPress 的服务端口冲突，将其重命名为 .bak 后缀以禁用默认配置）

	cd /etc/nginx/conf.d/

	mv default.conf defaut.conf.bak

在 /etc/nginx/conf.d 创建 wordpress.conf 配置，参考下面的内容：

	server {
	    listen 80;
	    root /usr/share/wordpress;
	    location / {
	        index index.php index.html index.htm;
	        try_files $uri $uri/ /index.php index.php;
	    }
	    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
	    location ~ .php$ {
	        fastcgi_pass   127.0.0.1:9000;
	        fastcgi_index  index.php;
	        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
	        include        fastcgi_params;
	    }
	}

配置后，通知 `Nginx` 进程重新加载：

	nginx -s reload


## 三、准备域名和解析

3.1域名注册

3.2域名解析

 WordPress 博客已经部署完成。可以通过浏览器访问博客查看效果。

通过IP地址查看：

博客访问地址：`http://你的服务器公网ip地址/wp-admin/install.php`。

通过域名查看：

博客访问地址：`http://你的域名/wp-admin/install.php`。