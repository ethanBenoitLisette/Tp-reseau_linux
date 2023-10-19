TP2 : Appréhender l'environnement Linux

(note: le tp à été fait avec une vm que axrl m'a passer via clé usb d'ou le nom dans les rep)

🌞 S'assurer que le service sshd est démarré

```
[axel@localhost ~]$ systemctl status
           │ ├─sshd.service
           │ │ └─684 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
```


🌞 Analyser les processus liés au service SSH

```
[axel@localhost ~]$ ps -e |grep sshd
    691 ?        00:00:00 sshd
 ```

🌞 Déterminer le port sur lequel écoute le service SSH

```
[axel@localhost ~]$ ss -e |grep sshd
tcp   ESTAB  0      52                       10.0.0.11:ssh           10.0.0.1:49562  timer:(on,229ms,0) ino:19268 sk:28 cgroup:/system.slice/sshd.service <->
```

🌞 Consulter les logs du service SSH

```
[axel@localhost ~]$ journalctl |grep ssh
Nov 27 21:42:33 localhost systemd[1]: Created slice Slice /system/sshd-keygen.
Nov 27 21:42:34 localhost systemd[1]: Reached target sshd-keygen.target.
Nov 27 21:42:34 localhost sshd[691]: Server listening on 0.0.0.0 port 22.
Nov 27 21:42:34 localhost sshd[691]: Server listening on :: port 22.
Nov 27 21:43:03 localhost.localdomain sshd[837]: Accepted password for axel from 10.0.0.1 port 49562 ssh2
Nov 27 21:43:03 localhost.localdomain sshd[837]: pam_unix(sshd:session): session opened for user axel(uid=1000) by (uid=0)
```




1. Modification du service

🌞 Identifier le fichier de configuration du serveur SSH

````
[axel@localhost ssh]$ cat ssh_config
#       $OpenBSD: ssh_config,v 1.35 2020/07/17 03:43:42 dtucker Exp $

# This is the ssh client system-wide configuration file.  See
# ssh_config(5) for more information.  This file provides defaults for
# users, and the values can be changed in per-user configuration files
````
🌞 Modifier le fichier de conf

````
[axel@localhost ssh]$ cat ssh_config | grep Port
#   Port 24
````

````
[axel@localhost ssh]$ sudo  firewall-cmd --list-all | grep port
  ports:
````




🌞 Redémarrer le service
```
[axel@localhost ssh]$ sudo systemctl restart sshd
```

🌞 Effectuer une connexion SSH sur le nouveau port

depuis votre PC
il faudra utiliser une option à la commande ssh pour vous connecter à la VM


Je vous conseille de remettre le port par défaut une fois que cette partie est terminée.

✨ Bonus : affiner la conf du serveur SSH

faites vos plus belles recherches internet pour améliorer la conf de SSH
par "améliorer" on entend essentiellement ici : augmenter son niveau de sécurité
le but c'est pas de me rendre 10000 lignes de conf que vous pompez sur internet pour le bonus, mais de vous éveiller à divers aspects de SSH, la sécu ou d'autres choses liées



II. Service HTTP

1. Mise en place

🌞 Installer le serveur NGINX

````
[axel@localhost ssh]$ sudo apt install nginx
 Installed:
  nginx-1:1.20.1-13.el9.x86_64                  nginx-core-1:1.20.1-13.el9.x86_64                  nginx-filesystem-1:1.20.1-13.el9.noarch                  rocky-logos-httpd-90.13-1.el9.noarch

Complete!
````
🌞 Démarrer le service NGINX
````
[axel@localhost ssh]$ sudo systemctl start nginx
````
🌞 Déterminer sur quel port tourne NGINX
````
[axel@localhost ssh]$ sudo firewall-cmd --add-port=80/tcp --permanent
success
````
````
[axel@localhost nginx]$ cat nginx.conf | grep listen
        listen       80;
        listen       [::]:80;
````

🌞 Déterminer les processus liés à l'exécution de NGINX

vous devez filtrer la sortie de la commande utilisée pour n'afficher que les lignes demandées

🌞 Euh wait

y'a un serveur Web qui tourne là ?
bah... visitez le site web ?

ouvrez votre navigateur (sur votre PC) et visitez http://<IP_VM>:<PORT>

vous pouvez aussi (toujours sur votre PC) utiliser la commande curl depuis un terminal pour faire une requête HTTP


dans le compte-rendu, je veux le curl (pas un screen de navigateur)

utilisez Git Bash si vous êtes sous Windows (obligatoire)
vous utiliserez | head après le curl pour afficher que certaines des premières lignes
vous utiliserez une option à cette commande head pour afficher les 7 premières lignes de la sortie du curl





1. Analyser la conf de NGINX
🌞 Déterminer le path du fichier de configuration de NGINX

faites un ls -al <PATH_VERS_LE_FICHIER> pour le compte-rendu

🌞 Trouver dans le fichier de conf

les lignes qui permettent de faire tourner un site web d'accueil (la page moche que vous avez vu avec votre navigateur)

ce que vous cherchez, c'est un bloc server { } dans le fichier de conf
vous ferez un cat <FICHIER> | grep <TEXTE> -A X pour me montrer les lignes concernées dans le compte-rendu

l'option -A X permet d'afficher aussi les X lignes après chaque ligne trouvée par grep





une ligne qui parle d'inclure d'autres fichiers de conf

encore un cat <FICHIER> | grep <TEXTE>

bah ouais, on stocke pas toute la conf dans un seul fichier, sinon ça serait le bordel




3. Déployer un nouveau site web
🌞 Créer un site web

