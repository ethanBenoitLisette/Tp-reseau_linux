I. Simple bs program
Première partie pour mettre en place un environnement fonctionnel et deux programmes simples qui discutent à travers le réseau.


I. Simple bs program

1. First steps
2. User friendly
3. You say client I hear control




1. First steps

Référez-vous au cours sur les sockets pour la syntaxe.

🌞 bs_server_I1.py

écoute sur une IP spécifique et port 13337 en TCP
répond automatiquement "Hi mate !" dès qu'un client se connecte
affiche la réponse des clients qui se connectent


Il faudra ouvrir ce port dans le firewall de la machine.

🌞 bs_client_I1.py

se connecte à l'IP spécifique de la VM serveur et au port 13337
envoie la string "Meooooo !"
affiche une éventuelle réponse
quitte proprement

➜ Pour quitter proprement, on attend pas juste que l'exécution arrive en fin de fichier, mais on quitte explicitement

librairie sys

elle contient une méthode exit()

la méthode exit() prend un entier en paramètre : le code retour à retourner quand le programme se termine. Pour rappel :


0 veut dire que le programme s'est terminé correctement
autre chose veut dire que le programme ne s'est pas terminé correctement



🌞 Commandes...

je veux dans le compte-rendu toutes les commandes réalisées sur le client et le serveur pour que ça fonctionne
et je veux aussi voir une exécution de votre programme
oh et je veux un ss sur le serveur

n'affiche qu'une ligne : celle qui concerne l'écoute de notre programme
ajoutez les bonnes options à ss ainsi qu'un | grep ... pour n'afficher que la bonne ligne

Commande du client :
```
[root@localhost TP4]# python bs_client_I1.py
b'Hi mate!'
```
Commande du server :
```
[root@localhost TP4]# sudo firewall-cmd --add-port=13337/tcp --permanent
success
[root@localhost TP4]# sudo firewall-cmd --add-port=13337/tcp --permanent
success
[root@localhost TP4]# python bs_server_I1.py
b'Meooooo !'
```





2. User friendly
🌞 bs_client_I2.py

Vous aurez besoin du cours sur la gestion d'erreurs pour cette partie.


````
[root@localhost TP4]# python bs_client_I2.py
Connecté avec succès au serveur 10.0.3.17 sur le port 13337
Hi mate!
Que veux-tu envoyer au serveur :
ui
Mes respects humble humain.
[root@localhost TP4]# python bs_client_I2.py
Connecté avec succès au serveur 10.0.3.17 sur le port 13337
Hi mate!
Que veux-tu envoyer au serveur :
meo
Meo à toi confrère.
[root@localhost TP4]# python bs_client_I2.py
Connecté avec succès au serveur 10.0.3.17 sur le port 13337
Hi mate!
Que veux-tu envoyer au serveur :
waf
ptdr t ki
````





🌞 bs_server_I2.py

retour visuel

afficher un message de succès quand un client se co
le message doit être : Un client vient de se co et son IP c'est <CLIENT_IP>.



````
[root@localhost TP4]# python bs_server_I2.py
Un client vient de se connecter et son IP est 10.0.3.16
ui
Un client vient de se connecter et son IP est 10.0.3.16
meo
Un client vient de se connecter et son IP est 10.0.3.16
waf
````





3. You say client I hear control
On va ajouter un peu de contrôle pour éviter que notre client fasse nawak à l'utilisation du programme.
🌞 bs_client_I3.py






II. You say dev I say good practices


1. Args

🌞 bs_server_II1.py

On devra donc pouvoir faire :

$ python bs_server_II1.py -p 8888

```

```



1. Logs
Allô les dévs ? Ici it4 l'admin qui vous parle. Ils sont où les ptain de logs de votre application bowdel.

Ce qu'on voudrait veut :
➜ des logs serveur

dans la console
dans un fichier de log

➜ des logs client

PAS dans la console : c'est le client, c'est un moldu, on lui montre R
dans un fichier de log


Chaque ligne de log :


doit être timestamped

préfixée par date et heure, dans un format standard si possible



doit être nivelée

je viens d'inventer le terme
c'est à dire que vous préciser un niveau de logging



Il existe des standards sur les niveaux de log en informatique. Les trois en gras sont les plus utilisés. En haut le plus critique, en bas, le moins :

Emergency
Alert
Critical

Error : ERROR ou ERR en rouge

Warning : WARNING ou WARN en jaune
Notice

Informational : INFO en blanc
Debug

Toutes les lignes de log de ce TP devront être au format suivant :

yyyy-mm-dd hh:mm:ss LEVEL message


Par exemple :

2023-11-03 03:43:21 INFO Un client vient de se co et son IP c'est <CLIENT_IP>.



A. Logs serveur
Le serveur va log chacune des actions à la fois dans la console, et aussi dans un fichier.
Ce fichier il est pas à n'importe quel endroit si on utilise un système GNU/Linux, un dossier est dédié aux logs : /var/log/.
On peut donc créer là-bas un sous-dossier pour notre application, et on stocke dedans le fichier de log de notre application.
Vous pouvez faire ça à la main, ou utiliser la librairie logger, vous êtes libres pour le moment ! (logger c'est le feu quand même).
🌞 bs_server_II2A.py

ce qui doit générer une ligne de log :


INFO lancement du serveur

Le serveur tourne sur <IP>:<port>



INFO connexion d'un client

l'IP du client doit apparaître dans la ligne de log
Un client <IP_CLIENT> s'est connecté.



INFO message reçu d'un client

Le client <IP_CLIENT> a envoyé <MESSAGE>.



INFO message envoyé par le serveur

Réponse envoyée au client <IP_CLIENT> : <MESSAGE>.



WARN aucun client connecté depuis + de 1 minute

le message : Aucun client depuis plus de une minute.

il doit apparaître toutes les minutes si personne ne se co




en console

le mot-clé INFO doit apparaître en blanc
le mot clé WARN doit apparaître en jaune


dans un fichier

le fichier doit être /var/log/bs_server/bs_server.log

le créer en amont si nécessaire, précisez la(les) commande(s) dans le compte-rendu




B. Logs client
Les logs du client, c'est que dans un fichier. En effet, que ce soit une app console ou graphique, le client on veut lui montrer que ce qui est directement lié à SON utilisation de l'application. Et pas le reste.
Donc on lui jette pas les logs et des vilaines erreurs au visage, ni 14000 messages informatifs.
Je vous laisse choisir l'emplacement du fichier de log de façon pertinente.
🌞 bs_client_II2B.py

ce qui doit générer une ligne de log :


INFO connexion réussie à un serveur

Connexion réussie à <IP>:<PORT>.



INFO message envoyé par le client

Message envoyé au serveur <IP_SERVER> : <MESSAGE>.



INFO message reçu du serveur

Réponse reçue du serveur <IP_SERVER> : <MESSAGE>.



ERROR connexion au serveur échouée

pour le tester, il suffit de lancer le client alors que le serveur est éteint !
le message : Impossible de se connecter au serveur <IP_SERVER> sur le port <PORT>.





en console

affiche juste ERROR Impossible de se connecter au serveur <IP_SERVER> sur le port <PORT>. en rouge quand ça fail (pas de timestamp là)
les messages de niveau INFO ne sont pas visibles dans la console du client


dans un fichier

<DOSSIER_DE_LOG>/bs_client.log




C. NOTE IMPORTANTE
A partir de maintenant, vous savez gérer des logs à peu près proprement.
Vous allez dév plusieurs machins en cours, vous devrez utiliser exactement la même méthode que précédemment pour générer les logs : timestamp, niveau de log, message, stocké dans un fichier précis etc.