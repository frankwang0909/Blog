+++
categories = ["tools"]
tags = ["WordPress"]
date = "2017-08-02T21:23:27+08:00"
title = "Centos Wp"
keywords = ["CentOS", "WordPress", "Build a website", "LNMP"]
description = "Build a WordPress blog on CentOS system. First, you need to prepare the basic operating environment that the WordPress blog system depends on."
url = "/centos_wordpress.html"

+++

When the financial budget or human resources are limited, `WordPress` is still the best choice to quickly build a blog or corporate website.

Recently, I used `WordPres`s while learning to build a simple official website for a brother company. The code is debugged locally. Today I learned how to publish this program on the server.

Note: The server is a cloud host on Tencent, and the operating system is `CentOS` 6.8 64-bit.

## 1. Prepare LNMP environment

`LNMP` is the abbreviation of `Linux, Nginx, MySQL and PHP` and is the basic operating environment that the `WordPress` blog system relies on. Let's first prepare the LNMP environment.

### 1.1 Install Nginx

Install `Nginx` using `yum`:

yum install nginx -y

Modify `/etc/nginx/conf.d/default.conf` to remove the monitoring of `IPv6` addresses (`CentOS 6` does not support IPv6, you need to cancel the monitoring of IPv6 addresses, otherwise `Nginx` cannot start successfully), you can refer to the following example:

server {
	    listen 80 default_server;
	    # listen [::]:80 default_server;
	    server_name _;
	    root /usr/share/nginx/html;

# Load configuration files for the default server block.
	    include /etc/nginx/default.d/*.conf;

location/{
	    }

error_page 404 /404.html;
	        location = /40x.html {
	    }

error_page 500 502 503 504 /50x.html;
	        location = /50x.html {
	    }

}

After the modification is completed, start `Nginx`:

nginx

At this point, you can access the external HTTP service of the cloud host to confirm whether the installation has been successful.

Set `Nginx` to `start automatically at boot`:

chkconfig nginx on


### 1.2 Install MySQL

Install `MySQL` using `yum`:

yum install mysql-server -y


After the installation is complete, start the `MySQL` service:

service mysqld restart

Set the `MySQL` account `root` password:

/usr/bin/mysqladmin -u root password 'yourPassword4WordPress'


Set `MySQ`L to `start automatically at boot`:

chkconfig mysqld on


### 1.3 Install PHP

Install `PHP` using `yum`:

yum install php-fpm php-mysql -y

(CentOs 6 has PHP-FPM and PHP-MYSQL installed by default. Executing the above command may prompt that they are already installed.)

After installation, start the `PHP-FPM` process:

service php-fpm start


After starting, you can use the following command to check which port the `PHP-FPM` process is listening on (PHP-FPM listens to port 9000 by default)

netstat -nlpt | grep php-fpm


Set `PHP-FPM` to `start automatically at boot`:

chkconfig php-fpm on


## 2. Install and configure WordPress

### 2.1 Install WordPress

After configuring the `LNMP` environment, continue to use `yum` to install `WordPress`:

yum install wordpress -y

After the installation is complete, you can see the source code of `WordPress` in `/usr/share/wordpress`.



### 2.2 Configure database

Configuration to enter `MySQL`:

mysql -uroot --password='yourPassword4WordPress'

Create a database for `WordPress`:

CREATE DATABASE wordpress;


The `MySQL` part is set up, we exit the `MySQL` environment:

exit

To synchronize the above `DB` configuration to the `configuration file` of `WordPress`, please refer to the following configuration:

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
	define('AUTH_KEY', 'put your unique phrase here');
	define('SECURE_AUTH_KEY', 'put your unique phrase here');
	define('LOGGED_IN_KEY', 'put your unique phrase here');
	define('NONCE_KEY', 'put your unique phrase here');
	define('AUTH_SALT', 'put your unique phrase here');
	define('SECURE_AUTH_SALT', 'put your unique phrase here');
	define('LOGGED_IN_SALT', 'put your unique phrase here');
	define('NONCE_SALT', 'put your unique phrase here');

/**#@-*/

/**
	 * WordPress Database Table prefix.
	 *
	 * You can have multiple installations in one database if you give each
	 * a unique prefix. Only numbers, letters, and underscores please!
	 */
	$table_prefix = 'wp_';

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


### 2.3 Configure Nginx

`WordPress` has been installed, we configure `Nginx` to forward requests to `PHP-FPM` for processing.

First, rename the default configuration file (because the default Server listens on port 80, which conflicts with the WordPress service port, rename it to .bak suffix to disable the default configuration)

cd /etc/nginx/conf.d/

mv default.conf defaut.conf.bak

Create wordpress.conf configuration in /etc/nginx/conf.d, refer to the following content:

server {
	    listen 80;
	    root /usr/share/wordpress;
	    location/{
	        index index.php index.html index.htm;
	        try_files $uri $uri/ /index.php index.php;
	    }
	    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
	    location ~ .php$ {
	        fastcgi_pass 127.0.0.1:9000;
	        fastcgi_index index.php;
	        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
	        include fastcgi_params;
	    }
	}

After configuration, notify the `Nginx` process to reload:

nginx -s reload


## 3. Prepare domain name and resolution

### 3.1 Domain name registration

### 3.2 Domain name resolution

The WordPress blog has been deployed. You can access the blog through a browser to view the effect.

View by IP address:

Blog access address: `http://your server public IP address/wp-admin/install.php`.

View by domain name:

Blog access address: `http://your domain name/wp-admin/install.php`.