bon on est pas en cours de design ici, alors on va faire simplissime
créer un sous-dossier dans /var/www/

par convention, on stocke les sites web dans /var/www/

votre dossier doit porter le nom tp2_linux



dans ce dossier /var/www/tp2_linux, créez un fichier index.html

il doit contenir <h1>MEOW mon premier serveur web</h1>




🌞 Adapter la conf NGINX

dans le fichier de conf principal

vous supprimerez le bloc server {} repéré plus tôt pour que NGINX ne serve plus le site par défaut
redémarrez NGINX pour que les changements prennent effet


créez un nouveau fichier de conf

il doit être nommé correctement
il doit être placé dans le bon dossier
c'est quoi un "nom correct" et "le bon dossier" ?

bah vous avez repéré dans la partie d'avant les fichiers qui sont inclus par le fichier de conf principal non ?
créez votre fichier en conséquence


redémarrez NGINX pour que les changements prennent effet
le contenu doit être le suivant :




server {
  # le port choisi devra être obtenu avec un 'echo $RANDOM' là encore
  listen <PORT>;

  root /var/www/tp2_linux;
}


🌞 Visitez votre super site web

toujours avec une commande curl depuis votre PC (ou un navigateur)


III. Your own services
Dans cette partie, on va créer notre propre service :)
HE ! Vous vous souvenez de netcat ou nc ? Le ptit machin de notre premier cours de réseau ? C'EST L'HEURE DE LE RESORTIR DES PLACARDS.

1. Au cas où vous auriez oublié
Au cas où vous auriez oublié, une petite partie qui ne doit pas figurer dans le compte-rendu, pour vous remettre nc en main.

Allez-le télécharger sur votre PC si vous ne l'avez pu. Lien dans Google ou dans le premier TP réseau.

➜ Dans la VM


nc -l 8888

lance netcat en mode listen
il écoute sur le port 8888
sans rien préciser de plus, c'est le port 8888 TCP qui est utilisé



➜ Sur votre PC

nc <IP_VM> 8888
vérifiez que vous pouvez envoyer des messages dans les deux sens


Oubliez pas d'ouvrir le port 8888/tcp de la VM bien sûr :)


2. Analyse des services existants
Un service c'est quoi concrètement ? C'est juste un processus, que le système lance, et dont il s'occupe après.
Il est défini dans un simple fichier texte, qui contient une info primordiale : la commande exécutée quand on "start" le service.
Il est possible de définir beaucoup d'autres paramètres optionnels afin que notre service s'exécute dans de bonnes conditions.
🌞 Afficher le fichier de service SSH

vous pouvez obtenir son chemin avec un systemctl status <SERVICE>

mettez en évidence la ligne qui commence par ExecStart=

encore un cat <FICHIER> | grep <TEXTE>

c'est la ligne qui définit la commande lancée lorsqu'on "start" le service

taper systemctl start <SERVICE> ou exécuter cette commande à la main, c'est (presque) pareil





🌞 Afficher le fichier de service NGINX

mettez en évidence la ligne qui commence par ExecStart=



3. Création de service

Bon ! On va créer un petit service qui lance un nc. Et vous allez tout de suite voir pourquoi c'est pratique d'en faire un service et pas juste le lancer à la min.
Ca reste un truc pour s'exercer, c'pas non plus le truc le plus utile de l'année que de mettre un nc dans un service n_n
🌞 Créez le fichier /etc/systemd/system/tp2_nc.service

son contenu doit être le suivant (nice & easy)


[Unit]
Description=Super netcat tout fou

[Service]
ExecStart=/usr/bin/nc -l <PORT>



Vous remplacerez <PORT> par un numéro de port random obtenu avec la même méthode que précédemment.

🌞 Indiquer au système qu'on a modifié les fichiers de service

la commande c'est sudo systemctl daemon-reload


🌞 Démarrer notre service de ouf

avec une commande systemctl start


🌞 Vérifier que ça fonctionne

vérifier que le service tourne avec un systemctl status <SERVICE>

vérifier que nc écoute bien derrière un port avec un ss

vous filtrerez avec un | grep la sortie de la commande pour n'afficher que les lignes intéressantes


vérifer que juste ça marche en vous connectant au service depuis votre PC

➜ Si vous vous connectez avec le client, que vous envoyez éventuellement des messages, et que vous quittez nc avec un CTRL+C, alors vous pourrez constater que le service s'est stoppé

bah oui, c'est le comportement de nc ça !
le client se connecte, et quand il se tire, ça ferme nc côté serveur aussi
faut le relancer si vous voulez retester !

🌞 Les logs de votre service

mais euh, ça s'affiche où les messages envoyés par le client ? Dans les logs !

sudo journalctl -xe -u tp2_nc pour visualiser les logs de votre service

sudo journalctl -xe -u tp2_nc -f  pour visualiser en temps réel les logs de votre service


-f comme follow (on "suit" l'arrivée des logs en temps réel)


dans le compte-rendu je veux

une commande journalctl filtrée avec grep qui affiche la ligne qui indique le démarrage du service
une commande journalctl filtrée avec grep qui affiche un message reçu qui a été envoyé par le client
une commande journalctl filtrée avec grep qui affiche la ligne qui indique l'arrêt du service



🌞 Affiner la définition du service

faire en sorte que le service redémarre automatiquement s'il se termine

comme ça, quand un client se co, puis se tire, le service se relancera tout seul
ajoutez Restart=always dans la section [Service] de votre service
n'oubliez pas d'indiquer au système que vous avez modifié les fichiers de service :)