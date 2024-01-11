I. Init


1. sudo c pa bo

🌞 Ajouter votre utilisateur au groupe docker

```
[root@localhost ~]# sudo systemctl start docker
[root@localhost ~]# sudo usermod -aG docker ethan
[root@localhost ~]# sudo systemctl restart docker
```
```
[ethan@localhost etc]$ cat virc
if v:lang =~ "utf8$" || v:lang =~ "UTF-8$"
   set fileencodings=ucs-bom,utf-8,latin1
endif
```

vérifier que vous pouvez taper des commandes docker comme docker ps sans avoir besoin des droits root

1. Un premier conteneur en vif

Je rappelle qu'un "conteneur" c'est juste un mot fashion pour dire qu'on lance un processus un peu isolé sur la machine.

Bon trève de blabla, on va lancer un truc qui juste marche.
On va lancer un conteneur NGINX qui juste fonctionne, puis custom un peu sa conf. Ce serait par exemple pour tester une conf NGINX, ou faire tourner un serveur NGINX de production.

Hé les dévs, jouez le jeu bordel. NGINX c'est pas votre pote OK, mais on s'en fout, c'est une app comme toutes les autres, comme ta chatroom ou ta calculette. Ou Netflix ou LoL ou Spotify ou un malware. NGINX il est réputé et standard, c'est juste un outil d'étude pour nous là. Faut bien que je vous fasse lancer un truc. C'est du HTTP, c'est full standard, vous le connaissez, et c'est facile à tester/consommer : avec un navigateur.

🌞 Lancer un conteneur NGINX

avec la commande suivante :


docker run -d -p 9999:80 nginx



```
[ethan@localhost etc]$ docker run -d -p 9999:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
7b73345df136: Pull complete
Digest: sha256:2bdc49f2f8ae8d8dc50ed00f2ee56d00385c6f8bc8a8b320d0a294d9e3b49026
Status: Downloaded newer image for nginx:latest
```

🌞 Visitons

````
[ethan@localhost etc]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS
                   NAMES
f7cee683af78   nginx     "/docker-entrypoint.…"   8 minutes ago   Up 8 minutes   0.0.0.0:9999->80/tcp,
 :::9999->80/tcp   charming_mcnulty
````
````
[ethan@localhost etc]$ docker logs charming_mcnulty
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/12/22 08:40:18 [notice] 1#1: start worker process 28
````
````
[ethan@localhost ~]$ docker inspect epic_volhard
[
    {
        "Id": "b27b1428716d22fceb7e23c1bd084bb36dd3bdc68028abd08cb86fc2c369e3e4",
        "Created": "2023-12-22T09:45:19.9003248Z",
        "Path": "/docker-entrypoint.sh",
        ...
````
````
[ethan@localhost ~]$ sudo ss -lnpt
State  Recv-Q Send-Q   Local Address:Port   Peer Address:Port Process
LISTEN 0      128            0.0.0.0:22          0.0.0.0:*     users:(("sshd",pid=698,fd=3))
LISTEN 0      4096           0.0.0.0:9999        0.0.0.0:*     users:(("docker-proxy",pid=1676,fd=4))
LISTEN 0      128               [::]:22             [::]:*     users:(("sshd",pid=698,fd=4))
LISTEN 0      4096              [::]:9999           [::]:*     users:(("docker-proxy",pid=1681,fd=4))
````
````
[ethan@localhost ~]$ sudo firewall-cmd --zone=public --add-port=9999/tcp --permanent
success
[ethan@localhost ~]$ sudo firewall-cmd --reload
success
````
🌞 On va ajouter un site Web au conteneur NGINX

créez un dossier nginx

pas n'importe où, c'est ta conf caca, c'est dans ton homedir donc /home/<TON_USER>/nginx/



dedans, deux fichiers : index.html (un site nul) site_nul.conf (la conf NGINX de notre site nul)
exemple de index.html :


<h1>MEOOOW</h1>


````
[ethan@localhost ~]$ mkdir /home/ethan/nginx
[ethan@localhost ~]$ cd /home/ethan/nginx
[ethan@localhost nginx]$ echo '<h1>MEOOOW</h1>' > index.html
[ethan@localhost nginx]$ echo '
server {
    listen        8080;

    location / {
        root /var/www/html;
    }
}
' > site_nul.conf
````
```
[ethan@localhost nginx]$ cd
[ethan@localhost ~]$ docker cp /home/ethan/nginx/. b27b1428716d:/etc/nginx/sites-available/
Successfully copied 3.58kB to b27b1428716d:/etc/nginx/sites-available/
[ethan@localhost ~]$ docker restart b27b1428716d
b27b1428716d
```
````
[ethan@localhost ~]$ sudo systemctl restart docker
[sudo] password for ethan:
[ethan@localhost ~]$ docker run -d -p 9999:8080 -v /home/ethan/nginx/index.html:/var/www/html/index.html -v /home/ethan/nginx/site_nul.conf:/etc/nginx/conf.d/site_nul.conf nginx
6f511ad538c79c3af67d00a11a897db94326754169fb78da1689b35ff388ea90
````

🌞 Visitons

````
[ethan@localhost ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                               NAMES
6f511ad538c7   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   80/tcp, 0.0.0.0:9999->8080/tcp, :::9999->8080/tcp   busy_edison
````

1. Un deuxième conteneur en vif
Cette fois on va lancer un conteneur Python, comme si on voulait tester une nouvelle lib Python par exemple. Mais sans installer ni Python ni la lib sur notre machine.
On va donc le lancer de façon interactive : on lance le conteneur, et on pop tout de suite un shell dedans pour faire joujou.

🌞 Lance un conteneur Python, avec un shell

il faut indiquer au conteneur qu'on veut lancer un shell
un shell c'est "interactif" : on saisit des trucs (input) et ça nous affiche des trucs (output)

il faut le préciser dans la commande docker run avec -it



ça donne donc :


# on lance un conteneur "python" de manière interactive
# et on demande à ce conteneur d'exécuter la commande "bash" au démarrage
docker run -it python bash



Ce conteneur ne vit (comme tu l'as demandé) que pour exécuter ton bash. Autrement dit, si ce bash se termine, alors le conteneur s'éteindra. Autrement diiiit, si tu quittes le bash, le processus bash va se terminer, et le conteneur s'éteindra. C'est vraiment un conteneur one-shot quoi quand on utilise docker run comme ça.

🌞 Installe des libs Python

une fois que vous avez lancé le conteneur, et que vous êtes dedans avec bash

installez deux libs, elles ont été choisies complètement au hasard (avec la commande pip install):

aiohttp
aioconsole


tapez la commande python pour ouvrir un interpréteur Python
taper la ligne import aiohttp pour vérifier que vous avez bien téléchargé la lib


Notez que la commande pip est déjà présente. En effet, c'est un conteneur python, donc les mecs qui l'ont construit ont fourni la commande pip avec !

➜ Tant que t'as un shell dans un conteneur, tu peux en profiter pour te balader. Tu peux notamment remarquer :

si tu fais des ls un peu partout, que le conteneur a sa propre arborescence de fichiers
si t'essaies d'utiliser des commandes usuelles un poil évoluées, elles sont pas là

genre t'as pas ip a ou ce genre de trucs
un conteneur on essaie de le rendre le plus léger possible
donc on enlève tout ce qui n'est pas nécessaire par rapport à un vrai OS
juste une application et ses dépendances