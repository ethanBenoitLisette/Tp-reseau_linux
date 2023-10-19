Partie 1 : Mise en place et maîtrise du serveur Web


🌞 Installer le serveur Apache

````
[ethan@localhost ~]$ sudo dnf install httpd

Installed:
  apr-1.7.0-11.el9.x86_64                            apr-util-1.6.1-20.el9.x86_64
  apr-util-bdb-1.6.1-20.el9.x86_64                   apr-util-openssl-1.6.1-20.el9.x86_64
  httpd-2.4.53-7.el9.x86_64                          httpd-core-2.4.53-7.el9.x86_64
  httpd-filesystem-2.4.53-7.el9.noarch               httpd-tools-2.4.53-7.el9.x86_64
  mailcap-2.1.49-5.el9.noarch                        mod_http2-1.15.19-2.el9.x86_64
  mod_lua-2.4.53-7.el9.x86_64                        rocky-logos-httpd-90.13-1.el9.noarch

Complete!
````


🌞 Démarrer le service Apache
````
[ethan@localhost conf]$ ss -alpn | grep httpd
u_str LISTEN 0      100                   /etc/httpd/run/cgisock.1621 22480                  * 0        
[ethan@localhost conf]$ sudo firewall-cmd --add-port=100/tcp --permanent
success
````


🌞 TEST

````
[ethan@localhost conf]$ ps -ef | grep apache
apache      1622    1621  0 16:41 ?        00:00:00 /usr/sbin httpd -DFOREGROUND
````
````
<!doctype html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>HTTP Server Test Page powered by: Rocky Linux</title>
    <style type="text/css">
  ````

1. Avancer vers la maîtrise du service
🌞 Le service Apache...

```` 
[Unit]
Description=The Apache HTTP Server
Wants=httpd-init.service
After=network.target remote-fs.target nss-lookup.target httpd-init.service
Documentation=man:httpd.service(8)
````

🌞 Déterminer sous quel utilisateur tourne le processus Apache

````
[ethan@localhost /]$sudo nano /etc/httpd/conf/httpd.conf
 User apache
[ethan@localhost /]$ps -ef | grep apache
 apache      1622    1621  0 Dec12 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
````


````
[ethan@localhost /]$ ls -al /usr/share/testpage/
total 12
drwxr-xr-x.  2 root root   24 Dec 12 16:01 .
drwxr-xr-x. 78 root root 4096 Dec 12 16:01 .
````

🌞 Changer l'utilisateur utilisé par Apache

créez un nouvel utilisateur

pour les options de création, inspirez-vous de l'utilisateur Apache existant

le fichier /etc/passwd contient les informations relatives aux utilisateurs existants sur la machine
servez-vous en pour voir la config actuelle de l'utilisateur Apache par défaut (son homedir et son shell en particulier)




modifiez la configuration d'Apache pour qu'il utilise ce nouvel utilisateur
````
[ethan@localhost ~]$ sudo nano /etc/httpd/conf/httpd.conf
User no
Group no
[ethan@localhost ~]$ sudo ps -ef | grep no
no          2448    2447  0 16:24 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
````

🌞 Faites en sorte que Apache tourne sur un autre port

````
[ethan@localhost ~]$ cat /etc/httpd/conf/httpd.conf |grep 100
Listen 100
````
````
[ethan@localhost ~]$ sudo ss -alnpt | grep 100
[sudo] password for ethan:
LISTEN 0      511                *:100             *:*    users:(("httpd",pid=2853,fd=4),("httpd",pid=2852,fd=4),("httpd",pid=2851,fd=4),("httpd",pid=2849,fd=4))
````

📁 fichier  [ /etc/httpd/conf/httpd.conf](./config/httpd.conf)