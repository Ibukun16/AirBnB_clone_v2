#!/usr/bin/env bash
# Bash Script to Setup web server for Airbnb Static_web 
sudo apt-get update -y
sudo apt-get updgrade -y
sudo apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir /data/web_static/shared/
echo "Holberton School" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://github.com/Ibukun16;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart 
