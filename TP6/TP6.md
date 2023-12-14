1. Premiers pas
🌞 sleep_and_print.py

[sleep_and_print.py](partie-2/sleep_and_print.py)


Le code va exécuter la première fonction (~5 secondes) puis la deuxième (à nouveau ~5 secondes) pour un total de ~10 secondes d'exécution. Pas de surprises.

🌞 sleep_and_print_async.py

[sleep_and_print_async.py](partie-2/sleep_and_print_async.py)



Dès que l'exécution de la première fonction commencera à produire de l'attente, l'exécution de la deuxième commencera.


2. Web Requests
🌞 web_sync.py

on peut l'appeler comme ça : python web_sync.py https://www.ynov.com
[web_sync.py](partie-2/web_sync.py)

🌞 web_async.py

[web_async.py](partie-2/web_async.py)

🌞 web_sync_multiple.py

[web_sync_multiple.py](partie-2/web_sync_multiple.py)

🌞 web_async_multiple.py

[web_async_multiple.py](partie-2/web_async_multiple.py)


🌞 Mesure !

````
[root@localhost TP6]# python web_sync_multiple.py urls.txt
Contenu écrit avec succès dans le fichier : /tmp/web_www.pokepedia.fr_
Contenu écrit avec succès dans le fichier : /tmp/web_www.ynov.com_
Contenu écrit avec succès dans le fichier : /tmp/web_www.monsterhunter.com_
Le programme a pris 2.08 secondes pour s'exécuter.

[root@localhost TP6]# python web_async_multiple.py urls.txt
Contenu écrit avec succès dans le fichier : /tmp/web_www.ynov.com_
Contenu écrit avec succès dans le fichier : /tmp/web_www.pokepedia.fr_
Contenu écrit avec succès dans le fichier : /tmp/web_www.monsterhunter.com_
Le programme a pris 0.35 secondes pour s'exécuter.
````





























1. Première version
Là on veut juste un truc qui ressemble de trèèès loin à un outil de chat. On va avancer ptit à ptit.
🌞 chat_server_ii_2.py

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)


🌞 chat_client_ii_2.py

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)

1. Client asynchrone
Adapter le code du client pour qu'il contienne deux fonctions asynchrones :


🌞 chat_client_ii_3.py

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)


🌞 chat_server_ii_3.py

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)



1. Un chat fonctionnel



🌞 chat_server_ii_4.py

[chat_server_ii_4.py](partie-2/chat_server_ii_4.py)


5. Gérer des pseudos
On va faire en sorte que chaque user choisisse un pseudo, et que le serveur l'enregistre. Ce sera plus sympa que {IP}:{port} pour identifier les clients.
🌞 chat_client_ii_5.py

[chat_client_ii_5.py](partie-2/chat_client_ii_5.py)




Si vous avez encore le client qui envoie juste la string "Hello" à la connexion, enlevez-le !

➜ Dès sa connexion, le client envoie donc un message contenant son pseudo

on peut utiliser ce savoir côté serveur : le premier message d'un client contient le pseudo

🌞 chat_server_ii_5.py

[chat_client_ii_5.py](partie-2/chat_client_ii_5.py)



6. Déconnexion
Enfin, gérer proprement la déconnexion des clients.
Pendant vos tests, vous avez du apercevoir des comportements rigolos quand un client est coupé pendant que le serveur tourne.
Quand un client se déconnecte, il envoie un message vide facilement reconnaissable. Idem si le serveur se déconnecte, il envoie au client un message vide assez reconnaissable.
🌞 chat_server_ii_6.py et chat_client_ii_6.py

côté client, si le serveur se déco

[chat_server_ii_6.py](partie-2/chat_server_ii_6.py)
[chat_client_ii_6.py](partie-2/chat_client_ii_6.py)

Bonus 

6. Gestion d'historique
   
Quand tu rejoins la conversation en retard, t'as pas l'historique, relou.
➜ Gérer un historique de conversation

[chat_server_b-6.py](partie-3/chat_server_b-6.py)
