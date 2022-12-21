

🌞 Install de MariaDB sur db.tp5.linux

````
[ethan@localhost ~]$ sudo dnf install mariadb-server
Last metadata expiration check: 1:16:40 ago on Tue Dec 20 03:21:59 2022.
Complete!
````
````
[ethan@localhost ~]$ sudo systemctl enable mariadb
Created symlink /etc/systemd/system/mysql.service → /usr/lib/systemd/system/mariadb.service.
Created symlink /etc/systemd/system/mysqld.service → /usr/lib/systemd/system/mariadb.service.
Created symlink /etc/systemd/system/multi-user.target.wants/mariadb.service → /usr/lib/systemd/system/mariadb.service.
````
````
[ethan@localhost ~]$ sudo systemctl start mariadb
````
````
[ethan@localhost ~]$ sudo mysql_secure_installation

NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB

Thanks for using MariaDB!
````

🌞 Port utilisé par MariaDB

````
[ethan@localhost ~]$ ss -a|grep mysql
u_str LISTEN 0      80                      /var/lib/mysql/mysql.sock 37110                         * 0 
````
````
[ethan@localhost ~]$ sudo firewall-cmd --add-port=37110/tcp --permanent
success
[ethan@localhost ~]$ sudo firewall-cmd --reload
success
````
La doc vous fait exécuter la commande mysql_secure_installation c'est un bon réflexe pour renforcer la base qui a une configuration un peu chillax à l'install.

🌞 Processus liés à MariaDB
````
[ethan@localhost ~]$ ps -ef | grep mysql
mysql      12936       1  0 04:43 ?        00:00:00 /usr/libexec/mariadbd --basedir=/usr
````


➜ Une fois la db en place, go sur la partie 3.