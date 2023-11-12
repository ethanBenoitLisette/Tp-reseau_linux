

I. Simple bs program




1. First steps
   
[bs_server_I1.py](bs_server_I1.py)

[bs_client_I1.py](bs_client_I1.py)

🌞 Commandes...

Commande du client :
```
[root@localhost TP4]# git clone https://github.com/ethanBenoitLisette/Tp-reseau_linux.git

[root@localhost ~]# cd /etc/Tp-reseau_linux/TP4

[root@localhost TP4]# python bs_client_I1.py
b'Hi mate!'
```
Commande du server :
```
[root@localhost ~]# cd /etc/Tp-reseau_linux/TP4

[root@localhost TP4]# git clone https://github.com/ethanBenoitLisette/Tp-reseau_linux.git

[root@localhost TP4]# sudo firewall-cmd --add-port=13337/tcp --permanent
success

[root@localhost TP4]# sudo firewall-cmd --add-port=13337/tcp --permanent
success

[root@localhost TP4]# python bs_server_I1.py
b'Meooooo !'
```


1. User friendly

[bs_server_I2.py](bs_server_I2.py)

[bs_client_I2.py](bs_client_I2.py)

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





1. You say client I hear control
On va ajouter un peu de contrôle pour éviter que notre client fasse nawak à l'utilisation du programme.
🌞 bs_client_I3.py

[bs_client_I3.py](bs_client_I3.py)






II. You say dev I say good practices


1. Args

🌞 bs_server_II1.py

On devra donc pouvoir faire :

$ python bs_server_II1.py -p 8888

```
[root@localhost TP4]# python bs_server_II1.py -p 8888
Un client vient de se connecter et son IP est 10.0.3.16
ui

[root@localhost TP4]# python bs_server_II1.py -p 52598418
ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).
```



2. Logs



A. Logs serveur

🌞 bs_server_II2A.py


[ bs_server_II2A.py]( bs_server_II2A.py)


B. Logs client

🌞 bs_client_II2B.py

[ bs_client_II2B.py]( bs_client_II2B.py)




C. NOTE IMPORTANTE
A partir de maintenant, vous savez gérer des logs à peu près proprement.
Vous allez dév plusieurs machins en cours, vous devrez utiliser exactement la même méthode que précédemment pour générer les logs : timestamp, niveau de log, message, stocké dans un fichier précis etc.